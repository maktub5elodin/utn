--[[
lab-fisica.lua — Informe de laboratorio de Física (U.D.B. Física, UTN FRBA).

Arma, a partir del bloque `laboratorio:` del pdf.yaml del documento:
  1. la carátula obligatoria de la U.D.B. (solo PDF: TikZ con las medidas del
     formulario oficial; en Word la arma docx_lab.py con tablas nativas);
  2. la página de título del informe (título, subtítulo, curso/turno/grupo,
     tabla de integrantes, docentes), igual en PDF y en Word;
  3. el anexo de datos firmados (fotos, una por página), si hay `anexo:`.

Y da al cuerpo la estética de los informes TP5/TP6:
  - tablas con encabezado azul y grilla gris (PDF; en Word, estilo de tabla);
  - `*Tabla N: …*` o `*Figura N: …*` (párrafo solo en cursiva) -> pie gris centrado;
  - cita `> …` -> recuadro de resultado con filete azul.

Los estilos de Word se definen en docx_lab.py (custom-style de cada Div).
]]

local LATEX = FORMAT:match("latex") ~= nil
local DOCX = FORMAT:match("docx") ~= nil
local AQUI = PANDOC_SCRIPT_FILE:match("^(.*)/[^/]*$") or "."

-- ── Utilidades ──────────────────────────────────────────────────────────

local function texto(v)
  if v == nil then return nil end
  local s = pandoc.utils.stringify(v)
  if s == "" then return nil end
  return s
end

local function lista(v)
  if v == nil then return {} end
  if pandoc.utils.type(v) == "List" then return v end
  return { v }
end

-- Texto plano -> LaTeX escapado (lo hace el escritor de pandoc)
local function tex(s)
  if s == nil or s == "" then return "" end
  local out = pandoc.write(pandoc.Pandoc({ pandoc.Plain({ pandoc.Str(s) }) }), "latex")
  return (out:gsub("%s+$", ""))
end

local function tex_bloques(blocks)
  local out = pandoc.write(pandoc.Pandoc(blocks), "latex")
  return (out:gsub("%s+$", ""))
end

local function raw(s) return pandoc.RawBlock("latex", s) end

-- Div con estilo: en Word, custom-style; en PDF, envoltorio LaTeX
local ESTILOS_TEX = {
  ["Titulo TP"]      = { "\\vspace*{4pt}{\\centering\\fontsize{22}{27}\\selectfont\\bfseries\\color{marinolab}", "\\par}" },
  ["Subtitulo TP"]   = { "{\\centering\\fontsize{16}{20}\\selectfont\\bfseries\\color{azullab}", "\\par}\\vspace{10pt}" },
  ["Datos TP"]       = { "{\\centering\\color{grislab}", "\\par}" },
  ["Integrantes TP"] = { "\\vspace{10pt}{\\centering\\large\\bfseries\\color{marinolab}", "\\par}\\vspace{2pt}" },
  ["Pie de tabla"]   = { "{\\centering\\footnotesize\\color{grislab}", "\\par}\\vspace{4pt}" },
  ["Resultado"]      = { "\\begin{resultadolab}", "\\end{resultadolab}" },
}

local function estilo(nombre, blocks)
  if LATEX then
    local e = ESTILOS_TEX[nombre]
    local out = { raw(e[1]) }
    for _, b in ipairs(blocks) do table.insert(out, b) end
    table.insert(out, raw(e[2]))
    return out
  end
  return { pandoc.Div(blocks, { ["custom-style"] = nombre }) }
end

local function parrafo(s) return pandoc.Para({ pandoc.Str(s) }) end

-- ── Datos del pdf.yaml ──────────────────────────────────────────────────

