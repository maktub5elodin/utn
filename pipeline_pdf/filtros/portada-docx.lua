--[[
portada-docx.lua — Subtítulo y fecha del pdf.yaml en la salida Word.

El pdf.yaml de cada documento define subtitle y date como variables de la
plantilla LaTeX. El .docx no usa esa plantilla: arma el encabezado con los
metadatos. Este filtro copia esas dos variables a los metadatos, así el
pdf.yaml sigue siendo el único lugar donde se escriben.
]]

function Meta(meta)
  if not FORMAT:match("docx") then return nil end
  local vars = PANDOC_WRITER_OPTIONS.variables or {}
  for _, clave in ipairs({ "subtitle", "date" }) do
    local v = vars[clave]
    if v and not meta[clave] then meta[clave] = tostring(v) end
  end
  return meta
end
