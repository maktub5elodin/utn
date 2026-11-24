--[[
tp-mecanica.lua — TP Final de Ingeniería Mecánica I (PDF y Word).

Un solo .md genera las dos entregas (variable de entorno TP_VERSION, que fija
tp.mk). A partir del bloque `tp:` del pdf.yaml del documento:

  1. Versión: los bloques `::: solo-e3` (o `solo-e2`) quedan solo en esa versión.
  2. Valores: cada número marcado [13,2]{.v k="res.funcionamiento.fuerza_mano_N"}
     se compara con el JSON de valores (tp.valores), redondeado a los decimales
     escritos. Si no coincide, la compilación se detiene.
  3. Controles de contenido (se detiene si alguno falla): secciones obligatorias
     y por versión, cantidad de láminas, largo de la introducción, del abstract
     y de la conclusión, vocabulario controlado fuera del bloque `::: alternativas`,
     correspondencia entre notas al pie y Bibliografía ∪ Links de interés, orden
     alfabético, imágenes existentes, figuras citadas. Deja un informe JSON en
     .build/aux/controles_<salida>.<formato>.json.
  4. Armado: carátula (PDF: la carátula oficial completada, ya en PDF; en Word
     la inserta docx_tp.py), página de título e índice, `## 1. Sección` -> nivel 1
     (el `# Título` del .md se descarta), láminas a página completa apaisada,
     Bibliografía y Links con sangría francesa, numeración de tablas en Word.
]]

local LATEX = FORMAT:match("latex") ~= nil
local DOCX = FORMAT:match("docx") ~= nil
local text = pandoc.text
local stringify = pandoc.utils.stringify

local VERSION = os.getenv("TP_VERSION")
local SALIDA = os.getenv("TP_SALIDA") or "documento"

local function raw(s)
  if LATEX then return pandoc.RawBlock("latex", s) end
  return pandoc.RawBlock("openxml", s)
end

local function tex(s)
  local out = pandoc.write(pandoc.Pandoc({ pandoc.Plain({ pandoc.Str(s) }) }), "latex")
  return (out:gsub("%s+$", ""))
end

local function tex_inlines(inl)
  local out = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inl) }), "latex")
  return (out:gsub("%s+$", ""))
end

local function existe(ruta)
  local f = io.open(ruta, "r")
  if f then f:close() return true end
  return false
end

local function leer(ruta)
  local f = io.open(ruta, "r")
  if not f then return nil end
  local s = f:read("a"); f:close()
  return s
end

local function lista(v)
  if v == nil then return {} end
  if pandoc.utils.type(v) == "List" then return v end
  return { v }
end

-- Minúsculas sin tildes, para comparar y ordenar
local TILDES = { ["á"] = "a", ["é"] = "e", ["í"] = "i", ["ó"] = "o", ["ú"] = "u", ["ü"] = "u",
                 ["ñ"] = "n", ["ż"] = "z", ["à"] = "a", ["è"] = "e", ["ç"] = "c" }
local function plano(s)
  s = text.lower(s)
  for k, v in pairs(TILDES) do s = s:gsub(k, v) end
  return s
end

local function palabras(s)
  local n = 0
  for w in s:gmatch("%S+") do
    if w:find("[%w\128-\255]") then n = n + 1 end
  end
  return n
end

-- ── Datos del pdf.yaml ──────────────────────────────────────────────────

local function datos(meta)
  local m = meta.tp
  if not m then error("tp-mecanica.lua: falta el bloque `tp:` en pdf.yaml") end
  if VERSION == nil then error("tp-mecanica.lua: falta TP_VERSION (la fija tp.mk: e2 o e3)") end
  local v = m.versiones and m.versiones[VERSION]
  if not v then error("tp-mecanica.lua: tp.versiones." .. VERSION .. " no existe en pdf.yaml") end
  return {
    titulo = stringify(m.titulo),
    pie = stringify(m.pie),
    valores = stringify(m.valores),
    caratula_pdf = ".build/aux/caratula_" .. VERSION .. ".pdf",
    laminas_png = stringify(m.laminas_png),
    c = m.controles or {},
  }
end

-- ── 1. Versión ──────────────────────────────────────────────────────────

local function aplicar_version(blocks)
  return blocks:walk({
    Div = function(d)
      for _, v in ipairs({ "e2", "e3" }) do
        if d.classes:includes("solo-" .. v) then
          if v == VERSION then return d.content end
          return {}
        end
      end
    end,
  })
