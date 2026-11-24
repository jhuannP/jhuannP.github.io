# Gelo e calor latente — decidir o estado final

27/10/2026. Notas originais com apoio de IA, rascunho para revisão pessoal. Python opcional. Percurso de reforço, não disciplina formal adicional ou cobertura de exame.

## Hipóteses e contas

Água pura perto de 1 atm, fusão a 0°C, sem ambiente, recipiente ou trabalho adicional. Balanço de entalpia a pressão constante, com trabalho de expansão incorporado nos parâmetros; não é um modelo de recipiente rígido e pressão variável. ci=2,1 J/(g K), ca=4,2 J/(g K), Lf=334 J/g, valores arredondados constantes. Sem sal, vapor, super-resfriamento, cinética ou medidas reais.

100 g de gelo a −10°C, 200 g de água a 40°C: água pode ceder 33 600 J até zero; aquecer gelo exige 2 100 J; restam 31 500 J < 33 400 J para fundir tudo. Fundem 31 500/334 g, restam 950/167≈5,69 g; líquido final 300−950/167 g. Tfinal=0°C. Conservação: 33 600=2 100+334·(31 500/334).

Variante água a 60°C: 50 400−35 500=14 900 J aquecem 300 g de água, T=745/63≈11,83°C. Variante 100 g de gelo a −20°C e 10 g de água a 5°C: toda água congela, faltam 650 J para o gelo chegar a zero; 110 g de gelo final a −650/231≈−2,81°C.

Referência energética opcional: gelo em zero tem h=0; gelo a T≤0 tem h=ciT, líquido a T≥0 tem h=Lf+caT. H inicial=mi ci Ti+ma(Lf+caTa), massa M=mi+ma. H<0: gelo a H/(Mci); 0<H<MLf: coexistência a zero, massa líquida H/Lf; H>MLf: água a (H−MLf)/(Mca). Fronteiras H=0 e H=MLf são gelo e água a zero. h é uma entalpia específica aproximada, não calor contido; a referência cancela no balanço por conservação de massa.

Q=mcΔT não descreve a mudança de fase; Q=ΔmLf usa somente a massa transformada. ΔT=0 não garante Q=0. Gramas com J/kg dão erro por fator 1000. Temperatura de patamar não prevê tempo.

## Fonte

[OpenStax Physics §11.3](https://openstax.org/books/physics/pages/11-3-phase-change-and-latent-heat), consulta parcial em 27/10/2026: fase, Q=mLf, tabela 11.3 com Lf da água 334 kJ/kg, patamar. Capacidades 2,1/4,2 J/(g K) são valores arredondados fixados no exemplo, não extraídos como dados exatos dessa tabela. Contextos, misturas, classificação, figura e exercícios próprios. Sem problemas reproduzidos, leitura integral, vídeo assistido ou experimento realizado.

## Código e verificações

`ice.py` usa int/Fraction, rejeita bool/float. Massas em g não negativas, total positivo; temperaturas em °C com gelo −40..0 e água 0..90. Energia em J, capacidades/latente fixos; saídas imutáveis com estado, temperatura e massas. Domínio limitado para não extrapolar a outras fases. Frações exatas verificam o modelo arredondado, sem precisão física exata.

Da raiz: `python3 -m unittest discover -s labs/gelo-calor-latente -t .`. Cinco testes: três exemplos, 108 misturas contra balanços de energia cedida/recebida por fases inicial/final, fronteiras, escalas de massa/limites simples e contratos. A conferência é do modelo, não de um experimento, simulação temporal ou todas as condições reais.

Respostas dos 12 exercícios: 33600 J;2100 J;33400 J;31500 J;31500/334 g;0°C;745/63°C;334000 J/kg; Q pode ser não nulo no patamar; comparar energias antes da fase; H=MLf é líquido a zero; aritmética exata não elimina aproximações físicas. Resoluções completas na aula.

Revisão proposta: reconstruir mistura e variante a 60°C em duas sessões. Experiência apenas proposta, sem dados coletados. Pendentes: recipiente e perdas na mudança de fase, vapor, sais, curvas completas e revisão pessoal/uso com aluno.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 752 fórmulas MathML conferidas. A contagem esperada das misturas foi corrigida de 324 para 108 após a primeira execução; os balanços já passavam, e a repetição dos cinco testes passou. Em 390 px, exercício da massa rejeitou 100 e aceitou 94,3113772455 pelo Enter; interpretação do patamar aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, uso com aluno, experimento, leitor de tela e Windows real pendentes.
