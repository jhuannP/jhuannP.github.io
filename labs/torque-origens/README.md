# Torque, origem e apoios ideais

Modelo sintético plano, força prescrita, corpo rígido ideal; int/Fraction sem float/bool. Posições em m, forças em N, torques em N m. Rascunho assistido por IA, revisão pessoal pendente. Nenhuma medição ou resultado da IC.

Na raiz:

```sh
python3 -B -m labs.torque-origens.statics
python3 -B -m unittest discover -s labs/torque-origens -t .
```

`resultant(loads,origin)` soma vetores e momentos com coordenadas na mesma base; até100 pares (ponto,força), incluindo lista vazia. `cross` devolve apenas componente z. Não infere pontos de aplicação, dinâmica, rigidez ou suportes reais. Transladar origem por a produz tau'=tau−a×R. Deslocar uma força ao longo da sua linha preserva momento para corpo rígido, sem garantir mesma deformação interna.

`beam(L,W,P,x)` calcula reações verticais candidatas de uma barra horizontal uniforme: peso W em L/2, carga P em x e apoios nas extremidades0,L. L>0,W/P/x>=0. x pode excederL para estudar carga externa sobre prolongamento ideal sem peso; geometria/rigidez desse prolongamento é pressuposta, não calculada. Sem forças horizontais, binários de apoio ou deformação. RA=W+P−RB,RB=W/2+Px/L. `unilateral_ok` verifica SOMENTE se ambas reações são não negativas; não certifica estabilidade, atrito ou suporte real. Apoio que só empurra não exerce reação negativa. Igualdade zero é contato limite, sem estabilidade demonstrada.

Referência L6,W12,P6,x5: RA7,RB11, força/torque totais0. Com x15,RA−3,RB21 satisfazem equações algébricas, mas são incompatíveis com ambos apoios apenas de compressão. Não se usa o resultado negativo como contato validado. A posição x15 é novo cenário com prolongamento ideal sem peso, não deslocamento permitido de uma carga numa barra material limitada a[0,6].

Cinco testes incluem729 mudanças de origem,81 candidatos de viga por balanço independente em B,81 identidades de trabalho virtual por radiano,binário,linha de ação e material anterior. Nenhuma integração de rotação ou dinâmica após perda de contato. Figura original somente do cenário x5.

Fonte local autorizada:Nussenzveig,Curso de Física BásicaI,5ªedição2013/reimpressão2017,§11.3pp281–283/PDF282–284 e§12.8pp339–340/PDF340–341,consulta textual parcial30/10/2026;p283/PDF284visual para vetor/origem. Nenhum exercício/figura copiado nemPDF distribuído. Fonte pública auxiliar:FeynmanLecturesI,cap18,corpo inicial18–1/18–2 consultado parcialmente30/10,sem alegar leitura integral de torque ou transferir paginação. Livro em https://www.feynmanlectures.caltech.edu/I_18.html .
