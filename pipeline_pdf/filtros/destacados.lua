--[[
destacados.lua — Citas marcadas como alerta de GitHub → recuadros de color en el PDF.

En el .md se usa la sintaxis de alerta de GitHub, que allá ya se ve en color:

  > [!CAUTION]                                  (rojo: un error)
  > **Mi error:** no arribé a $2y^2 - 12y + 52$.

  > [!TIP]                                      (verde: una respuesta correcta)
  > **Respuesta:** $Q_1 = (5;\,3)$ y $Q_2 = (-5;\,3)$.

En LaTeX la cita pasa al tcolorbox correspondiente (entornos "destacadoerror" y
"destacadocorrecto", definidos en base.yaml). En Word se quita el marcador y
queda como cita común. Las citas sin marcador (ej. enunciados) no se tocan.
]]

local ENTORNOS = {
  ["[!CAUTION]"] = "destacadoerror",
  ["[!TIP]"] = "destacadocorrecto",
}

-- Devuelve el entorno y el contenido de la cita sin el marcador, o nil si no lo tiene.
local function sin_marcador(cita)
  local primero = cita.content[1]
  if not primero or primero.t ~= "Para" then return nil end
  local ins = primero.content
  local entorno = ins[1] and ins[1].t == "Str" and ENTORNOS[ins[1].text]
  if not entorno then return nil end
  ins:remove(1)
  while ins[1] and (ins[1].t == "SoftBreak" or ins[1].t == "LineBreak" or ins[1].t == "Space") do
    ins:remove(1)
  end
  local bloques = cita.content
  if #ins == 0 then bloques:remove(1) end
  return entorno, bloques
end

function BlockQuote(cita)
  local entorno, bloques = sin_marcador(cita)
  if not entorno then return nil end
  if FORMAT:match("latex") then
    local salida = { pandoc.RawBlock("latex", "\\begin{" .. entorno .. "}") }
    for _, b in ipairs(bloques) do salida[#salida + 1] = b end
    salida[#salida + 1] = pandoc.RawBlock("latex", "\\end{" .. entorno .. "}")
    return salida
  end
  return pandoc.BlockQuote(bloques)
end
