# Seleção vibracional em C₂v

22/10/2026. Aula `q3-selecao-vibracional`, rascunho original para revisão de Jhuann. Pré-requisito: geometria, caracteres e separação de movimentos rígidos de `q3-deslocamentos-simetria`. O modelo classifica canais por simetria; não fornece frequências, derivadas físicas, intensidade ou espectro.

## Fontes consultadas

Miessler, Fischer e Tarr, *Química Inorgânica*, quinta edição brasileira, Pearson 2014: blocos IR em p.107/PDF122 e Raman em p.110/PDF125, lidos parcialmente por extração local. A extração ampla abrangeu pp.101–110, mas não é alegada leitura integral; espectros/exercícios intermediários não foram usados na nova aula. O critério de polarizabilidade é formulado explicitamente, sem confundi-lo com um valor de polarização. Nenhuma figura, exercício ou página privada foi distribuída.

[DePrince Lab, Florida State University — Vibrational Motion](https://www.chem.fsu.edu/~deprince/tutorials/jupyter_notebooks/vibration/vibration.html), consulta direta parcial em 22/10/2026, blocos do elemento de transição/regras de seleção: distinção dipolo/polarizabilidade e limites de uma condição apenas de simetria. Não se executou notebook, Psi4 ou cálculo eletrônico; não se reproduzem seus exemplos. Tentativa de abrir IUPAC Polarizability retornou 403 e não foi usada como fonte confirmada.

A construção de caracteres a partir de monômios, a enumeração classe/canal e os exemplos são próprios. As fontes não são apresentadas como resultados pessoais de Jhuann.

## Convenção e hipóteses

Geometria angular AB₂ adimensional da aula anterior: A=(0,0,0), Bₐ=(1,0,1), Bᵦ=(−1,0,1), plano xz, eixo C₂ em z. Ordem E,C₂z,σxz,σyz. Caracteres:

| Classe | Caracteres | Dipolo | Polarizabilidade simétrica |
|---|---|---|---|
| A₁ | (1,1,1,1) | z | xx, yy, zz |
| A₂ | (1,1,−1,−1) | nenhum | xy |
| B₁ | (1,−1,1,−1) | x | xz |
| B₂ | (1,−1,−1,1) | y | yz |

O algoritmo transforma vetores por sinais e deriva as funções de grau um/dois. Funções quadráticas representam a transformação de componentes de um tensor; não significam αxx=x² numericamente.

Fundamentais harmônicos desde o estado vibracional totalmente simétrico, com estado eletrônico fixo, canais dipolares ou polarizabilidade simétrica usual. Em C₂v, todas as classes são reais e 1D: condição necessária é que ΓQ⊗ΓO contenha A₁. A média dos quatro produtos de caracteres é zero ou um, multiplicidade de A₁, sem interpretação probabilística. Um canal permitido ainda requer elemento físico não nulo. Operador constante entre estados ortogonais é um contraexemplo simples, sem inserir números arbitrários de intensidade.

AB₂ angular já tem Γvib=2A₁+B₁: três modos com canais IR e Raman permitidos por simetria; isso não implica três bandas detectadas/resolvidas. Duas cópias de A₁ não impõem degenerescência e não determinam formas normais. A₂/B₂ podem ser selecionadas como testes de classe genéricos, mas não existem como modos deste exemplo. O caso linear anterior é restrito a um subgrupo: suas regras completas não são inferidas aqui. Não se aplica exclusão mútua sem grupo e hipóteses pertinentes.

## Verificação

Quatro testes Python: caracteres avaliando monômios diretamente em três pontos distintos, sem reutilizar a potência de sinais do cálculo; 36 produtos classe/canal, cancelamentos e fechamento de produtos; canais e contagem ligados à decomposição do AB₂ pelo construtor geométrico existente; contratos. Não é cálculo independente de dipolos, tensor de polarizabilidade ou espectro molecular.

`reference.json` enumera quatro classes × nove canais = 36 estados, comparados com JavaScript. Cada estado guarda os caracteres, produto, multiplicidade, permissão, canais e ocorrência no AB₂. A lista completa de possibilidades não comprova atividade experimental.

Tese visual: tabela de sinais e média de projeção em uma superfície editorial simples. Conteúdo: convenção → operador → produto → contraexemplos/limites → Python/exercícios. Classe muda os caracteres do modo; canal muda o operador; caracteres e projeção se atualizam juntos. Sinal numérico e texto acompanham as cores. Sem espectro fictício ou animação que sugira uma frequência medida.

Próxima entrega pessoal: calcular A₁ com x e z, testar A₂ com xy e explicar por que esse último não cria um modo no AB₂. Próximo desenvolvimento: dinâmica 3D com massas/forças explicitamente escolhidas e vínculo com simetria, após revisar a fonte. Intensidades, mecanismos completos e as 15 lacunas do mapa de Química III seguem pendentes.
