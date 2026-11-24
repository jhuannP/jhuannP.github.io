# Raoult, fases e inventários — rascunho didático

29/10/2026. Material original preparado com apoio de IA para revisão de Jhuann. Não representa dados de substâncias reais ou domínio pessoal demonstrado.

## Reprodução e contrato

Da raiz do protótipo:

```sh
python3 -B -m labs.raoult-fracoes.split
python3 -B -m unittest discover -s labs/raoult-fracoes -t .
```

Biblioteca padrão,Fraction. pA*,pB*,P na mesma unidade;N em mol;frações sem unidade. Use inteiros ou Fraction,sem bool,float ou texto. pA*>pB*>0,P,N>0,0<z<1. bubble/dew aceitam também composições0/1 para exibir as fronteiras;split_at_tp não resolve componentes puros ou volatilidades iguais. Na coexistência pura a fração de fases não é dada por um quociente de extremos distintos;é outro problema.

Regimes retornados:liquid/vapor (uma só fase,x/y ausente=None),bubble/dew (fase incipiente,quantidade zero,composição limite calculada) e two-phase (quantidades positivas). Não atribuir inventário finito a uma fase incipiente. A composição x é a fração molar A no líquido;y no vapor;z global;beta é nV/N. Os inventários de A/B e de cada fase são fornecidos. Este recorte não fornece massa,volume,calor ou tempo. Temperatura fixa com troca de calor possível;não é um flash adiabático ou simulação de destilação aberta.

## Modelo e deduções

### A pergunta exige três composições diferentes

Retome frações molares, potencial químico e regra da alavanca. Uma mistura pode conter líquido e vapor de composições diferentes, mesmo que a composição global permaneça fixa. Usaremos x=n_A,L/n_L para o líquido, y=n_A,V/n_V para o vapor e z=n_A,total/N para o sistema inteiro. A fração vaporizada é β=n_V/N. y não é β: um conta a participação de A dentro do vapor; o outro conta a participação do vapor no inventário molar total.

### Escolher o modelo antes de desenhar as curvas

Considere dois componentes A/B não reagentes e uma solução líquida ideal totalmente miscível, em equilíbrio com mistura gasosa ideal a temperatura fixa. As pressões de saturação puras p_A* e p_B* são fornecidas nessa mesma temperatura, com p_A*>p_B*>0. Desprezamos a correção da pressão no potencial químico do líquido, apropriada ao recorte de pressões moderadas do modelo. Não há sólido, líquido imiscível, interface curva ou gás não ideal. O código trabalha com pressões na mesma unidade e não converte valores de substâncias reais.

### A igualdade de potenciais químicos gera uma relação testável

Em equilíbrio, μ_i,L=μ_i,V para cada espécie. Na solução ideal, μ_i,L=μ_i,L,puro+RT ln x_i; no vapor ideal, μ_i,V=μ_i,V,°+RT ln(y_iP/P°). A coexistência da espécie pura relaciona μ_i,L,puro a μ_i,V,°+RT ln(p_i*/P°), na aproximação de pressão do líquido já declarada. Subtrair elimina as referências e fornece RT ln x_i=RT ln(y_iP/p_i*). Os logaritmos envolvem razões sem unidade; não se toma ln de uma pressão dimensional isolada.

### Raoult e Dalton devem fechar para as duas espécies

Exponenciar a igualdade dá y_iP=x_i p_i*. O lado esquerdo é a pressão parcial gasosa; o direito usa a fração molar líquida. Para A: yP=x p_A*. Para B: (1−y)P=(1−x)p_B*. Somar as duas relações recupera a pressão total. Substituir z no lugar de x ou y só é permitido no limite em que toda a matéria está naquela fase. Não é necessário escolher P° para usar essa relação já reduzida.

### Curva de bolha: iniciar vapor com o líquido conhecido

