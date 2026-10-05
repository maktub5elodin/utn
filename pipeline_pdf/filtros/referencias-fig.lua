--[[
referencias-fig.lua — Referencias cruzadas a figuras, sintaxis de pandoc-crossref.

Reemplazo mínimo de pandoc-crossref (no instalado), solo para figuras:

  Definir:  ![Epígrafe](figuras/x.png){#fig:nombre}   (párrafo propio)
  Citar:    @fig:nombre   -> "figura 2"
            @Fig:nombre   -> "Figura 2"   (inicio de oración)
            [@fig:a; @fig:b] -> "figuras 1 y 3"

Pandoc ya convierte la figura con id en \begin{figure}...\label{fig:nombre};
este filtro convierte cada cita en "figura~\ref{fig:nombre}" y LaTeX pone el
número. Si se cambia el orden de las figuras, los números se actualizan solos.

Verificación: si una cita apunta a una etiqueta que no existe, o si una
etiqueta está repetida, la compilación se detiene con un error que lista
todos los casos (nunca sale un "??" silencioso en el PDF).
]]

local function es_ref_fig(id)
  return id:match("^[Ff]ig:") ~= nil
end

local function etiqueta(id)
  return "fig:" .. id:sub(5)  -- normaliza @Fig:x -> fig:x
end

local function texto_ref(ids, mayuscula)
  local nombre = (#ids > 1) and "figuras" or "figura"
  if mayuscula then nombre = nombre:gsub("^f", "F") end
  local refs = {}
  for _, id in ipairs(ids) do refs[#refs + 1] = "\\ref{" .. id .. "}" end
  local lista
  if #refs == 1 then
    lista = refs[1]
  else
    lista = table.concat(refs, ", ", 1, #refs - 1) .. " y~" .. refs[#refs]
  end
  return nombre .. "~" .. lista
end

function Pandoc(doc)
  -- 1) Etiquetas definidas (figuras con id fig:...)
  local definidas, problemas = {}, {}
  doc:walk({
    Figure = function(fig)
      local id = fig.identifier
      if es_ref_fig(id) then
        if definidas[id] then
          problemas[#problemas + 1] = "etiqueta repetida: " .. id
        end
        definidas[id] = true
      end
    end,
  })

  -- 2) Citas @fig:... -> texto + \ref
  doc = doc:walk({
    Cite = function(cita)
      local ids, mayuscula = {}, false
      for i, c in ipairs(cita.citations) do
        if not es_ref_fig(c.id) then return nil end  -- cita bibliográfica: no tocar
        if i == 1 then mayuscula = c.id:match("^F") ~= nil end
        local id = etiqueta(c.id)
        if not definidas[id] then
          problemas[#problemas + 1] = "referencia a etiqueta inexistente: @" .. c.id
        end
        ids[#ids + 1] = id
      end
      return pandoc.RawInline("latex", texto_ref(ids, mayuscula))
    end,
  })

  if #problemas > 0 then
    error("referencias-fig.lua:\n  - " .. table.concat(problemas, "\n  - "))
  end
  return doc
end
