# Orbitais por simetria — sobreposição e autoproblema

Modelo original de um elétron com duas funções reais normalizadas equivalentes, geometria fixa. H tem diagonais α, fora da diagonal β; S tem diagonais1, fora da diagonal s, |s|<1. α,β estão numa unidade abstrata de energia, não são dados de H₂⁺. Sem integrais, densidade espacial ou energia molecular total.

`modes` retorna direções não normalizadas, energias e o quadrado do fator de normalização. `metric_inner` e `rayleigh` incluem termos cruzados. `shifted` implementa H′=H+C S. A API usa int/Fraction, rejeita bool/float e base dependente. O caso |s|=1 é excluído; nenhuma aproximação próxima da singularidade é feita em float.

## Fontes parcialmente consultadas —27/10/2026

Miessler, Fischer e Tarr, *Química Inorgânica*, 5ª edição brasileira, Pearson2014: §§5.1–5.1.1 pp.117–120/PDF132–135. P.118/PDF133 também inspecionada visualmente, inclusive a nota da simplificação dos coeficientes. A explicação própria mantém a sobreposição na normalização e nos denominadores; não atribui os números ou deduções ao livro. Sem leitura integral do capítulo ou reprodução da figura.

[MIT5.61 Fall2007, Lecture30, Molecular Orbitals II](https://www.ocw.mit.edu/courses/5-61-physical-chemistry-fall-2007/e1317ade387213639a8d2bf26103078a_lecture30.pdf), pp.2–3/PDF2–3: matrizes H e S e autoproblema generalizado, consulta parcial. [Programa CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214) reaberto: ativação15/07/2024; captura indicada de dois meses antes, sem comprovar versão ministrada. Item2 ganha cobertura parcial.

Uma fonte adicional do IITDelhi retornou502 e não foi tratada como texto consultado. A extração do exemplar Miessler retornou avisos de fontes/streams em outras partes; os recortes acima continham texto e p.118 foi visualmente conferida. PDFs e páginas privadas não são distribuídos.

## Verificação e revisão

Na raiz: `python3 -m unittest discover -s labs/orbitais-sobreposicao -t .`.

Testes: referências, resíduos Hc−ESc, determinante, normalização, ortogonalidade na métrica, decomposição do quociente de Rayleigh em pesos positivos, mudança de origem, fase da segunda função, empate/inversão de ordem e contratos. Não certificam molécula real ou domínio pessoal.

Revisão de20min: obter as duas normas, substituir as direções e derivar as energias; depois explicar o erro de substituir S porI. Permanecem integrais dependentes da distância, energia nuclear, grupos gerais, poliatômicas, ocupação multieletrônica e revisão pessoal.

Conferência em27/10/2026: cinco testes locais e14 do catálogo aprovados;808 estruturas MathML globais. Navegador390px: normalização rejeitou1/2 e aceitou5/12 pelo Enter, ordem energética aceita. Figura/fórmula inspecionadas, largura390px e console sem erros. Captura na raiz: `orbitais-sobreposicao-mobile.jpg`.