end

-- ── 2. Valores ──────────────────────────────────────────────────────────

local function buscar(t, ruta)
  local x = t
  for parte in ruta:gmatch("[^%.]+") do
    if type(x) ~= "table" then return nil end
    local n = tonumber(parte)
    if n and x[n] ~= nil then x = x[n] else x = x[parte] end
    if x == nil then return nil end
  end
  return x
end

local function formatear(valor, literal)
  if type(valor) == "number" then
    local dec = literal:match(",(%d+)$")
    local d = dec and #dec or 0
    local s = string.format("%." .. d .. "f", valor + 0.0)
    if s:match("^%-0[%.0]*$") then s = s:sub(2) end
    return (s:gsub("%.", ","))
  end
  return tostring(valor)
end

local function aplicar_valores(blocks, valores, problemas, conteo)
  return blocks:walk({
    Span = function(sp)
      if not sp.classes:includes("v") then return nil end
      local k = sp.attributes.k
      local literal = stringify(sp.content)
      local valor = k and buscar(valores, k)
      conteo.n = conteo.n + 1
      if valor == nil then
        table.insert(problemas, "valor sin clave o clave inexistente: [" .. literal .. "] k=" .. tostring(k))
      else
        local esperado = formatear(valor, literal)
        if esperado ~= literal then
          table.insert(problemas, string.format("valor desactualizado: %s escrito «%s», la fuente da «%s»", k, literal, esperado))
        end
      end
      return sp.content
    end,
  })
end

