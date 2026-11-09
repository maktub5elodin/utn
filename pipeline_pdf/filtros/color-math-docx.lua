--[[
color-math-docx.lua — Fórmulas con \color en la salida Word.

El conversor de fórmulas de pandoc no entiende {\color{X} ...} y deja la fórmula
entera como LaTeX crudo. Este filtro quita el \color y conserva el contenido;
\boxed sí se convierte (recuadro nativo de Word), y docx_estilo.py lo pinta de
verde después.
]]

local MARCA = "{\\color{"

local function sin_color(t)
  while true do
    local i = t:find(MARCA, 1, true)
    if not i then return t end
    local fin_nombre = t:find("}", i + #MARCA, true)
    -- Busca la llave que cierra el grupo abierto en i.
    local j, prof = i + 1, 1
    while prof > 0 do
      local c = t:sub(j, j)
      if c == "\\" then j = j + 1
      elseif c == "{" then prof = prof + 1
      elseif c == "}" then prof = prof - 1 end
      j = j + 1
    end
    t = t:sub(1, i - 1) .. t:sub(fin_nombre + 1, j - 2) .. t:sub(j)
  end
end

function Math(m)
  if not FORMAT:match("docx") then return nil end
  m.text = sin_color(m.text)
  return m
end
