# Potencial de par: energia e força — rascunho original

29/10/2026. Apoio de IA para revisão de Jhuann. Entradas fictícias,sem medição ou domínio pessoal certificado.

## Reprodução e contrato

Da raiz do protótipo:

```sh
python3 -B -m labs.potencial-par.pair
python3 -B -m unittest discover -s labs/potencial-par -t .
```

Biblioteca padrão,Fraction. r e sigma na mesma unidade de comprimento;epsilon energia por par. U nessa energia,F_r energia/comprimento,curvatura energia/comprimento². Entradas inteiras/Fraction positivas;bool,float e textos rejeitados. Sem detecção dimensional. minimum_bracket aceita1…128passos;work exige0<a<b e painéis pares2…512. Expressão12–6 sem corte,não é LAMMPS ou pacote de dinâmica molecular. Nenhum parâmetro real ajustado.

## Teoria e limites

### O contexto biológico exige mais de um tipo de interação

Retome derivadas, energia potencial e a aula de água. Interações eletrostáticas, dispersão e ligações de hidrogênio participam da organização molecular; a geometria e o meio importam. Ligações de hidrogênio têm orientação e o efeito hidrofóbico envolve a resposta do solvente, não uma atração de par universal entre grupos apolares. Nesta aula estudamos um modelo radial simples para aprender a ler energia e força. Ele não substitui esses mecanismos nem explica sozinho enovelamento, membranas ou afinidade molecular.

### Um potencial de par precisa de domínio e parâmetros

Adote U(r)=4ε[(σ/r)¹²−(σ/r)⁶] para r>0, ε>0 e σ>0. É a forma 12–6 de Lennard–Jones: ε tem unidade de energia, σ de comprimento, e cada razão σ/r é sem unidade. O termo repulsivo sobe rapidamente e o atrativo decai em longa distância; o expoente12 é uma escolha de modelo, não a derivação quântica universal da repulsão. Escolhemos U→0 quando r→∞. Os parâmetros são prescritos e não foram ajustados a dados de proteína, água ou átomo específico.

### A força é uma derivada com direção, não o sinal de U

Defina n do sítio 1 para o 2 e r como distância entre eles. A força sobre 2 é F_r n, com F_r=−dU/dr; a de 1 é oposta. Derivar dá F_r=(24ε/r)[2(σ/r)¹²−(σ/r)⁶]. F_r>0 empurra para aumentar a distância; F_r<0 atrai para reduzi-la. U negativo não obriga F_r negativo: entre σ e a distância de mínimo, U já é negativo mas a força é repulsiva. A direção usa a derivada do potencial em relação à distância, não a altura isolada do gráfico.

### Zero de energia não é equilíbrio

Em r=σ, os termos de U cancelam: U=0. A força, porém, vale 24ε/σ e é repulsiva. Somar uma constante C ao potencial não muda sua derivada nem qualquer diferença de energia; portanto a localização do zero é uma convenção. O mínimo e as forças têm significado mecânico neste modelo. σ é o cruzamento escolhido do zero, não o ponto de força nula nem automaticamente um diâmetro rígido que proíba r<σ.

### Resolver a força nula encontra o mínimo

Para F_r=0 com r finito positivo, 2(σ/r)¹²=(σ/r)⁶. Dividir pelo fator positivo fornece (r/σ)⁶=2 e r_min=2^(1/6)σ≈1,122462σ. Nesse ponto, (σ/r_min)⁶=1/2 e U=4ε(1/4−1/2)=−ε. A profundidade do poço em relação a U(∞)=0 é ε. O limite F→0 no infinito não é outro equilíbrio a uma distância finita. Não se obtém r_min fazendo U=0.

### A segunda derivada testa estabilidade local

Derivar outra vez dá U″=(24ε/r²)[26(σ/r)¹²−7(σ/r)⁶]. Substituindo o mínimo resulta U″(r_min)=72ε/r_min²>0. Para um deslocamento pequeno δ, U(r_min+δ)=−ε+(1/2)U″(r_min)δ²+termos de ordem maior, e a força restauradora é aproximadamente −U″δ. Essa aproximação é local, não um oscilador harmônico válido para qualquer separação. Força nula identifica um ponto estacionário; a curvatura é o teste adicional de mínimo nesse caso.

### Um exemplo original deixa as escalas visíveis

Primeiro use s=r/σ e U/ε,F_rσ/ε como grandezas sem unidade. Em s=1: U/ε=0 e F_rσ/ε=24. Em s=2: U/ε=4(1/4096−1/64)=−63/1024 e F_rσ/ε=24(2/8192−1/128)=−93/512. Se ε=2E₀ e σ=3L₀, então r=6L₀ corresponde a U=−63E₀/512 e F_r=−31E₀/(256L₀). E₀ e L₀ são unidades de referência escolhidas; os números são fictícios, não valores de uma substância identificada.

### Trabalho confere a relação entre área e energia

Para aumentar a separação de r=σ a 2σ ao longo da coordenada radial, o trabalho feito pela interação é ∫F_rdr=U(σ)−U(2σ)=63ε/1024>0. Isso não contradiz a força atrativa no extremo final: o sinal da força varia ao longo do caminho. A integral inclui o trecho repulsivo inicial. O laboratório integra a força por Simpson e compara à diferença exata de potenciais. Usar apenas a força no extremo multiplicada pela distância não é essa integral. Não estamos calculando o trabalho externo num protocolo com solvente e dissipação.