Se a composição do líquido é x, a soma das pressões parciais dá P_bolha(x)=x p_A*+(1−x)p_B*. Em uma descompressão isotérmica de um sistema fechado inicialmente líquido, a primeira bolha aparece quando x=z e P=P_bolha(z). A quantidade de vapor tende a zero, mas sua composição limite é y=x p_A*/P_bolha(x), geralmente distinta de x. Nesta seção a pressão é controlada e o volume pode mudar; não estamos mantendo volume fixo.

### Curva de orvalho: iniciar líquido com o vapor conhecido

Agora conheça y no vapor. Reescreva Raoult como x=yP/p_A* e 1−x=(1−y)P/p_B*. Como essas frações líquidas somam 1, obtenha 1/P_orvalho(y)=y/p_A*+(1−y)/p_B*. Na compressão de vapor puro de fase, a primeira gota aparece com y=z; na descompressão de líquido, essa mesma fronteira marca a última gota que desaparece. Não é a mesma expressão da bolha: uma soma é aritmética em x; a outra é harmônica em y.

### A região de fases usa a composição global

Para 0<z<1 e volatilidades distintas, P_orvalho(z)<P_bolha(z). A T fixa, P acima da bolha deixa apenas líquido; abaixo do orvalho deixa apenas vapor. Entre as fronteiras, ambas as fases têm quantidade positiva. Exatamente na bolha β=0 e y descreve vapor incipiente; no orvalho β=1 e x descreve líquido incipiente. Fora da coexistência, o solver retorna None para a composição da fase ausente, sem criar uma fase com quantidade negativa. Componentes puros e p_A*=p_B* são casos degenerados excluídos do solver, não resultados para extrapolar pelo quociente 0/0.

### A linha horizontal encontra as duas composições

Dentro da região bifásica, a pressão dada fornece x=(P−p_B*)/(p_A*−p_B*) e depois y=x p_A*/P. Esses extremos são determinados por T,P e pelo modelo material, não pela quantidade total de cada fase. O ponto global z deve ficar entre x e y; uma linha horizontal na figura conecta os dois estados coexistentes. O eixo horizontal representa x na curva de bolha, y na de orvalho e z no ponto global. Não é uma sequência espacial através do recipiente.

### A alavanca vem dos inventários, não do desenho sozinho

Os balanços N=n_L+n_V e Nz=n_Lx+n_Vy dão z=(1−β)x+βy. Isolando, β=(z−x)/(y−x), e a fração líquida é 1−β. São frações de quantidade de matéria, não de massa ou volume. O denominador é positivo no interior deste modelo, pois A é o mais volátil. Uma β fora de [0,1] indica que os extremos escolhidos não são compatíveis com o estado global, não uma quantidade física negativa de fase.

### Exemplo original: composição rica não significa muita fase

Prescreva p_A*=80 kPa, p_B*=20 kPa, P=40 kPa, z=2/5 e N=5 mol; não atribuídos a moléculas reais. As fronteiras globais são P_bolha=44 kPa e P_orvalho=200/7 kPa≈28,571 kPa: o estado é bifásico. Os extremos são x=1/3 e y=2/3, enquanto β=1/5. Portanto há 4 mol de líquido e 1 mol de vapor. A se reparte em 4/3 mol líquidos e 2/3 mol gasosos, somando 2 mol; B em 8/3 e 1/3 mol, somando 3 mol. Ter 2/3 de A no vapor não significa vaporizar 2/3 dos 5 mol.

### Seguir uma descompressão não é manter a fase com composição fixa

Para o mesmo z=2/5, a primeira bolha a 44 kPa tem y=8/11. A 40 kPa, y=2/3 e β=1/5. A 32 kPa, x=1/5, y=1/2 e β=2/3. A última gota desaparece a 200/7 kPa, com y=z=2/5 e x=1/7 como limite incipiente. O sistema fechado conserva z, enquanto as composições e quantidades das fases mudam. Retirar vapor durante uma destilação muda o inventário e exige outro balanço; não é seguir essa mesma linha de z constante.

### O enriquecimento decorre da volatilidade relativa

