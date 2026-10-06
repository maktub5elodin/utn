--[[
salto-pagina.lua — Salto de página en el PDF, invisible en el .md.

Un comentario en una línea propia (con línea en blanco antes y después)

  <!-- salto-pagina -->

se convierte en \clearpage al compilar a LaTeX. En la vista previa del .md
no se ve nada.
]]

function RawBlock(b)
  if not FORMAT:match("latex") or b.format ~= "html" then return nil end
  if b.text:match("^<!%-%-%s*salto%-pagina%s*%-%->$") then
    return pandoc.RawBlock("latex", "\\clearpage")
  end
end
