--[[
png-a-pdf.lua — Vista previa en PNG en el .md, vectorial en el PDF.

El .md apunta a figuras/*.png para que VS Code y GitHub puedan mostrarlas.
Al compilar a LaTeX/PDF, este filtro cambia cada figuras/X.png por
figuras/X.pdf, de modo que el documento final usa siempre el vectorial.

Si el .pdf correspondiente no existe, la compilación se detiene (en lugar de
caer silenciosamente al PNG).
]]

local function existe(ruta)
  local f = io.open(ruta, "r")
  if f then f:close() return true end
  return false
end

function Image(img)
  if not FORMAT:match("latex") then return nil end
  local base = img.src:match("^(figuras/.+)%.png$")
  if not base then return nil end
  local pdf = base .. ".pdf"
  if not existe(pdf) then
    error("png-a-pdf.lua: no existe " .. pdf .. " (¿falta correr figuras_tp7_ej1b.py?)")
  end
  img.src = pdf
  return img
end
