--[[
solo-md.lua — Contenido que se ve en el .md pero no llega al PDF.

1. Bloques marcados a mano. Todo lo que esté entre

     <!-- solo-md -->
     ...
     <!-- /solo-md -->

   (cada comentario en una línea propia, con línea en blanco antes y después;
   si no, pandoc lo junta con el párrafo vecino) se descarta al compilar a LaTeX.
   En la vista previa del .md los comentarios no se ven, así que el contenido
   se lee normalmente.

2. Diagramas ASCII. Los bloques de código del .md son los diagramas ASCII,
   que no van al PDF. Cada uno se reemplaza por un recuadro "Figura pendiente"
   hasta que exista la figura definitiva (PNG en el .md, PDF vectorial en el
   documento).

Si un marcador de apertura queda sin cerrar, la compilación se detiene.
]]

local function marcador(bloque)
  if bloque.t ~= "RawBlock" or bloque.format ~= "html" then return nil end
  local txt = bloque.text:match("^<!%-%-%s*(.-)%s*%-%->$")
  if txt == "solo-md" then return "abre" end
  if txt == "/solo-md" then return "cierra" end
  return nil
end

local PENDIENTE = [[
\begin{center}
\fbox{\parbox{0.85\linewidth}{\centering\itshape
Figura pendiente (en el .md figura como diagrama ASCII).}}
\end{center}]]

function Blocks(bloques)
  if not FORMAT:match("latex") then return nil end
  local salida, dentro = {}, false
  for _, b in ipairs(bloques) do
    local m = marcador(b)
    if m == "abre" then
      if dentro then error("solo-md.lua: <!-- solo-md --> anidado") end
      dentro = true
    elseif m == "cierra" then
      if not dentro then error("solo-md.lua: <!-- /solo-md --> sin apertura") end
      dentro = false
    elseif not dentro then
      if b.t == "CodeBlock" then
        salida[#salida + 1] = pandoc.RawBlock("latex", PENDIENTE)
      else
        salida[#salida + 1] = b
      end
    end
  end
  if dentro then error("solo-md.lua: <!-- solo-md --> sin cierre") end
  return salida
end
