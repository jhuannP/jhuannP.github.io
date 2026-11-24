# Duas massas acopladas e modos normais

27/10/2026. Notas originais com apoio de IA, rascunho para revisão pessoal. Conexão entre Física II e álgebra linear, sem prova de domínio pessoal ou experimento.

## Modelo e solução

Duas massas iguais m>0, molas externas k0>0 presas a paredes fixas e mola central kc≥0, sem atrito/forçamento/massa de molas ou colisões. x1,x2 são deslocamentos do equilíbrio, positivos à direita. Extensão central x2−x1. Equações: m x1''=−k0 x1+kc(x2−x1), m x2''=−k0 x2−kc(x2−x1).

qs=(x1+x2)/√2,qa=(x1−x2)/√2; inversa tem a mesma transformação. Frequências ws²=k0/m,wa²=(k0+2kc)/m; padrões (1,1) e (1,−1). Base normalizada ortonormal preserva normas de posições/velocidades. Para cada modo q(t)=q0 cos(wt)+v0 sin(wt)/w; exige w>0, garantido no modelo exato por k0>0. Em kc=0 há degenerescência e base não única, mas solução física funciona. Não modela modo livre com k0=0.

E=(m/2)(v1²+v2²)+(k0/2)(x1²+x2²)+(kc/2)(x2−x1)². Nas coordenadas modais: soma de (m/2)(qdot²+w²q²). Cada energia modal constante. Momento das massas em geral não conservado: derivada=−k0(x1+x2), forças externas das paredes. Pontos de fixação estacionários não realizam trabalho; potencial é independente do tempo.

Exemplo m=1 kg,k0=kc=4 N/m, x1(0)=0,10 m,x2(0)=0,v1=v2=0: ws=2,wa=2√3,qs0=qa0=0,10/√2. x1=0,05[cos2t+cos(2√3t)],x2=0,05[cos2t−cos(2√3t)]. Acelerações iniciais a1=−0,8,a2=0,4 m/s². Energia total0,04 J=0,01+0,03 J em modos. Uma massa inicialmente parada não significa modo puro ou ausência de energia na mola central.

## Fonte e normalização

Nussenzveig II, 5ª ed./2014, §4.6 pp.113–116/PDF114–117, consulta parcial em27/10/2026; p.115/PDF116 inspecionada visualmente. Fonte considera pêndulos ligados por mola em pequenas oscilações e coordenadas (x1±x2)/2. Nosso modelo usa três molas e (x1±x2)/√2, derivado por forças; frequências correspondem à forma algébrica, amplitudes/energia dependem da normalização. Exemplos, valores, figura, código e exercícios próprios; sem reprodução de problemas, leitura integral ou distribuição do PDF. Fonte curricular não reaberta neste bloco.

## Código e verificação

`modes.py`: parâmetros/entradas/saídas finitos em float, m,k0>0,kc≥0, pares de posição/velocidade e tempo em SI. Solução analítica, sem integração dinâmica no módulo; k0=0 não implementado. A transformação retorna cópias de coordenadas. Valores extremos podem exceder float ou perder fase; finitude não garante precisão arbitrária. Teste de Verlet independente apenas nos testes.

Da raiz: `python3 -m unittest discover -s labs/modos-duas-massas -t .`. Cinco testes: exemplo/modos puros; PVI e derivadas em27 estados; normas/energia/momento; refinamento do Verlet por passos50,100,200 em t=1; limite kc=0 e contratos. Comparação numérica não prova dinâmica real ou todos os tempos/regimes.

Respostas dos12 exercícios:2;12;0,10/√2;−0,8;0,4;0,04;0,01;0,03; sem extensão central no simétrico; PVI mistura modos; energia não garante momento; degenerescência em kc=0. Resoluções na aula.

Revisão proposta em duas sessões: forças e desacoplagem; depois PVI e energia pelas duas rotas. Pendentes: massas/molas gerais, cadeias, dissipação, experimentos e revisão pessoal.

Conferência da entrega: cinco testes locais e14 do catálogo aprovados;772 fórmulas MathML conferidas. Em390px, energia inicial rejeitou0,02 e aceitou0,04 pelo Enter; interpretação de forças externas aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela, Windows real e experimento pendentes.