local function datos(meta)
  local m = meta.laboratorio
  if not m then error("lab-fisica.lua: falta el bloque `laboratorio:` en pdf.yaml") end
  local d = {
    materia  = texto(m.materia) or "Física I",
    catedra  = texto(m.catedra) or "U.D.B. Física",
    curso    = texto(m.curso),
    turno    = texto(m.turno),
    dias     = texto(m.dias),
    grupo    = texto(m.grupo),
    tp       = texto(m.tp),
    titulo   = texto(m.titulo),
    fecha    = texto(m.fecha),
    profesor = texto(m.profesor),
    jtp      = texto(m.jtp),
    atp      = {},
    integrantes = {},
    anexo    = {},
    anexo_titulo = texto(m["anexo-titulo"]) or "Anexo datos firmados",
  }
  for _, k in ipairs({ "curso", "turno", "dias", "tp", "titulo", "fecha", "profesor", "jtp" }) do
    if not d[k] then error("lab-fisica.lua: falta laboratorio." .. k .. " en pdf.yaml") end
  end
  for _, a in ipairs(lista(m.atp)) do table.insert(d.atp, texto(a)) end
  for _, i in ipairs(lista(m.integrantes)) do
    table.insert(d.integrantes, { apellido = texto(i.apellido), nombre = texto(i.nombre) })
  end
  if #d.integrantes == 0 then error("lab-fisica.lua: falta laboratorio.integrantes en pdf.yaml") end
  for _, f in ipairs(lista(m.anexo)) do table.insert(d.anexo, texto(f)) end
  -- Encabezado de página: "Física I — A1193 — Grupo N°5" (o sin grupo, si es individual)
  d.grupo_txt = d.grupo and ("Grupo N°" .. d.grupo) or "Individual"
  return d
end

-- ── Carátula U.D.B. (PDF) ───────────────────────────────────────────────
-- Medidas en cm desde la esquina superior izquierda de la hoja, tomadas del
-- formulario oficial (carátula .docx, A4, márgenes 2,5 cm) tal como lo
-- imprime Word. Si hay más de 6 integrantes, la tabla crece y el recuadro de
-- indicaciones se achica para que todo siga entrando en la hoja.

