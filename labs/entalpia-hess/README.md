# Entalpia e lei de Hess — notas originais

16/10/2026. Rascunho assistido por IA para revisão pessoal.

## Defina o sistema antes de chamar energia de calor

Considere um sistema fechado, sem troca de matéria, com variações desprezíveis de energia cinética e potencial macroscópicas. Q é positivo quando entra no sistema; W é positivo quando o sistema realiza trabalho. A primeira lei é ΔU=Q−W. Calor descreve transferência, não uma substância armazenada.

## Entalpia acrescenta um termo de estado

Definimos H=U+pV, com p e V do sistema. H é uma função de estado, assim como U. O produto pV tem unidade de energia: Pa·m³=J. H não é calor em geral; processos com trabalho elétrico, variação de pressão ou fluxo de matéria exigem analisar o balanço apropriado.

## Quando o calor coincide com a variação de entalpia

Se o único trabalho é de expansão contra pressão externa constante p_ext, W=p_extΔV. Se os estados inicial e final estão em equilíbrio mecânico com essa mesma pressão, ΔH=ΔU+p_extΔV=Q. Essa igualdade pressupõe também sistema fechado e ausência das variações macroscópicas citadas. A pressão constante, sozinha, não elimina outros trabalhos. Em recipiente rígido, sem outro trabalho, Q_V=ΔU.

## O sinal se refere ao sistema e à transformação escrita

Uma transformação com ΔH<0 é exotérmica; nas condições anteriores transfere calor do sistema para o ambiente. Se ΔH>0, é endotérmica. Inverter os estados troca o sinal. Uma etapa endotérmica pode compor uma transformação global exotérmica; o sinal do total não determina o de cada etapa.

## A escrita da reação fixa a normalização

Para a reação escrita com coeficientes ν_i, positivos nos produtos e negativos nos reagentes, a variação padrão molar de reação é Δ_rH°=Σν_iΔ_fH_i°. As entalpias padrão de formação devem usar a mesma temperatura e as fases especificadas. O valor é por mol de avanço da reação tal como escrita. A quantidade total transformada importa: para Δ_rH constante, ΔH=ξΔ_rH.

## Estado padrão não fixa uma temperatura universal

O estado padrão especifica referências; a pressão padrão usual é 1 bar. É preciso informar T, frequentemente 298,15 K nas tabelas, mas o símbolo ° não significa necessariamente essa temperatura. A entalpia padrão de formação dos elementos em seus estados de referência é zero por convenção, não porque sua energia absoluta seja nula. Trocar fase ou temperatura troca o problema.

## A lei de Hess cancela estados intermediários

Se estados compatíveis A, B e C têm entalpias H_A, H_B e H_C, somar (H_B−H_A)+(H_C−H_B) deixa H_C−H_A. É a propriedade de função de estado. As reações também precisam somar corretamente: A→B mais B→C dá A→C. Cancelar símbolos sem respeitar espécie, fase e coeficientes produz outro balanço.

## Uma tabela sintética permite auditar as duas rotas

Adote três formas isoméricas hipotéticas de mesma composição atômica, em estados padrão a 298,15 K, com entalpias molares relativas h_A=0, h_B=20 e h_C=−30 kJ/mol. A→B dá +20; B→C dá −50; A→C dá −30 kJ/mol de reação. Dois mol de avanço totalizam −60 kJ. Os valores não são medições de substâncias reais; a referência zero de A não identifica A como elemento.

## Inverter, multiplicar e fechar um ciclo

C→A tem Δ_rH=+30 kJ/mol. Duplicar todos os coeficientes de A→C dobra a entalpia molar da reação escrita, enquanto converter a mesma quantidade física exige metade do avanço. No ciclo A→B→C→A, a soma é 20−50+30=0. Isso não cria energia utilizável de graça: retornar ao estado inicial zera a mudança da função de estado.

## Entalpia de formação combina equações balanceadas

Exemplo fictício: X₂+Y₂→2XY. Atribua Δ_fH°(XY)=−15 kJ/mol e zero aos elementos X₂ e Y₂ em seus estados de referência. A reação conserva dois átomos de cada elemento e dá 2(−15)−0−0=−30 kJ/mol de reação. Avanço de 2 mol consome 2 mol de X₂ e 2 mol de Y₂, forma 4 mol de XY e produz ΔH=−60 kJ. São dados sintéticos, sem associação a uma molécula real.

