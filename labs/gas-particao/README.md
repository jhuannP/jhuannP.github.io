# Gás ideal: estados e controles

Modelo sintético monoatômico 3D de Maxwell–Boltzmann, equilíbrio, interações e estrutura interna desprezadas. Rascunho didático assistido por IA, revisão pessoal pendente; não são dados ou pesquisa de Jhuann.

Na raiz do site:

```sh
python3 -B -m labs.gas-particao.gas
python3 -B -m unittest discover -s labs/gas-particao -t .
```

`state(N, theta, V, tau)` recebe inteiros/Fraction positivos, N inteiro de 1 a 100. theta=kB T_K tem unidade de energia; tau=lambda³ tem unidade de volume, no mesmo sistema que V. Z e N tau/V são adimensionais, P é energia/volume, U é energia e Cv/kB adimensional. Tau é informado no estado considerado; o programa não valida sua relação física com theta, massa ou h. Ao quadruplicar theta com massa e h fixos, tau divide por oito. Não o mantenha constante ao derivar ln Z em temperatura.

ZN=(V/tau)^N/N!, P=N theta/V, U=3N theta/2. Preservamos N! exatamente dentro da aproximação semiclassica; não é a partição quântica exata para N finito. O diagnóstico N tau/V pequeno é necessário ao regime clássico diluído, mas não testa interações, contorno ou todo regime de validade. A rotina deliberadamente não devolve um selo de validade.

Referência própria N=3,theta=2,V=300,tau=1: Z=4500000,P=1/50,U=9,Cv/kB=9/2,Ntau/V=1/100. N=3 facilita a aritmética, sem representar um gás macroscópico medido. Volume duplo multiplica Z por 8 e reduz P à metade, mantendo U. Theta quádruplo e tau/8 multiplicam Z por 512, P e U por 4.

Os testes comparam derivadas de log-partição usando lgamma e diferenças centrais, verificam uma identidade multinomial por ocupações, escalas exatas e exemplos anteriores. Tolerâncias finitas não certificam todo argumento. Pesos de ocupação 1/prod(nj!) são uma verificação algébrica, não uma enumeração de estados quânticos físicos. A figura é um diagrama de razões, não trajetória temporal ou simulação de partículas.

Fonte primária consultada parcialmente em 30/10/2026: David Tong, Statistical Physics, §§2.2–2.2.1,2.2.3 e condição clássica em2.2.4, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S2.html . Não há cópia de problemas ou figuras; implementação, testes e comparação são locais. Grande canônico, estatística quântica, mistura e limites gerais não desenvolvidos aqui.
