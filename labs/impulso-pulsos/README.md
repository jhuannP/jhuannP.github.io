# Impulso, sistema e pulsos de força

27/10/2026. Aula existente ampliada para15 seções/12 exercícios, em rascunho com apoio de IA; revisão pessoal de Jhuann pendente. Três seções, dois exercícios, exemplo, Python e desafio anteriores preservados. Novos exemplos, figura, laboratório e contas próprios; sem resultado experimental ou de IC.

## Hipóteses e fundamentos

Referencial inercial, mecânica newtoniana, sistema fixo de partículas de massas constantes. p=mv, J=∫Fresultante dt=pf−pi, vf=vi+J/m. Componentes têm sinal; impulso vetorial não é soma de módulos. Unidade N s=kg m/s, distinta de joule=N m.

Força média Fm=J/Δt para Δt>0. Ela preserva área, não pico ou perfil. Triângulo de pico12 N/base0,5 s e retângulo de6 N/base0,5 s têm J=3 N s e média6 N. Exemplo constante anterior preservado: m=2 kg, Δv=1,5 m/s.

Pulso triangular original, com t numérico em segundos: F=48t no intervalo[0,1/4] e F=48(1/2−t) em[1/4,1/2], zero fora. Coeficiente48 em N/s; integral J=24t² ou3−24(1/2−t)², com coeficientes dimensionados correspondentes. vi=−1 m/s dá vf=1/2 m/s. No instante1/4 s, ambos perfis dão v=−1/4 m/s; em1/8 s, triangular v=−13/16 e retangular v=−5/8 m/s. Mesmos extremos ou mesmo ponto intermediário não igualam todo o movimento.

Mesma velocidade final não fixa deslocamento. Com m=2 kg, repouso inicial e observação até1 s: pulso6 N até0,5 s seguido de zero dá Δx=9/8 m;3 N ao longo de1 s dá3/4 m. Ambos J=3 N s e vf=3/2 m/s. Fórmula derivada por integrar aceleração duas vezes:

Δx=vi(tf−ti)+(1/m)∫ti^tf(tf−t)F(t)dt.

O primeiro momento temporal da força altera o deslocamento, mesmo com a integral de F igual. No exemplo de duração0,5 s com pulso triangular ou retangular simétricos, os deslocamentos finais coincidem; não alegamos que todos os perfis de mesma área precisem dar posições finais diferentes. A figura mostra velocidades intermediárias distintas.

## Sistema e conservação

Duas partículas: dp1/dt=F12+F1ext, dp2/dt=F21+F2ext. Sob forças internas newtonianas F12=−F21, somar dá dP/dt=Fext total. Só no sistema dos dois corpos o par é interno. No corpo1 sozinho, F12 é externa. Fluxo de massa e momento de campos não são cobertos.

Exemplo próprio: m1=2 kg,v1=1 m/s,m2=3 kg,v2=−1 m/s, P inicial=−1 kg m/s. Impulsos internos+3/−3 N s dão momentos5 e−6, velocidades5/2 e−2 m/s, mesmo P total. A energia cinética não foi imposta; a interação poderia transferir energia de outra forma.

Fext(t)=0 em todo instante garante P constante. Somente Jext=0 garante Pf=Pi, permitindo variação intermediária. Se ‖Fext‖≤Fmax, ‖Jext‖≤FmaxΔt. Limite2 N por0,01 s dá0,02 N s; razão com3 N s é1/150, correção de velocidade≤0,01 m/s para2 kg. Não dividir por momento inicial nulo ao definir erro relativo. Uma colisão curta não elimina automaticamente a relevância de impulsos externos.

## Laboratório exato

`pulse.py` aceita tempos, forças, massa e condições em int/Fraction, sem bool/float. Dois ou mais nós de tempos estritamente crescentes definem interpolação linear por trechos e extensão zero fora. Nos extremos, o valor pontual é o do nó, mas saltos ao exterior não alteram as integrais. Intervalo invertido é rejeitado; duração zero permite impulso zero, sem força média.

Em um trecho iniciado em u com altura f e inclinação b, integrar F=f+b(t−u). O código recorta o intervalo e usa primitivas para ∫Fdt e∫tFdt. `propagate` usa essas duas integrais para posição/velocidade e exige massa positiva. Posição/velocidade iniciais são dadas no início do intervalo solicitado. Não há modelo de contato ou inferência de dados reais; racional exato também pode ficar caro com entradas grandes.

Da raiz: `python3 -m unittest discover -s labs/impulso-pulsos -t .`.

Cinco testes: exemplos/sinais; momentos temporais por Simpson racional independente em182 intervalos de dois perfis, com integrandos até grau2; igualdade de velocidade e diferença de deslocamento, mais composição de estados; comparação com velocity Verlet em F(t)=8t e erro espacial de segunda ordem; contratos e limites. Simpson é exato para esses polinômios, não para uma força arbitrária. O integrador numérico separado não transforma os pulsos em dados experimentais.

## Fontes e páginas

Nussenzveig, Curso de Física Básica1: Mecânica,5ª ed., Blucher2013, reimpressão2017 identificada anteriormente. Consulta parcial em27/10/2026: §8.1 pp.186–187/PDF187–188 (pares/sistema/forças externas); §9.2 pp.212–213/PDF213–214 (impulso e média). p.212/PDF213 inspecionada visualmente. Página do PDF contada desde1; sem leitura integral dos capítulos ou cópia de seus exemplos/figuras.

[Feynman LecturesI, cap.10](https://www.feynmanlectures.caltech.edu/I_10.html), edição oficial online, §§10–1/10–2 parcialmente consultados em27/10/2026 para terceira lei e soma de momentos. Não transferimos paginação para a tradução local. Fontes de FísicaI não fixam edição; a versão efetivamente ministrada em2023 segue não recuperada. Programa e aprovação vêm do mapa existente; não reabertos neste bloco.

## Exercícios e revisão

Respostas dos12 itens:1,5; não;3;6;0,5;−13/16;9/8;−1;0,02; sistema dos dois corpos; igualdade nos extremos sem constância garantida; integrar tempo versus deslocamento. Dicas e resoluções completas na aula.

Revisão proposta de20min: desenhar pulsos e integrar áreas com sinais; depois delimitar os sistemas e justificar uma cota externa. Dúvidas e avaliação pessoal permanecem em branco. Pendentes: colisões2D, centro de massa, sistemas abertos, contato real e revisão pessoal. Não usar a página preparada como certificação de domínio ou experiência docente.

Conferência da entrega: cinco testes locais e14 do catálogo aprovados;726 estruturas MathML verificadas. No navegador390px, exercício11 rejeitou constância em todo instante e aceitou igualdade entre extremos pelo Enter; figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
