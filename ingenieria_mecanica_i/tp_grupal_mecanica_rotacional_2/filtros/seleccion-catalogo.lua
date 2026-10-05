--[[
seleccion-catalogo.lua — En el PDF, del catálogo solo la pieza seleccionada.

El .md trae la tabla completa del catálogo (Anexo A), con la fila elegida
marcada con "►" en la primera celda. Al compilar a LaTeX, toda tabla que tenga
una fila marcada así se reemplaza por una tabla vertical de dos columnas
(Magnitud | Valor) con los datos de esa fila sola. La versión vertical entra
en el ancho de la página; la fila de 11 columnas no.

Debe ir antes de tablas-cebra.lua en pdf.yaml (ese filtro convierte las tablas
en LaTeX crudo).
]]

local stringify = pandoc.utils.stringify

local function celdas(fila)
  local t = {}
  for _, c in ipairs(fila.cells) do t[#t + 1] = stringify(c.contents) end
  return t
end

-- Escapa "|" para no romper la tabla en formato pipe
local function limpio(s)
  return (s:gsub("►%s*", ""):gsub("|", "\\|"))
end

function Table(tbl)
  if not FORMAT:match("latex") then return nil end
  local elegida
  for _, cuerpo in ipairs(tbl.bodies) do
    for _, fila in ipairs(cuerpo.body) do
      local c = celdas(fila)
      if c[1] and c[1]:find("►", 1, true) then
        if elegida then error("seleccion-catalogo.lua: más de una fila marcada con ►") end
        elegida = c
      end
    end
  end
  if not elegida then return nil end

  local enc = celdas(tbl.head.rows[1])
  local md = { "| Magnitud | " .. limpio(elegida[1]) .. " |", "|---|---|" }
  for i = 2, #enc do
    md[#md + 1] = "| " .. limpio(enc[i]) .. " | " .. limpio(elegida[i] or "") .. " |"
  end
  return pandoc.read(table.concat(md, "\n"), "markdown").blocks
end