local function caratula_tex(d)
  local L, R, XT = 2.5, 18.48, 6.82        -- márgenes y comienzo de las tablas angostas
  local H, P = 0.68, 1.3465                -- alto de fila y paso entre filas
  local G = P - H                          -- separación entre tablas
  local t = {}
  local function add(s) table.insert(t, s) end
  local function caja(x1, y1, x2, y2) add(string.format("\\draw (%.3f,%.3f) rectangle (%.3f,%.3f);", x1, y1, x2, y2)) end
  local function linea(x1, y1, x2, y2) add(string.format("\\draw (%.3f,%.3f) -- (%.3f,%.3f);", x1, y1, x2, y2)) end
  local function texto_izq(x, y, ancho, s)
    add(string.format("\\node[anchor=west,inner sep=0pt] at (%.3f,%.3f) {\\labajustar{%.3fcm}{%s}};", x + 0.19, y, ancho - 0.38, s))
  end
  local function texto_centro(x, y, s)
    add(string.format("\\node[inner sep=0pt,align=center] at (%.3f,%.3f) {%s};", x, y, s))
  end

  add("\\begin{tikzpicture}[remember picture,overlay,x=1cm,y=-1cm,shift={(current page.north west)},line width=0.6pt]")
  add("\\caratulagrande")
  -- Recuadro gris «LABORATORIO DE FÍSICA» con el logo superpuesto a la izquierda
  add(string.format("\\fill[grisfondo] (%.3f,2.49) rectangle (%.3f,4.45);", XT, R))
  caja(XT, 2.49, R, 4.45)
  texto_centro((XT + R) / 2, 2.90, "LABORATORIO DE FÍSICA")
  add("\\fill[white] (5.84,2.49) rectangle (7.54,4.39);")
  add("\\node[anchor=north,inner sep=0pt] at (6.69,2.49) {\\logoutn{1.90cm}};")
  -- GRUPO N° | CURSO
  local y = 2.49 + 1.96 + G
  local xm = XT + 5.83
  caja(XT, y, R, y + H); linea(xm, y, xm, y + H)
  local curso_car = d.curso:gsub("^(%a)(%d)", "%1-%2")
  texto_izq(XT, y + H / 2, xm - XT, "GRUPO N°" .. tex(d.grupo or "—"))
  texto_izq(xm, y + H / 2, R - xm, "CURSO:" .. tex(curso_car))
  -- Franjas de una línea
  local filas = {
    "PROFESOR: " .. tex(d.profesor),
    "JTP: " .. tex(d.jtp),
    "ATP: " .. tex(table.concat(d.atp, " ; ")),
    "ASISTE LOS DÍAS: " .. tex(d.dias),
    "EN EL TURNO: " .. tex(d.turno),
    "TRABAJO PRÁCTICO N°:" .. tex(d.tp),
    "TÍTULO: " .. tex(d.titulo),
  }
  for _, s in ipairs(filas) do
    y = y + P
    caja(L, y, R, y + H)
    texto_izq(L, y + H / 2, R - L, s)
  end
  -- Integrantes presentes, en dos columnas (mínimo 3 filas, como el formulario)
  y = y + P
  local n = #d.integrantes
  local nf = math.max(3, math.ceil(n / 2))
  local xi = L + 8.0
  caja(L, y, R, y + H * (nf + 1))
  texto_izq(L, y + H / 2, R - L, "INTEGRANTES PRESENTES EL DÍA QUE SE REALIZÓ")
  add("\\caratulanombres")
  for f = 1, nf do
    local yf = y + H * f
    linea(L, yf, R, yf); linea(xi, yf, xi, yf + H)
    for c = 1, 2 do
      local i = d.integrantes[(f - 1) * 2 + c]
      if i then
        local x0, x1 = (c == 1) and L or xi, (c == 1) and xi or R
        texto_centro((x0 + x1) / 2, yf + H / 2,
          string.format("\\labajustar{%.3fcm}{%s}", x1 - x0 - 0.38, tex(i.nombre .. " " .. i.apellido)))
      end
    end
  end
  -- Fechas y firmas
  y = y + H * (nf + 1) + G
  local c1, c2 = L + 5.34, L + 10.64
  local alto_fechas = 1.28 + 3 * 0.64
  caja(L, y, R, y + alto_fechas); linea(c1, y, c1, y + alto_fechas); linea(c2, y, c2, y + alto_fechas)
  add("\\caratulachica")
  texto_centro((c1 + c2) / 2, y + 0.64, "FECHAS")
  texto_centro((c2 + R) / 2, y + 0.64, "FIRMA Y ACLARACIÓN\\\\DEL DOCENTE")
  local etiquetas = { "REALIZADO EL", "CORREGIDO", "APROBADO" }
  for k, e in ipairs(etiquetas) do
    local yf = y + 1.28 + 0.64 * (k - 1)
    linea(L, yf, R, yf)
    texto_izq(L, yf + 0.32, c1 - L, e)
  end
  add(string.format("\\node[inner sep=0pt] at (%.3f,%.3f) {\\mdseries %s};", (c1 + c2) / 2, y + 1.28 + 0.32, tex(d.fecha)))
  -- Indicaciones para las correcciones: hasta el margen inferior
  y = y + alto_fechas + G
  local fondo = math.max(27.53, y + 1.5)
  caja(L, y, R, fondo)
  add(string.format("\\node[anchor=north west,inner sep=0pt] at (%.3f,%.3f) {\\underline{INDICACIONES PARA LAS CORRECCIONES:}};", L + 0.19, y + 0.12))
  add("\\end{tikzpicture}")
  return table.concat(t, "\n")
end

-- ── Página de título del informe (PDF y Word) ───────────────────────────