### Energia por par e energia por mol não dão a mesma unidade de força

Se U e ε forem energias por par em joules e r em metros, −dU/dr estará em newtons. Se ε estiver em kJ/mol, a derivada usa energia por mol e comprimento; para obter força sobre um par é necessário converter a energia por mol em energia por entidade, usando a constante de Avogadro e as unidades adequadas. O código exige uma unidade coerente escolhida pelo leitor e não detecta dimensionalmente entradas. Não chamamos os valores normalizados de pN ou kJ/mol sem essa conversão.

### Um mínimo mecânico não é a distribuição de distâncias

Em um exemplo estatístico separado, suponha um par isotrópico confinado a uma casca finita r_a<r<r_b a temperatura T>0, com U como energia por par e β=1/(k_BT). A densidade radial em relação a dr é proporcional a r²exp(−βU), porque uma casca de espessura dr possui volume 4πr²dr. Não é apenas exp(−βU). No mínimo mecânico, a derivada de ln da densidade é 2/r−βU′=2/r>0, portanto esse ponto não é um máximo interior da densidade radial. O máximo pode inclusive estar na borda externa da casca. Sem confinamento, U→0 e a integral radial até infinito diverge; não se deve normalizá-la como probabilidade de um par ligado. Essa observação não determina uma constante de ligação biológica.

### Corte numérico e mudança de referência são escolhas distintas

A documentação LAMMPS apresenta lj/cut com raio de corte; aqui usamos a expressão sem corte para todo r>0 e não executamos LAMMPS. Se alguém zerar U acima de um corte sem ajustar o valor na borda, cria uma descontinuidade de energia. Subtrair U(r_c) apenas abaixo do corte pode torná-la contínua, mas a derivada ainda pode saltar ali. Isso altera o modelo global, não é simplesmente somar uma constante em todo o domínio. Implementar corte suave ou correções e verificar dinâmica seria outro trabalho, não uma propriedade certificada por este laboratório.

### O alcance deste recorte permanece explícito

As funções racionais conferem energia, força, curvatura e trabalho; a raiz irracional do mínimo é delimitada por bisseção de s⁶−2 e comparada a uma referência de alta precisão. Escalas, sinais e refinamento testam a implementação, não o ajuste físico. Eletrostática com solvente, ligações de hidrogênio direcionais, polarização, muitos corpos, calibração, afinidade e experimentos continuam pendentes. O efeito hidrofóbico e ΔG de associação não foram reduzidos ao valor −ε. Jhuann ainda precisa refazer e explicar o material; a aula não comprova experiência de modelagem molecular.

## Verificações independentes

Seis métodos:fixtures r/sigma1,2,1/2 e sinais;24 modelos de escala e constantes de referência;15 aproximações centrais para derivada e5 comparações de curvatura;intervalos de raiz com16/32/60passos,monotonicidade/sinais/potência exata,referênciaDecimal70 e curvatura positiva;três quadraturas32/64/128 com refinamento aproximadamente de quarta ordem;contratos.

Diferenças centrais usam somente potential,enquanto a força foi derivada separadamente. O trabalho usa force e é comparado à diferença de potential;uma regra de Simpson racional ainda tem erro de quadratura. Bisseção delimita exatamente raiz de s⁶=2 por extremos racionais e sinais,não uma raiz exatamente racional. Decimal é conferência adicional,não argumento único da delimitação. A figura contém curvaU e tabelaF em escalas explicitadas. Não há trajetória,temperatura ou afinidade estimada. O exemplo térmico da casca é uma derivação separada,não algoritmo implementado de amostragem.

## Fontes consultadas e autoria

- Nelson/Cox,Lehninger6PT,Artmed2014(original2013),§2.1 pp.53–54/PDF83–84,consulta textual parcial29/10/2026 de dispersão/repulsão,solvente e contexto de interações. Edição difere da8ª2021 oficial. P.53/PDF83 inspecionada visualmente; sem capítulo integral ou cópia de figura/tabela/exercícios/PDF. Modelo matemático12–6 não é atribuído como código ou fórmula lida nesse recorte.
- [LAMMPS pair_style lj/cut](https://docs.lammps.org/pair_lj.html),Description/Coefficients consultados parcialmente29/10/2026,fórmula12–6,unidades e zero de energia versus mínimo. A fonte usa r_c;adotamos explicitamente função sem corte. Não instalamos/rodamos programa,não copiamos exemplos/scripts e não avaliamos opções aceleradas ou de mistura.
- [JúpiterCCM0121](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121),reaberto29/10/2026,itemI.5 e bibliografia. Ativação01/01/2025 compatível com semestre aprovado2025/1,não prova versão ministrada. Práticas seguem lacuna sem evidência pessoal.

Deduções,números,figura,código e exercícios originais. Função de par sem direção de ligação de hidrogênio,solvente explícito,eletrostática ou muitos corpos. Mínimo deU não é ΔG de associação. Sem copiar PDF ou caminho privado para o site. Revisão pessoal continua pendente.

Conferência de paginação: a extração de intervalo gerou uma leitura ambígua do cabeçalho e motivou uma correção equivocada de offset. Extrações individuais81…85 e imagemPDF83 confirmaram impressa53/PDF83 e54/PDF84,restauradas nas referências antes da entrega;sem assumir causa para a leitura de intervalo. Simpson32/64/128 deu erros assinados0,0006098313640;0,00003906269079;0,000002456726542 em unidades deε,contra trabalho exato63/1024.
