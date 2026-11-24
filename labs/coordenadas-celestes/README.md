# Esfera e transformação local: primeiro recorte AGA0106

Apoio próprio, não conteúdo comprovado da turma de 2022. Histórico sem aprovação (RN) preservado no mapa. Página principal de Júpiter reconferida em 22/10/2026 continua com ativação futura em 01/01/2027; espelho de 2023 ainda indisponível diretamente. Dois grupos antes sem material próprio passam apenas de lacuna a parcial, totalizando três parciais/sete lacunas.

Convenções: latitude φ positiva ao norte, declinação δ ao norte do equador celeste, ângulo horário H crescente para oeste. Código usa H entre −180° e 180°, em graus; unidade angular 1h=15°. Azimute de norte para leste: N=0°, L=90°, S=180°, O=270°. Altura h a partir do horizonte, positiva acima. Direção não fornece distância ou visibilidade real. Sem converter data civil/UTC/fuso/longitude para TSL.

Derivação própria por mudança de base: a=cosδ cosH, b=−cosδ sinH, c=sinδ. Projeções locais E=b, N=−sinφ a+cosφ c, U=cosφ a+sinφ c. Norma preservada; sin h=U. Recuperação h=atan2(U,hypot(E,N)), A=atan2(E,N) reduzido a 0°–360°. Para φ=−30°, δ=0°, H=0°: E=0, N=1/2, U=√3/2, h=60°, A=0°. H=−90° dá horizonte leste; +90° oeste; 180° dá h=−60°, A=180°.

Em φ=δ=−30° e H=0°, zênite e A sem valor único. O limiar numérico hypot(E,N)≤1e−12 retorna None também para pontos extremamente próximos da singularidade; não é definição geométrica exata ou precisão de instrumento. Polos terrestres φ=±90° excluídos por exigir convenção adicional de direção norte. O laboratório recebe int/float finitos, sem bool; demais faixas explícitas no código.

Na raiz do site:

    python3 -m labs.coordenadas-celestes.horizontal
    python3 -m unittest discover -s labs/coordenadas-celestes -t .

Cinco testes: meridiano/cardinais, norma e mudança inversa em 175 configurações, zênite/nadir e limiar, polos celestes/simetria de H e entradas inválidas. Sem Astropy, efemérides ou dados observacionais. Não aplica refração, precessão/nutação, aberração, paralaxe, movimentos próprios ou catálogo. Não equivale a transformação ICRS observacional.

Fontes consultadas parcialmente em 22/10/2026:

- [USP — AGA0106, ativação 2027](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=AGA0106), estrutura atual e bibliografia, sem atribuir à turma de 2022.
- [Fiona Vincent — notas de St Andrews de 1998, cópia didática na UFSC](https://minerva.ufsc.br/~kanaan/astro1/aula-posicao/index.html), índice e [capítulo 4](https://minerva.ufsc.br/~kanaan/astro1/aula-posicao/chapter4.htm), declinação, H e unidade angular. Texto do capítulo 7 identifica triângulo, mas imagens de equações não foram recuperadas; não se afirma leitura delas. Descrições meridianas do hemisfério norte não foram generalizadas ao sul.
- [Astropy AltAz](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html), convenção N=0°/L=90° e distinção de refração. Somente documentação; sem instalação ou comparação computacional.

Apostila pública 2025 de Gastão Lima Neto foi localizada nominalmente, mas a leitura do PDF falhou; não é apresentada como fonte consultada de conteúdo. Bibliografia nominal do mapa segue não identificada no acervo; nenhuma cópia privada ou pública foi redistribuída. Notas, figura, código e dez exercícios originais, assistidos por IA para revisão pessoal. Primeira aula própria com doze seções; não certifica domínio ou experiência observacional. Próxima revisão: reconstruir as projeções e explicar a diferença entre H crescente para oeste e A crescente para leste. Próximo aprofundamento possível: tempo sideral e conversão de unidades angulares, com fontes e escalas explícitas.

Verificação: cinco testes novos e 13 de catálogo aprovados; 548 estruturas MathML e verificações de foco/rolagem de fórmulas conferidas. No navegador em 390 px, figura legível, questão de H positivo rejeitou azimute 90° e aceitou 270°. Navegação da página do curso à aula confirmada; status RN e limitação da versão futura visíveis. Largura contida no viewport e nenhum erro de console observado. Prévia: coordenadas-celestes-mobile.jpg. Não houve validação por Astropy, observação real ou revalidação global de painéis. Catálogo: 502 aulas/3188 exercícios; mapas: 367 grupos parciais/180 lacunas. Saldo semanal após bloco: 91%; parada em 65%.