## O gráfico de estados não desenha uma barreira cinética

A linha azul conecta estados inicial, intermediário e final; a pontilhada conecta apenas as extremidades. O eixo horizontal é uma ordenação simbólica de estados, não tempo nem coordenada microscópica de reação. A altura de B não é uma energia de ativação. Variar B altera parcelas que se cancelam; variar a quantidade transforma o total em kJ, mas não as entalpias molares do gráfico.

## Uma conta correta ainda deixa perguntas abertas

ΔH negativo não prova espontaneidade nem rapidez: entropia, condições e energia de Gibbs também importam, e cinética exige taxas/mecanismos. A aula de equilíbrio de Química I já introduz Δ_rG=RT ln(Q/K), mas falta aprofundar sua derivação. Variação com temperatura, capacidades caloríficas e lei de Kirchhoff serão desenvolvidas depois. O laboratório verifica balanços; não mede calor nem prevê uma reação real.

## Resoluções

No exemplo sintético h_A=0, h_B=20, h_C=−30 kJ/mol, qual Δ_rH de B→C em kJ/mol de reação?

h_C−h_B=−30−20=−50 kJ/mol.

Qual Δ_rH de A→C nesse exemplo, em kJ/mol de reação?

20+(−50)=−30 kJ/mol, igual a h_C−h_A.

Para 2 mol de avanço de A→C, qual ΔH total em kJ?

2 mol×(−30 kJ/mol)=−60 kJ.

Qual Δ_rH de C→A, em kJ/mol de reação?

Inverter troca o sinal: −(−30)=+30 kJ/mol.

Com Δ_fH°(XY)=−15 e referências dos elementos iguais a zero, qual Δ_rH° de X₂+Y₂→2XY em kJ/mol de reação?

A soma assinada é 2(−15)−1(0)−1(0)=−30.

Se h_B passar a 40, mantendo h_A=0 e h_C=−30, qual soma molar de A→B e B→C, em kJ/mol de reação?

40+(−30−40)=40−70=−30.

Q_p=ΔH vale apenas por a pressão ser constante?

Com trabalho além de expansão, o calor não precisa coincidir com ΔH.

A altura de B no gráfico fornece a energia de ativação?

Não há estado de transição nem caminho microscópico definido.

Uma transformação exotérmica é necessariamente rápida e espontânea?

Entalpia não substitui Gibbs, condições de contorno ou cinética.

Na soma de entalpias, pode cancelar água líquida com vapor como se fossem o mesmo estado?

Espécie e fase fazem parte da definição do estado; omitir a vaporização altera a entalpia.

## Roteiro de estudo e verificação

Escreva uma solução própria invertendo e duplicando as reações. Confira conservação de espécies, fases e unidades antes de somar. No Python, teste o efeito de somar a mesma constante aos três níveis isoméricos: diferenças devem permanecer. Isso vale aqui porque cada reação conserva a soma dos coeficientes; deslocamentos arbitrários entre espécies não são permitidos em reações gerais. Em uma tabela de formação, mantenha referências elementares coerentes.

Execute `python3 -m unittest discover -p 'test_*.py'` na raiz para incluir os quatro testes do laboratório. O código aceita inteiros/Fraction para preservar exatidão, não números reais genéricos. A interface usa apenas as faixas finitas declaradas. Casos de referência cruzam Python e JavaScript; vetores de reação, balanço de átomos e invariâncias são verificados separadamente. Nenhuma execução pessoal de Jhuann é presumida.

## Fontes e pendências

Escopo: [USP CCM0124](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124), consulta 16/10/2026, programa de 2025 posterior à turma. Apoio conceitual: [Michigan State University, Thermochemistry](https://www2.chemistry.msu.edu/courses/cem152/Chap19-2026.pdf), páginas 2–16, consultadas diretamente em 16/10/2026. A fonte usa w para trabalho sobre o sistema; aqui W é trabalho realizado pelo sistema, portanto w=−W. Não foram reutilizados seus exemplos ou exercícios. A tentativa de abrir a definição de entalpia da IUPAC retornou 403; não é registrada como leitura integral.

Pendentes: calorimetria experimental, capacidades caloríficas, lei de Kirchhoff, reações gerais com múltiplas etapas e aprofundamento químico de Gibbs. Os exemplos de formação usam números fictícios; não são uma tabela de dados de substâncias reais.
