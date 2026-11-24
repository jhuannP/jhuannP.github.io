# Transporte nuclear: localização e troca

29/10/2026. Laboratório original de balanço, não modelo mecanístico de Ran. Unidades de carga e de volume são arbitrárias, taxasa/b ems⁻¹. Não há dados de célula, fluorescência, membrana, receptores ou consumo deGTP medidos/calculados.

Duas regiões homogêneas com carga totalT constante,sem síntese,degradação ou ligação. N é carga nuclear e T−N citosólica. Coeficientes efetivos constantesa,b>0: dN/dt=a(T−N)−bN. Estado estacionário N*=aT/(a+b);tempo de relaxaçãoτ=1/(a+b). A solução analítica é N(t)=N*+(N(0)−N*)exp[−(a+b)t]. O código confere estacionário e derivada; não integra nem simula trajetória.

Vc/Vn são volumes fixos. Concentrações cn=N/Vn e cc=(T−N)/Vc: razão estacionáriacn/cc=aVc/(bVn), não apenas a/b. EmT12,a3,b1,Vc3,Vn1,N*9,citosol3,concentrações9 e1,razão9. Fluxos opostos9 unidades/s cada,fluxo líquido0;τ1/4s. Multiplicar a,b por1/10 preserva localização e razão,masfluxos caem para0,9 eτ sobe para2,5s. Uma imagem estacionária não identifica essas taxas separadamente. ComT0,a razão0/0 retornaNone.

Esse modelo não derivaa/b de Ran, não separa importação,exportação,retenção e outras causas biológicas, nem mede energia ou demonstra equilíbrio termodinâmico. O fluxo líquido nulo de carga não implica ausência de troca ou de processos energéticos ocultos. A prova de relaxação depende do modelo declarado;heterogeneidade e saturação podem invalidá-lo.

`python3 -m labs.nucleo-troca.exchange`

`python3 -B -m unittest discover -s labs/nucleo-troca -t .`

Quatro testes:exemplo;27 modelos com cinco estados/balanço independente de transferências;identificabilidade,escalas e volumes;zero/contratos. int/Fraction,parâmetros positivos,carga não negativa;bool/float rejeitados. Não é validação de célula real.

## Fonte biológica

Alberts e colaboradores,Biologia Molecular da Célula,6ªedição brasileira2017,cap12,pp653–655/PDF689–691,consulta textual parcial29/10/2026;p654/PDF690 visualmente inspecionada para importar/exportar e reciclagem. Figuras e exemplos do livro não copiados. Modelo de balanço,parâmetros e figura locais são próprios, sem atribuição como reprodução do livro. Recorte descreve Ran-GTP/Ran-GDP predominantes, não localização exclusiva. GEF troca nucleotídeo,não fosforilaGDP;hidrólise é deGTP ligado aRan, não reação da carga.

JúpiterCCM0211 reaberto29/10/2026,ativação15/07/2025,itens1/2: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211 . Versão ministrada2025/2 não comprovada. Fonte privada não distribuída.

Próxima revisão20min:comparar montagem/desmontagem em importação/exportação;depois reconstruir razão9 com volumes e mostrar dois conjuntos de taxas com mesma imagem. Mecanismos detalhados,experimentos de perturbação e revisão pessoal pendentes.
