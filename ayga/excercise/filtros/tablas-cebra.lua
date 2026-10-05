--[[
tablas-cebra.lua — Ajusta todas las tablas para el rayado de cebra.

El color de las filas lo pone \rowcolors (paquete colortbl, ver pdf.yaml).
Este filtro corrige dos cosas del LaTeX que pandoc genera para cada tabla:

1. Bordes: pandoc arma la longtable con @{} en los extremos (sin margen
   exterior), pero colortbl pinta cada celda con un sobrante de \tabcolsep
   hacia afuera, así que el gris se salía de las líneas horizontales. Se quita
   @{} y se recalculan los anchos p{...} para que la tabla siga midiendo
   exactamente \linewidth: (\linewidth - K\tabcolsep) pasa a (K+2).

2. Encabezado: queda siempre sin color (\hiderowcolors ... \showrowcolors),
   también cuando la tabla se parte y el encabezado se repite en otra página.

Se aplica a todas las tablas del documento; no hace falta marcar nada en el .md.
]]

local function ajustar(tex)
  local n
  -- 1) Sin @{} en los extremos de la especificación de columnas
  tex, n = tex:gsub("(\\begin{longtable}%[%]{)@{}", "%1", 1)
  if n ~= 1 then return nil end  -- formato inesperado: dejar la tabla como está
  tex = tex:gsub("@{}}\n", "}\n", 1)
  -- ... y anchos compensados por el margen exterior agregado
  tex = tex:gsub("%(\\linewidth %- (%d+)\\tabcolsep%)", function(k)
    return "(\\linewidth - " .. (tonumber(k) + 2) .. "\\tabcolsep)"
  end)
  -- 2) Encabezado sin color (en \endfirsthead y en \endhead)
  tex = tex:gsub("\\toprule\\noalign{}\n", "\\toprule\\noalign{}\n\\hiderowcolors\n")
  tex = tex:gsub("\\midrule\\noalign{}\n\\end(f?i?r?s?t?head)",
                 "\\showrowcolors\n\\midrule\\noalign{}\n\\end%1")
  return tex
end

function Table(tbl)
  if not FORMAT:match("latex") then return nil end
  local tex = ajustar(pandoc.write(pandoc.Pandoc({ tbl }), "latex"))
  if not tex then
    io.stderr:write("tablas-cebra.lua: tabla con formato inesperado, sin ajustar\n")
    return nil
  end
  return pandoc.RawBlock("latex", tex)
end
