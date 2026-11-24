# Laplaciano radial e casca esférica

Notas originais em rascunho, 28/10/2026. Referência pública consultada parcialmente: NIST DLMF §1.5(ii), Eqs.1.5.13,1.5.15,1.5.17 — https://dlmf.nist.gov/1.5#ii . Apoio para convenções polar/cilíndrica/esférica; derivação cartesiana, problema de contorno, números, figura e código próprios. Não se consultou novo livro privado neste bloco. Percurso complementar, não equivalência com disciplina ou domínio pessoal.

Execute da raiz: `python3 -m unittest discover -s labs/laplaciano-casca -t .` e `python3 labs/laplaciano-casca/radial.py`.

Potências inteiras de raio positivo usando Fraction. `shell3` só avalia f=2−2/r na casca 1≤r≤2, em coordenada adimensional. Não resolve uma EDP geral nem calcula distribuição na origem. Teste independente expande polinômios cartesianos por convolução (180 casos), além de potências harmônicas, contorno/fluxo e contratos. Valores exatos não certificam uma discretização, solução experimental ou regularidade global.

Revisão pessoal de20min: derive a soma dos termos cartesianos, obtenha as constantes na casca e explique por que o fluxo da fronteira interna usa normal oposta. Fonte singular, Green, geometrias não radiais, discretização e interpretação dimensional de campos reais permanecem pendentes.
