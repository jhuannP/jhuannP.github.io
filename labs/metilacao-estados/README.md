# Manutenção incompleta: lei de estados e denominadores

29/10/2026. Modelo original em rascunho para revisão de Jhuann.

M/H/U probabilidades deDNA uniformemente escolhido estar com duas/uma/zero marcas num sítioCpGsimétrico. CadaDNAreplica semiconservativamente,novasfitas semmarca. Apósreplicação,cada sítioHé completado com probabilidade hipotéticap,constante e dependente sódoestado;sem denovo,remoção ativa,seleção,morte ou perdas.

M→duasH;H→umaH eumaU;U→duasU,antes da manutenção. Lei pósmanutenção:M′=p(M+H/2),H′=(1−p)(M+H/2),U′=U+H/2. Soma1. m=M+H/2 é proporção esperada de alvos marcados;m′=(1+p)m/2. M+Hconta moléculas com marca,Mconta totalmente marcadas. Não confundir com frações efetivas de uma população finita,correlações entre irmãs ou taxa enzimática real.

InicialM1,p1/2:após2 rodadas,M3/8,H3/8,U1/4. Trêsobserváveis3/8,3/4,9/16. Semmanutençãop0recuperam=2⁻ⁿ; comp1einicialM1,preservaM1. Contudo p1não cria marca emU. TodosH e misturaM/Umeioameio têm mesma média1/2 e estados distintos; média não identifica o pareamento das marcas. Nenhuma previsão de expressão,doença ou herança transgeracional.

Fonte: Alberts,BiologiaMolecular daCélula,tradução6ªedArtmed2017,cap7pp404–405/PDF440–441,consulta textual parcial29/10/2026;p405/PDF441visual. p406/PDF442também visual,sem desenvolver histonas. Regra probabilística e figura locais,não atribuídas à fonte. [JúpiterCCM0121](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121) reaberto29/10,ativação01/01/2025,itemII.8;versão ministrada não comprovada. PDFprivado não distribuído.

```sh
python3 labs/metilacao-estados/states.py
python3 -B -m unittest discover -s labs/metilacao-estados -t .
```

Cinco testes: referência/trêsobserváveis; enumeração independente por fita/filha,3estados×4p; normalização e recorrência do momento,4leis×5p×11rodadas; limitesp0/p1até20rodadas e média não identificadora;contratos. n0..100,pint/Fraction,leis de três probabilidades soma1;sem bool/float. Não há validação experimental,pedagógica ou pessoal.
