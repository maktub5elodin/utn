-- Fórmulas de los títulos, legibles en el outline (marcadores) del PDF:
-- pandoc pone en el marcador el LaTeX crudo (\mathbb{R}^4); acá se cambia por
-- su equivalente Unicode (ℝ⁴). Solo en salida LaTeX.
local reemplazos = {
  {'\\mathbb{R}', 'ℝ'}, {' \\times ', ' × '}, {'%^4', '⁴'}, {'%^3', '³'},
  {'%^t', 'ᵗ'}, {'_2', '₂'},
}

function Header(h)
  if not FORMAT:match('latex') then return nil end
  return h:walk {
    Math = function(m)
      local s = m.text
      for _, r in ipairs(reemplazos) do
        s = s:gsub(r[1]:gsub('[%\\%{%}]', '%%%0'), r[2])
      end
      if s:match('[\\{}^_]') then
        error('marcadores.lua: fórmula sin equivalente Unicode: ' .. m.text)
      end
      -- pandoc arma \texorpdfstring{<LaTeX>}{<texto>} con todo el título y
      -- deja afuera del <texto> lo crudo: el Str queda solo en el marcador.
      return {
        pandoc.RawInline('latex', '\\texorpdfstring{$' .. m.text .. '$}{'),
        pandoc.Str(s),
        pandoc.RawInline('latex', '}'),
      }
    end
  }
end