Divida as relações de Raoult: y/(1−y)=(p_A*/p_B*)x/(1−x). A volatilidade relativa é α=p_A*/p_B*=4 no exemplo. Também y−x=x(1−x)(p_A*−p_B*)/P>0 no interior: o vapor fica enriquecido no mais volátil. Isso não diz que todo vapor é A nem que o líquido não contém A. Com p_A*≠p_B*, o modelo ideal não produz azeótropo interior; soluções reais podem exigir coeficientes de atividade e apresentar outro comportamento. Não inferimos seletividade real de uma mistura desconhecida.

### Outra incógnita permite uma verificação numérica

Defina K_i=p_i*/P e escreva y_i=K_i x_i. O inventário de cada espécie dá x_i=z_i/[1+β(K_i−1)]. Subtrair as normalizações das duas fases conduz a f(β)=∑z_i(K_i−1)/[1+β(K_i−1)]=0. Os denominadores são positivos em 0≤β≤1. Para o interior bifásico, f(0)>0, f(1)<0 e f′(β)=−∑z_i(K_i−1)²/[1+β(K_i−1)]²<0; há uma única raiz. O laboratório usa bisseção racional e compara seu intervalo à solução fechada, sem confundir tolerância de cálculo com erro do modelo físico.

### O que ainda seria necessário para uma aplicação real

A temperatura é mantida por um banho; vaporizar pode exigir calor, mas este recorte não calcula energia, entalpia, volume ou tempo de evaporação. O equilíbrio não determina a cinética e o solver não resolve uma expansão adiabática. Precisaríamos de dados de saturação confiáveis, atividades/fugacidades, balanço energético e incertezas para estudar um equipamento ou substâncias reais. Regra de fases geral, azeótropos, líquidos imiscíveis, sólido–líquido e destilação em estágios continuam pendentes. Aprovação na disciplina e este rascunho não certificam domínio; refazer e explicar o inventário é a próxima revisão pessoal.

## Verificação independente

Seis métodos de teste:exemplo exato com inventários e segunda pressão;27 estados fabricados por pressões parciais e inventários conhecidos;60 classificações em12 famílias de parâmetros(incluindo fronteiras incipientes);27 intervalos de bisseção de um balanço em beta;troca da unidade de pressão/escala de inventário e limites das curvas;contratos e degenerescências.

O oráculo de27 casos começa com x,beta conhecidos,calcula pressões parciais de A/B e cria z pelo inventário,em vez de repetir a solução fechada do solver. A bisseção trabalha na equação material f(beta),monótona no intervalo;intervalo de largura até2^-60 confere a solução fechada sem provar idealidade física. Pressões,moles e frações são racionais exatos neste recorte. Testes internos não são novos métodos de teste.

## Fontes efetivamente consultadas

- Levine,Physical Chemistry,6ªedição,copyright2009 (nome do arquivo2008 não é ano editorial confirmado). Consulta textual parcial29/10/2026:§9.6 pp.279–281/PDF297–299,potenciais químicos,Raoult e hipóteses;§12.6 pp.362–364/PDF380–382,curvas de pressão–composição,regiões e linhas de coexistência. P.363/PDF381 inspecionada visualmente para Eqs.12.37–12.38,evitando erros do OCR. Sem leitura integral ou cópia de figura,exemplo,problema,solução ou PDF. Números80/20kPa e inventários próprios,não identificar substâncias reais.
- [JúpiterCCM0124](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124),reaberto29/10/2026:item6 inclui equilíbrio binário líquido–vapor,líquido–líquido e sólido–líquido;item5 fornece misturas e potencial químico. Ativação01/01/2025 posterior à aprovação2024/1;versão ministrada não recuperada. ReferênciaLevine2009 consta da bibliografia.

Material permanece parcial:soluções reais,azeótropos,regra de fases geral,outras fases,balanço energético,incertezas e revisão pessoal pendentes. Nenhum PDF ou caminho privado do acervo servido no site. Figura calculada com modelo original e rotulada como dados fictícios.