-- ── Tablas: «: Epígrafe {#tbl:x}» -> id; @tbl:x -> «tabla N» ────────────
-- Pandoc no toma el {#tbl:x} del epígrafe: queda como texto al final. Se
-- extrae, se numeran las tablas en orden (todas llevan epígrafe, igual que
-- en LaTeX, así que el número coincide con el de longtable) y las citas se
-- escriben con el número, en PDF y en Word.

local function tablas_numeradas(blocks, problemas)
  local numeros, n = {}, 0
  blocks = blocks:walk({
    Table = function(t)
      n = n + 1
      local cap = t.caption.long[1]
      local ult = cap and cap.content[#cap.content]
      local id = ult and ult.t == "Str" and ult.text:match("^{#(tbl:[%w_%-]+)}$")
      if not id then
        table.insert(problemas, "tabla " .. n .. " sin epígrafe con {#tbl:...}")
        return nil
      end
      cap.content:remove(#cap.content)
      while #cap.content > 0 and cap.content[#cap.content].t == "Space" do cap.content:remove(#cap.content) end
      if numeros[id] then table.insert(problemas, "identificador de tabla repetido: " .. id) end
      numeros[id] = n
      t.identifier = id
      return t
    end,
  })
  blocks = blocks:walk({
    Cite = function(ci)
      local nums, mayus = {}, false
      for k, c in ipairs(ci.citations) do
        if not c.id:match("^[Tt]bl:") then return nil end
        if k == 1 then mayus = c.id:match("^T") ~= nil end
        local id = "tbl:" .. c.id:sub(5)
        if not numeros[id] then
          table.insert(problemas, "referencia a una tabla inexistente: @" .. c.id)
          return nil
        end
        table.insert(nums, tostring(numeros[id]))
      end
      local nombre = (#nums > 1 and "tablas" or "tabla")
      if mayus then nombre = nombre:gsub("^t", "T") end
      local lista_n = #nums == 1 and nums[1] or (table.concat(nums, ", ", 1, #nums - 1) .. " y\u{00A0}" .. nums[#nums])
      return pandoc.Str(nombre .. "\u{00A0}" .. lista_n)
    end,
  })
  return blocks, n
end

-- ── 3. Controles de contenido ──────────────────────────────────────────

-- Secciones de nivel 2 del .md: nombre sin numeración -> bloques
local function secciones(blocks)
  local s, orden, actual = {}, {}, nil
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.level == 2 then
      local nombre = stringify(b.content):gsub("^[%dA-Z]+%.%s*", ""):gsub("^Anexo%s+%u%.%s*", "Anexo: ")
      actual = { nombre = nombre, blocks = pandoc.List() }
      s[plano(nombre)] = actual
      table.insert(orden, actual)
    elseif b.t == "Header" and b.level == 1 then
      actual = nil
    elseif actual then
      actual.blocks:insert(b)
    end
  end
  return s, orden
end

local function parrafos(blocks)
  local n, total = 0, 0
  for _, b in ipairs(blocks) do
    if b.t == "Para" then
      n = n + 1
      total = total + palabras(stringify(b))
    end
  end
  return n, total
end

local function urls_de(elem)
  local u = {}
  pandoc.walk_block(pandoc.Div(elem), {
    Link = function(l) table.insert(u, l.target) end,
    Str = function(s) for x in s.text:gmatch("https?://[^%s<>]+") do table.insert(u, x) end end,
  })
  local limpio = {}
  for _, x in ipairs(u) do
    x = x:gsub("[%.,;%)]+$", ""):gsub("/$", "")
    limpio[x] = true
  end
  return limpio
end

local function items_div(blocks, clase)
  local items = {}
  for _, b in ipairs(blocks) do
    if b.t == "Div" and b.classes:includes(clase) then
      for _, bl in ipairs(b.content) do
        if bl.t == "BulletList" then
          for _, it in ipairs(bl.content) do table.insert(items, it) end
        end
      end
    end
  end
  return items
end

-- ¿Aparece el término como palabra entera? (si empieza o termina en letra,
-- el carácter vecino no puede ser letra: «carro» no encuentra «carrete»)
local function aparece(s, p)
  local function letra(c) return c ~= "" and c:match("[%w\128-\255_]") ~= nil end
  local ini = 1
  while true do
    local i, j = s:find(p, ini, true)
    if not i then return false end
    local ok_izq = not letra(p:sub(1, 1)) or not letra(s:sub(i - 1, i - 1))
    local ok_der = not letra(p:sub(-1)) or not letra(s:sub(j + 1, j + 1))
    if ok_izq and ok_der then return true end
    ini = i + 1
  end
end

local function vocabulario(texto_doc, terminos, problemas)
  local s = plano(texto_doc)
  local hallados = {}
  for _, t in ipairs(terminos) do
    t = stringify(t)
    local encontrado
    if t:sub(1, 3) == "re:" then
      encontrado = s:find(t:sub(4)) ~= nil
    else
      encontrado = aparece(s, plano(t))
    end
    if encontrado then
      table.insert(hallados, t)
      table.insert(problemas, "vocabulario controlado fuera del párrafo de alternativas: «" .. t .. "»")
    end
  end
  return hallados
end

local function controlar(doc_blocks, d, problemas, informe, conteo_valores)
  local c = d.c
  local s, orden = secciones(doc_blocks)
  informe.version = VERSION
  informe.secciones = {}
  for _, x in ipairs(orden) do table.insert(informe.secciones, x.nombre) end

  local function no_vacia(nombre)
    local x = s[plano(nombre)]
    if not x then
      table.insert(problemas, "falta la sección obligatoria «" .. nombre .. "»")
      return nil
    end
    local hay = false
    for _, b in ipairs(x.blocks) do
      if stringify(b):match("%S") or b.t == "Figure" then hay = true end
    end
    if not hay then table.insert(problemas, "la sección «" .. nombre .. "» está vacía") end
    return x
  end

  for _, nombre in ipairs(lista(c.obligatorias)) do no_vacia(stringify(nombre)) end
  for _, nombre in ipairs(lista(c.solo_e3)) do
    nombre = stringify(nombre)
    if VERSION == "e3" then no_vacia(nombre)
    elseif s[plano(nombre)] then
      table.insert(problemas, "la sección «" .. nombre .. "» no corresponde a " .. VERSION)
    end
  end

  -- Láminas en la sección Planos
  local planos = s[plano("Planos")]
  local nlam = 0
  if planos then
    for _, b in ipairs(planos.blocks) do
      pandoc.walk_block(b, { Image = function(img) if img.classes:includes("lamina") then nlam = nlam + 1 end end })
    end
  end
  informe.laminas = nlam
  local esperadas = tonumber(stringify(c.laminas or "0")) or 0
  if nlam ~= esperadas then
    table.insert(problemas, string.format("Planos: %d láminas, se esperaban %d", nlam, esperadas))
  end

  -- Largos
  local function largo(nombre, conf)
    local x = s[plano(nombre)]
    if not x or not conf then return end
    local n, pal = parrafos(x.blocks)
    informe[plano(nombre)] = { parrafos = n, palabras = pal }
    local function num(k) return conf[k] and tonumber(stringify(conf[k])) end
    if num("max_palabras") and pal > num("max_palabras") then
      table.insert(problemas, string.format("%s: %d palabras (máximo %d)", nombre, pal, num("max_palabras")))
    end
    if num("min_palabras") and pal < num("min_palabras") then
      table.insert(problemas, string.format("%s: %d palabras (mínimo %d)", nombre, pal, num("min_palabras")))
    end
    if num("max_parrafos") and n > num("max_parrafos") then
      table.insert(problemas, string.format("%s: %d párrafos (máximo %d)", nombre, n, num("max_parrafos")))
    end
    if num("min_parrafos") and n < num("min_parrafos") then
      table.insert(problemas, string.format("%s: %d párrafos (mínimo %d)", nombre, n, num("min_parrafos")))
    end
  end
  largo("Introducción", c.introduccion)
  largo("Abstract", c.abstract)
  largo("Conclusión", c.conclusion)

  -- Vocabulario: todo el texto (con notas), menos el bloque de alternativas
  local partes = {}
  local sin_alt = doc_blocks:walk({ Div = function(dv) if dv.classes:includes("alternativas") then return {} end end })
  local nalt = 0
  doc_blocks:walk({ Div = function(dv) if dv.classes:includes("alternativas") then nalt = nalt + 1 end end })
  if nalt ~= 1 then table.insert(problemas, "tiene que haber exactamente un bloque `::: alternativas` (hay " .. nalt .. ")") end
  for _, b in ipairs(sin_alt) do
    table.insert(partes, stringify(b))
    pandoc.walk_block(b, { Note = function(n) table.insert(partes, stringify(n.content)) end,
                           Math = function(m) table.insert(partes, m.text) end })
  end
  informe.vocabulario = vocabulario(table.concat(partes, "\n"), lista(c.vocabulario), problemas)

  -- Notas al pie y bibliografía
  local notas, n_notas = {}, 0
  doc_blocks:walk({ Note = function(n)
    n_notas = n_notas + 1
    local u = urls_de(n.content)
    local alguna = false
    for x in pairs(u) do notas[x] = true; alguna = true end
    if not alguna then table.insert(problemas, "nota al pie sin URL ni DOI: «" .. stringify(n.content):sub(1, 60) .. "…»") end
  end })
  informe.notas = n_notas
  local bib, links = {}, {}
  local function recorrer(items, destino, nombre)
    local textos = {}
    for _, it in ipairs(items) do
      local u = urls_de(it)
      local alguna = false
      for x in pairs(u) do destino[x] = true; alguna = true end
      if not alguna then table.insert(problemas, nombre .. ": entrada sin URL ni DOI: «" .. stringify(it):sub(1, 60) .. "»") end
      table.insert(textos, plano(stringify(it)))
    end
    for i = 2, #textos do
      if textos[i] < textos[i - 1] then
        table.insert(problemas, nombre .. ": fuera de orden alfabético: «" .. textos[i]:sub(1, 40) .. "»")
      end
    end
    return #items
  end
  local bib_sec = s[plano("Bibliografía")]
  local links_sec = s[plano("Links de interés")]
  informe.bibliografia = recorrer(bib_sec and items_div(bib_sec.blocks, "bibliografia") or {}, bib, "Bibliografía")
  informe.links = recorrer(links_sec and items_div(links_sec.blocks, "links") or {}, links, "Links de interés")
  if informe.bibliografia == 0 then table.insert(problemas, "la Bibliografía no tiene entradas (`::: bibliografia` con una lista)") end
  for x in pairs(notas) do
    if not bib[x] and not links[x] then table.insert(problemas, "fuente citada al pie que no está en Bibliografía ni en Links: " .. x) end
  end
  for x in pairs(bib) do
    if not notas[x] then table.insert(problemas, "entrada de la Bibliografía que no se cita al pie: " .. x) end
  end

  -- Imágenes y figuras citadas
  local ids, citadas = {}, {}
  doc_blocks:walk({
    Figure = function(f) if f.identifier:match("^fig:") then ids[f.identifier] = true end end,
    Image = function(img)
      if not existe(img.src) then table.insert(problemas, "no existe la imagen " .. img.src) end
    end,
    Cite = function(ci)
      for _, x in ipairs(ci.citations) do
        if x.id:match("^[Ff]ig:") then citadas["fig:" .. x.id:sub(5)] = true end
      end
    end,
  })
  local nfig = 0
  for id in pairs(ids) do
    nfig = nfig + 1
    if not citadas[id] then table.insert(problemas, "figura que no se cita en el texto: " .. id) end
  end
  informe.figuras = nfig
  informe.valores_verificados = conteo_valores.n
end

-- ── 4. Armado ───────────────────────────────────────────────────────────

local function lamina_latex(img, n, caption)
  local cap = tex_inlines(caption)
  return raw(table.concat({
    "\\begin{landscape}",
    "\\thispagestyle{empty}",
    "\\centering",
    "\\includegraphics[width=\\linewidth,height=\\dimexpr\\textheight-3cm\\relax,keepaspectratio]{" .. img.src .. "}\\par",
    "\\vspace{2mm}{\\small Lámina " .. n .. ": " .. cap .. "\\par}",
    "\\vfill",
    "\\noindent\\makebox[\\linewidth][s]{\\small\\itshape\\tppie\\hfill\\upshape\\thepage}",
    "\\end{landscape}",
  }, "\n"))
end

local function lamina_docx(img, n, caption, d)
  local base = img.src:match("([^/]+)%.pdf$")
  local png = d.laminas_png .. "/" .. base .. ".png"
  if not existe(png) then error("tp-mecanica.lua: falta " .. png .. " (lo genera tp.mk)") end
  local out = {}
  table.insert(out, pandoc.Div({ pandoc.Para({ pandoc.Image({}, png, "", pandoc.Attr("", {}, { width = "25.2cm" })) }) },
    { ["custom-style"] = "Lamina" }))
  local cap = pandoc.List({ pandoc.Str("Lámina " .. n .. ": ") })
  cap:extend(caption)
  table.insert(out, pandoc.Div({ pandoc.Para(cap) }, { ["custom-style"] = "Pie de lamina" }))
  -- fin de la sección apaisada de esta lámina (docx_tp.py completa el sectPr)
  table.insert(out, raw('<w:p><w:pPr><w:sectPr w:rsidR="00A1A1A1"/></w:pPr></w:p>'))
  return out
end

-- Imagen de una lámina (figura sola con clase .lamina), o nil
local function lamina(b)
  if not b or b.t ~= "Figure" or #b.content ~= 1 or b.content[1].t ~= "Plain" then return nil end
  local img = b.content[1].content[1]
  if img and img.t == "Image" and img.classes:includes("lamina") then return img end
  return nil
end

local function armar(blocks, d)
  local salida = pandoc.List()
  local nlam, ntab = 0, 0
  local primera_lamina = true
  for i, b in ipairs(blocks) do
    local img = lamina(b)
    if b.t == "Header" then
      -- "# Título" del .md: se descarta (el título sale de pdf.yaml)
      if b.level > 1 then
        b.level = b.level - 1
        salida:insert(b)
      end
    elseif img then
      nlam = nlam + 1
      local caption = b.caption.long[1] and b.caption.long[1].content or img.caption
      if LATEX then
        if primera_lamina then salida:insert(raw("\\clearpage\\newgeometry{margin=1cm}")) end
        salida:insert(lamina_latex(img, nlam, caption))
        if not lamina(blocks[i + 1]) then salida:insert(raw("\\restoregeometry")) end
      else
        if primera_lamina then
          -- cierra la sección vertical anterior
          salida:insert(raw('<w:p><w:pPr><w:sectPr w:rsidR="00B2B2B2"/></w:pPr></w:p>'))
        end
        salida:extend(lamina_docx(img, nlam, caption, d))
      end
      primera_lamina = false
    elseif b.t == "Div" and (b.classes:includes("bibliografia") or b.classes:includes("links")) then
      for _, bl in ipairs(b.content) do
        if bl.t == "BulletList" then
          if LATEX then salida:insert(raw("\\begin{tpbiblio}")) end
          for _, it in ipairs(bl.content) do
            local inl = pandoc.List()
            for k, x in ipairs(it) do
              if k > 1 then inl:insert(pandoc.Space()) end
              inl:extend(x.content or {})
            end
            if LATEX then
              salida:insert(pandoc.Plain({ pandoc.RawInline("latex", "\\tpitem "), table.unpack(inl) }))
            else
              salida:insert(pandoc.Div({ pandoc.Para(inl) }, { ["custom-style"] = "Bibliografia" }))
            end
          end
          if LATEX then salida:insert(raw("\\end{tpbiblio}")) end
        else
          salida:insert(bl)
        end
      end
    elseif b.t == "Div" and b.classes:includes("alternativas") then
      salida:extend(b.content)
    elseif b.t == "Table" and DOCX then
      ntab = ntab + 1
      local largo = b.caption.long
      if largo[1] then
        largo[1].content:insert(1, pandoc.Str("Tabla\u{00A0}" .. ntab .. ": "))
      end
      salida:insert(b)
    else
      salida:insert(b)
    end
  end
  return salida
end

local function inicio(d)
  local b = pandoc.List()
  if LATEX then
    if not existe(d.caratula_pdf) then error("tp-mecanica.lua: falta " .. d.caratula_pdf .. " (lo genera tp.mk)") end
    b:insert(raw("\\renewcommand{\\tppie}{" .. tex(d.pie) .. "}"))
    b:insert(raw("\\includepdf[pages=1]{" .. d.caratula_pdf .. "}"))
    b:insert(raw("\\begin{center}{\\fontsize{16}{20}\\selectfont\\bfseries " .. tex(d.titulo) .. "\\par}\\end{center}"))
    b:insert(raw("\\vspace{4pt}\\tableofcontents\\clearpage"))
  else
    b:insert(pandoc.Div({ pandoc.Para({ pandoc.Str(d.titulo) }) }, { ["custom-style"] = "Titulo TP" }))
    b:insert(pandoc.Div({ pandoc.Para({ pandoc.Str("Índice") }) }, { ["custom-style"] = "Indice titulo" }))
    b:insert(raw('<w:p><w:r><w:t>[[INDICE]]</w:t></w:r></w:p>'))
    b:insert(raw('<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
  end
  return b
end

-- JSON mínimo para el informe de controles
local function a_json(x, sangria)
  sangria = sangria or ""
  local t = type(x)
  if t == "table" then
    if #x > 0 or next(x) == nil then
      local partes = {}
      for _, v in ipairs(x) do table.insert(partes, a_json(v, sangria .. "  ")) end
      return "[" .. table.concat(partes, ", ") .. "]"
    end
    local claves = {}
    for k in pairs(x) do table.insert(claves, k) end
    table.sort(claves)
    local partes = {}
    for _, k in ipairs(claves) do
      table.insert(partes, sangria .. "  " .. string.format("%q", k) .. ": " .. a_json(x[k], sangria .. "  "))
    end
    return "{\n" .. table.concat(partes, ",\n") .. "\n" .. sangria .. "}"
  elseif t == "string" then
    return '"' .. x:gsub('\\', '\\\\'):gsub('"', '\\"'):gsub("\n", " ") .. '"'
  else
    return tostring(x)
  end
end

function Pandoc(doc)
  local d = datos(doc.meta)
  local blocks = aplicar_version(doc.blocks)

  local problemas, informe, conteo = {}, {}, { n = 0 }
  local texto_valores = leer(d.valores)
  if not texto_valores then error("tp-mecanica.lua: no existe " .. d.valores .. " (lo genera tp.mk)") end
  blocks = aplicar_valores(blocks, pandoc.json.decode(texto_valores, false), problemas, conteo)
  local ntablas
  blocks, ntablas = tablas_numeradas(blocks, problemas)
  informe.tablas = ntablas
  controlar(blocks, d, problemas, informe, conteo)

  informe.formato = FORMAT
  informe.problemas = problemas
  os.execute("mkdir -p .build/aux")
  local f = io.open(".build/aux/controles_" .. SALIDA .. "." .. (LATEX and "pdf" or "docx") .. ".json", "w")
  if f then f:write(a_json(informe), "\n"); f:close() end
  if #problemas > 0 then
    error("\ntp-mecanica.lua — controles que no pasan (" .. VERSION .. "):\n  - " .. table.concat(problemas, "\n  - "))
  end
  io.stderr:write(string.format("controles de contenido %s: OK (%d valores, %d notas, %d láminas, %d figuras)\n",
    VERSION, conteo.n, informe.notas, informe.laminas, informe.figuras))

  local final = inicio(d)
  final:extend(armar(blocks, d))
  if DOCX then
    -- Word no corta las URL largas y el justificado estira los espacios del
    -- renglón: espacio de ancho cero (U+200B) después de / . - _ en el texto
    -- visible del enlace (el destino no cambia). En el PDF lo resuelve xurl.
    final = pandoc.Blocks(final):walk({
      Link = function(l)
        local s = stringify(l.content)
        if s:match("^https?://") then
          l.content = { pandoc.Str((s:gsub("([/%.%-_%%=&%?])", "%1\u{200B}"))) }
          return l
        end
      end,
    })
  end
  doc.blocks = final
  return doc
end
