--[[
salto-pagina.lua — Salto de página en el PDF, invisible en el .md.

Un comentario en una línea propia (con línea en blanco antes y después)

  <!-- salto-pagina -->

se convierte en \clearpage al compilar a LaTeX y en un salto de página de
Word al compilar a .docx. En la vista previa del .md no se ve nada.
]]

function RawBlock(b)
  if b.format ~= "html" then return nil end
  if not b.text:match("^<!%-%-%s*salto%-pagina%s*%-%->$") then return nil end
  if FORMAT:match("latex") then
    return pandoc.RawBlock("latex", "\\clearpage")
  elseif FORMAT:match("docx") then
    return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end
end
