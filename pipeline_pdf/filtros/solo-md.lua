--[[
solo-md.lua — Contenido que se ve en el .md pero no llega al PDF.

1. Bloques marcados a mano. Todo lo que esté entre

     <!-- solo-md -->
     ...
     <!-- /solo-md -->

   (cada comentario en una línea propia, con línea en blanco antes y después;
   si no, pandoc lo junta con el párrafo vecino) se descarta al compilar a LaTeX
   o a Word.
   En la vista previa del .md los comentarios no se ven, así que el contenido
   se lee normalmente.

2. Bloques solo para el documento. El caso inverso: lo que va dentro de

     <!-- solo-pdf
     ...
     -->

   no se ve en la vista previa del .md (es un comentario) pero se lee como
   Markdown y entra al PDF y al Word. Sirve con un bloque solo-md al lado para
   mostrar dos versiones de un mismo paso (ej. una notación en el .md y otra en
   el PDF). El contenido no puede llevar "-->".

3. Diagramas ASCII. Los bloques de código del .md son los diagramas ASCII,
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

-- Contenido de un comentario <!-- solo-pdf ... -->, o nil si no lo es.
local function solo_pdf(bloque)
  if bloque.t ~= "RawBlock" or bloque.format ~= "html" then return nil end
  return bloque.text:match("^<!%-%-%s*solo%-pdf%s*\n(.-)%-%->%s*$")
end

local PENDIENTE = [[
\begin{center}
\fbox{\parbox{0.85\linewidth}{\centering\itshape
Figura pendiente (en el .md figura como diagrama ASCII).}}
\end{center}]]

-- En Word, el mismo aviso como párrafo centrado en cursiva.
local function pendiente()
  if FORMAT:match("latex") then return pandoc.RawBlock("latex", PENDIENTE) end
  return pandoc.Div(
    pandoc.Para({ pandoc.Emph({ pandoc.Str("[Figura pendiente: en el .md figura como diagrama ASCII.]") }) }),
    pandoc.Attr("", {}, { ["custom-style"] = "Figura pendiente" }))
end

function Blocks(bloques)
  if not (FORMAT:match("latex") or FORMAT:match("docx")) then return nil end
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
      local pdf = solo_pdf(b)
      if pdf then
        for _, sub in ipairs(pandoc.read(pdf, "markdown").blocks) do
          salida[#salida + 1] = sub
        end
      elseif b.t == "CodeBlock" then
        salida[#salida + 1] = pendiente()
      else
        salida[#salida + 1] = b
      end
    end
  end
  if dentro then error("solo-md.lua: <!-- solo-md --> sin cierre") end
  return salida
end
