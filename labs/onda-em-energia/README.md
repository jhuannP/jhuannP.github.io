# Onda eletromagnética: orientação e energia

27/10/2026. Notas de aula originais assistidas por IA, aguardando revisão de Jhuann. Pré-requisitos: Maxwell, derivadas, produtos vetoriais e média sobre um período. Nenhuma certificação de domínio ou conclusão de Física III.

Modelo: onda plana harmônica linearmente polarizada no vácuo sem fontes, sem campos estáticos de fundo. E aponta no eixo x, B no eixo y, fase kz−ωt com propagação+z. Faraday e Ampère–Maxwell dão ω=ck e E₀=cB₀. Para a direção oposta a fase e o sinal relativo de B são ajustados juntos. Não basta trocar B de sinal mantendo a fase.

Poynting: S=E×B/μ₀. Os campos oscilam juntos; o fluxo não inverte quando ambos trocam de sinal, e vale zero nos nós. A densidade total é u=ε₀E² e S=cu na direção da onda. Com amplitude E₀, intensidade média I=ε₀cE₀²/2; com valor eficaz E_rms, I=ε₀cE_rms². Potência através de uma área plana é fluxo orientado I A cosγ; absorção requer outro modelo.

O exemplo original c=2,B=3,E=6 é preservado como normalização. Laboratório fixa ε=1,μ=1/4,c=2,E₀=6,k=1,ω=2. Fluxo máximo72, médio36; densidade máxima36, dividida em18 e18. São números normalizados, não medidas SI. Onda plana infinita não é feixe finito com energia total finita.

## Referências parcialmente consultadas

Nussenzveig, Curso de Física Básica vol.3, 2ª ed., exemplar autorizado: §12.3 pp.249–251/PDF250–252 (onda) e §12.5 pp.255–257/PDF256–258 (energia e Poynting), consulta textual parcial em27/10/2026. PDF contado a partir de1. OCR imperfeito: não adotar automaticamente símbolos/unidades ambíguos ou convenções misturadas em recortes; deduções e dimensões da aula conferidas separadamente. Sem nova inspeção visual ou leitura integral.

[OpenStax University Physics vol.2 §16.2](https://openstax.org/books/university-physics-volume-2/pages/16-2-plane-electromagnetic-waves), hipótese de onda sem fundo, transversalidade e relações dos campos; [§16.3](https://openstax.org/books/university-physics-volume-2/pages/16-3-energy-carried-by-electromagnetic-waves), energia, fluxo e média, consulta parcial em27/10/2026. Exemplos, figura, deduções, exercícios e código próprios; sem copiar exercícios, números ou figuras dos autores. Livro privado não distribuído. Júpiter não reaberto neste bloco; limitações de versão curricular preservadas.

## Laboratório e verificações

Execute `python3 labs/onda-em-energia/wave.py`. Avalia solução analítica em unidades normalizadas; não é simulador de emissão ou propagação com condições de contorno. Quatro testes:

- Orientação, ortogonalidade, igualdade das duas parcelas de energia e S_z=±cu em18 pontos/direções, mais o produto vetorial original.
- Médias sobre um período em12 combinações de posição, direção e resolução8/16/64: média de E zero, média de E²18 e fluxo médio orientado±36. Os pontos médios integram exatamente esses modos trigonométricos em aritmética ideal; o erro restante é de ponto flutuante.
- Diferenças centrais para as duas componentes não triviais de Maxwell e continuidade de energia em12 posições/tempos/direções, com passos0,1/0,05/0,025. Máximos absolutos amostrados entre os resíduos normalizados:1,3997868;0,3525845;0,0883116. Caem aproximadamente quatro vezes ao reduzir o passo pela metade. Não são cotas globais, erros da solução analítica ou tolerâncias em SI; as equações e suas escalas são diferentes, e o máximo serve apenas à conferência de refinamento deste recorte.
- Candidato com somente B invertido falha em Maxwell, enquanto o par coerente apresenta resíduo pequeno no ponto e passo escolhidos. Contratos de direção/passos também conferidos.

Próxima ação de20min: deduzir a direção da fase, a relação E₀=cB₀ e o fator1/2; explicar por que36 e72 são perguntas distintas. Meios materiais, dispersão, polarização geral, ondas estacionárias, radiação e revisão pessoal permanecem pendentes.
