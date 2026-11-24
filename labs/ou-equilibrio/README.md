# OU, transição e equilíbrio na malha

Rascunho para revisão pessoal. Laboratório de momentos com coeficientes racionais prescritos,não amostra trajetórias. Para X_{n+1}=rX_n+η_n,inovações independentes centradas de variância q,independentes do passado,evolve itera m←rm,V←r²V+q. int/Fraction;variâncias não negativas;n0..10000. A lei gaussiana conjunta requer inovações e início gaussianos;momentos não garantem gaussianidade por si.

OU escalar dX=−θXdt+σdW,θ>0:ρ=e^(−θh),q=S(1−ρ²),S=σ²/(2θ). Coeficientes comρ1/2,q3/4 correspondem aS1 eθh=ln2,não ao passo1/2 da tabela Euler. Começar X0=2 determinístico dá após dois passos média1/2 e variância15/16. Começar N(0,S),independente do ruído futuro,mantém a lei estacionária;igualar variância sem inicialização gaussiana não basta para estacionariedade estrita.

Euler: r=1−θh,q=σ²h. Para |r|<1,V_h=q/(1−r²)=S/(1−θh/2). θ1,σ²2 e h1/2,1,3/2 dão V4/3,2,4,contraS1. h2 tem r−1 e V_n=4n desde zero,sem variância estacionária finita com ruído positivo. Função stationary só cobre |r|<1;casos degenerados sem ruído no limiar não são classificados como impossíveis em geral.

Exatidão refere-se à distribuição de transição nos nós. Usar o mesmo Z numa transição exata e em Euler não cria automaticamente o mesmo incremento browniano:integral ponderada e ΔW têm correlação própria. Não implementamos acoplamento de erro forte,detecção de cruzamento,ponte OU,estimação de parâmetros ou modelo físico validado.

## Fontes consultadas parcialmente em29/10/2026

Pavliotis,Stochastic Processes and Applications,Springer2014,§3.7 início p79/PDF92 e p80/PDF93,solução3.101 e momentos3.103;textual parcial e p80 também visual. §1.4 p15,trecho textual de processo estacionário por mudança temporal,localizador em extração;§4.4 p103/PDF115,trecho introdutório/invariante lido como contexto,sem polinômios ou espectro adotados. Offset+13 em p80,mas+12 em p103,conferidos localmente. Fórmulas próprias na notação escalar;sem PDF privado ou figuras/exemplos reproduzidos. Chorin–Hald não relido;percurso complementar,sem nova consulta de oferta ou equivalência USP.

## Verificação

```sh
python3 -B -m unittest discover -s labs/ou-equilibrio -t .
python3 labs/ou-equilibrio/moments.py
```

Cinco métodos:48 estados comparados à soma independente de pesos de inovações;27 decomposições em dois intervalos;nove núcleos preservandoS;três vieses Euler,limiar e marco exato;contratos. Python/desafio e painel existentes da aula permanecem próprios. Esses testes são de momentos,não de gaussianidade empírica ou evidência de pesquisa.
