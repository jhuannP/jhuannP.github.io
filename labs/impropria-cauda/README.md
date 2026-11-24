# Cauda conhecida e transformação regular

Caso original sintético f(x)=x^(−3/2)+3x^(−2),x≥1,integral5. Coordenadas adimensionais. Rascunho assistido porIA,revisão pessoal pendente;sem experimento real. Não é integrador geral de domínio infinito.

Da raiz:

```sh
python3 -B -m labs.impropria-cauda.tail
python3 -B -m unittest discover -s labs/impropria-cauda -t .
```

Cortes R=n²,nint1..10000:cauda exata2/n+3/n²,parcial5−cauda. Emn10,R100,cauda23/100;emn20,R400,cauda43/400. `minimum_cutoff`procura por monotonicidade o menor n do domínio com cauda≤tolerânciaFractionpositiva. Para1/100,n202,R40804;isso controla somente cauda,não erro total de quadratura. Tolerância abaixo da cauda do maior n é rejeitada,sem prometer precisão fora do domínio.

Primeira troca u=1/x dág(u)=u^(−1/2)+3 em(0,1],ainda ilimitado em0. Segunda troca u=t² produz2+6t em(0,1],com extensão analítica2 emt0. A rotina retorna a expressão regularizada; não computa0×infinito. O jacobiano é indispensável. Regras racionais já existentes em labs/quadratura-erro/experiment.py conferemtrapézio/Simpson5exatos no integrando linear. Não foi escrito novo motor de quadratura.

`finite_comparison`reutiliza numerics.trapezio em[1,R],float,com número de painéis1..100000 eR>1. Devolve erro de quadraturaQ−I_R e erro total assinadoI−Q=cauda−(Q−I_R). Os sinais podem se cancelar;proximidade acidental de5 não certifica parcelas pequenas. A desigualdade segura é|I−Q|≤cauda+|Q−I_R|. O erro finito neste exemplo é conhecido por referência analítica, não estimado automaticamente para função geral. Extremos de domínio/erro de arredondamento não certificados.

Cinco testes:cauda/corte mínimo;antiderivada comDecimal60dígitos emoitocortes;24identidades de jacobiano,endpoint ecincoregras exatas;decomposição assinada emtrêsmalhas;material antigo/contratos. O livro tem outras técnicas,como subtração de Taylor,que não foram implementadas aqui. A divergência dex^(−1)não se resolve apenas cortando ou reparametrizando.

Fontes consultadas30/10/2026:Burden/Faires/Burden,10ªedição,tradução/3ªbrasileiraCengage2016,§4.9pp274–278/PDF288–292visual;sumárioPDF12,offset14confirmado pelos cabeçalhos. Exemplo comsin e técnica de Taylor vistos incidentalmente,não reproduzidos/implementados. ApostolI,2ªedição1967,§10.23pp416–418/PDF436–438texto,p417/PDF437visual porqueOCRomitiuigualdade ems≤1. NISTDLMF3.5(i)–(ii),corpoE1–E8 e hipóteses de derivadas, https://dlmf.nist.gov/3.5 . Não foi lida seção vi de autovalores nesta consulta. Fórmulas básicas apoiam derivação;composto,família de cortes,figura e código locais. PDFs privados não distribuídos.