local function tabla_integrantes(d)
  local filas = {}
  for _, i in ipairs(d.integrantes) do
    table.insert(filas, { { pandoc.Plain({ pandoc.Str(i.apellido) }) }, { pandoc.Plain({ pandoc.Str(i.nombre) }) } })
  end
  local t = pandoc.utils.from_simple_table(pandoc.SimpleTable(
    {}, { pandoc.AlignCenter, pandoc.AlignCenter }, { 0.24, 0.24 },
    { { pandoc.Plain({ pandoc.Str("Apellido") }) }, { pandoc.Plain({ pandoc.Str("Nombre") }) } },
    filas))
  t.attr = pandoc.Attr("", { "integrantes" })
  return t
end

local function etiqueta(rotulo, valor)
  return pandoc.Para({ pandoc.Strong({ pandoc.Str(rotulo) }), pandoc.Space(), pandoc.Str(valor) })
end

local function bloque_titulo(d)
  local b = {}
  local function mas(lst) for _, x in ipairs(lst) do table.insert(b, x) end end
  mas(estilo("Titulo TP", { parrafo("Trabajo Práctico N°" .. d.tp) }))
  mas(estilo("Subtitulo TP", { parrafo(d.titulo) }))
  local linea_curso = "Curso: " .. d.curso .. "  |  Turno: " .. d.turno .. "  |  " .. d.grupo_txt
  mas(estilo("Datos TP", { parrafo(d.materia .. " — " .. d.catedra) }))
  mas(estilo("Datos TP", { parrafo(linea_curso) }))
  mas(estilo("Integrantes TP", { parrafo(#d.integrantes > 1 and "Integrantes" or "Integrante") }))
  table.insert(b, tabla_integrantes(d))
  if LATEX then
    table.insert(b, raw("\\vspace{6pt}"))
  else
    table.insert(b, pandoc.RawBlock("openxml", '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr></w:p>'))
  end
  table.insert(b, etiqueta("Profesor/a de la materia:", d.profesor))
  table.insert(b, etiqueta("Jefe de Trabajos Prácticos (JTP):", d.jtp))
  if #d.atp > 0 then
    table.insert(b, etiqueta("Asistentes de Trabajos Prácticos (ATP):", table.concat(d.atp, " — ")))
  end
  return b
end

-- ── Tablas (PDF): encabezado azul, grilla gris, centradas ───────────────

local function celda_tex(cell)
  local blocks = cell.contents
  if #blocks == 1 and (blocks[1].t == "Plain" or blocks[1].t == "Para") then
    return tex_bloques({ pandoc.Plain(blocks[1].content) })
  end
  return tex_bloques(blocks)
end

local function tabla_tex(tbl)
  local ncol = #tbl.colspecs
  local cols = {}
  for _, cs in ipairs(tbl.colspecs) do
    local al, w = cs[1], cs[2]
    local alin = (al == "AlignLeft" and "\\raggedright") or (al == "AlignRight" and "\\raggedleft") or "\\centering"
    if type(w) == "number" and w > 0 then
      table.insert(cols, string.format(">{%s\\arraybackslash}p{\\dimexpr %.4f\\dimexpr\\linewidth-%d\\arrayrulewidth\\relax-2\\tabcolsep\\relax}", alin, w, ncol + 1))
    else
      table.insert(cols, (al == "AlignLeft" and "l") or (al == "AlignRight" and "r") or "c")
    end
  end
  local function fila(row, cabecera)
    local celdas = {}
    for _, c in ipairs(row.cells) do
      local s = celda_tex(c)
      if cabecera then s = "\\textcolor{white}{\\bfseries " .. s .. "}" end
      table.insert(celdas, s)
    end
    while #celdas < ncol do table.insert(celdas, "") end
    return (cabecera and "\\rowcolor{azullab} " or "") .. table.concat(celdas, " & ") .. " \\\\ \\hline"
  end
  local cab = {}
  for _, r in ipairs(tbl.head.rows) do table.insert(cab, fila(r, true)) end
  local cuerpo = {}
  for _, body in ipairs(tbl.bodies) do
    for _, r in ipairs(body.body) do table.insert(cuerpo, fila(r, false)) end
  end
  local t = { "{\\tablalab", "\\begin{longtable}{|" .. table.concat(cols, "|") .. "|}", "\\hline" }
  if #cab > 0 then
    table.insert(t, table.concat(cab, "\n")); table.insert(t, "\\endfirsthead")
    table.insert(t, "\\hline"); table.insert(t, table.concat(cab, "\n")); table.insert(t, "\\endhead")
  end
  table.insert(t, table.concat(cuerpo, "\n"))
  table.insert(t, "\\end{longtable}}")
  return raw(table.concat(t, "\n"))
end

-- ── Cuerpo ──────────────────────────────────────────────────────────────

local function es_pie(b)
  if b.t ~= "Para" or #b.content ~= 1 or b.content[1].t ~= "Emph" then return false end
  local s = pandoc.utils.stringify(b.content[1])
  return s:match("^Tabla%s") or s:match("^Figura%s")
end

local cuerpo = {
  -- "# Título" del .md: se descarta (el título sale de pdf.yaml);
  -- "## 1. Introducción" -> nivel 1 (\\section), "###" -> 2, "####" -> 3.
  Header = function(h)
    if h.level == 1 then return {} end
    h.level = h.level - 1
    return h
  end,
  Table = function(t)
    if LATEX then return tabla_tex(t) end
  end,
  BlockQuote = function(q)
    return estilo("Resultado", q.content)
  end,
  Para = function(p)
    if es_pie(p) then
      return estilo("Pie de tabla", { pandoc.Para(p.content[1].content) })
    end
  end,
}

local function anexo(d)
  local b = {}
  if #d.anexo == 0 then return b end
  table.insert(b, pandoc.Header(1, { pandoc.Str(d.anexo_titulo) }))
  for _, f in ipairs(d.anexo) do
    if LATEX then
      table.insert(b, raw("\\clearpage\\thispagestyle{empty}\\begin{center}\\vspace*{\\fill}"
        .. "\\includegraphics[width=\\textwidth,height=0.95\\textheight,keepaspectratio]{" .. f .. "}"
        .. "\\vspace*{\\fill}\\end{center}"))
    else
      table.insert(b, pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
      table.insert(b, pandoc.Para({ pandoc.Image({}, f, "", pandoc.Attr("", {}, { width = "16cm" })) }))
    end
  end
  return b
end

function Pandoc(doc)
  local d = datos(doc.meta)
  local blocks = doc.blocks:walk(cuerpo)
  local inicio = {}
  if LATEX then
    local f = io.open(AQUI .. "/logo_utn.tex", "r")
    local logo = f:read("a"); f:close()
    table.insert(inicio, raw(logo))
    table.insert(inicio, raw(string.format(
      "\\fancyhead[L]{\\footnotesize\\textcolor{azullab}{\\bfseries %s}\\quad\\textcolor{grislab}{|}\\quad\\textcolor{grislab}{%s}}",
      tex("Trabajo Práctico N°" .. d.tp .. " — " .. d.titulo),
      tex(d.materia .. " — " .. d.curso .. " — " .. d.grupo_txt))))
    table.insert(inicio, raw("\\thispagestyle{empty}\\null\n" .. caratula_tex(d) .. "\n\\clearpage\\setcounter{page}{1}"))
  end
  for _, b in ipairs(bloque_titulo(d)) do
    if b.t == "Table" and LATEX then b = tabla_tex(b) end
    table.insert(inicio, b)
  end
  if LATEX then table.insert(inicio, raw("\\vspace{6pt}")) end
  local final = {}
  for _, b in ipairs(inicio) do table.insert(final, b) end
  for _, b in ipairs(blocks) do table.insert(final, b) end
  for _, b in ipairs(anexo(d)) do table.insert(final, b) end
  doc.blocks = final
  return doc
end
