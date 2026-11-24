# Kepler: tempo, geometria e cálculo verificável

Material original assistido por IA; revisão de Jhuann pendente. Entradas prescritas, sem dados observacionais. Não demonstra aprovação ou domínio pessoal.

Dois corpos pontuais isolados, gravitação newtoniana, movimento relativo no plano, μ=G(m₁+m₂). Use unidades L/T coerentes. a em L, μ em L³/T², M/E em radianos. state retorna x,y,r em L, velocidades em L/T, área em L² e período em T. 0≤e≤0,99, 0≤M,E≤2π; 1e−6≤a≤1e6, 1e−12≤μ≤1e12. bool, string e números não finitos rejeitados. Sem redução automática de voltas; a convenção ν=2π no endpoint preserva o rótulo de volta, fora dele ν é direção em [0,2π).

solve faz 48 passos de bisseção; half_width é largura nominal float, não certificado intervalar rigoroso. Em aritmética exata, erro ≤π/2^48 e ≤|resíduo|/(1−e); seno e subtrações arredondam. Não promete precisão relativa uniforme perto de M=0. Não implementa Newton, ponto fixo, escalas temporais, orientação celeste ou efemérides.

Exemplo original a=2, μ=8, e=0,6, E=π/2: M=π/2−0,6, (x,y)=(−1,2;1,6), ν≈126,87°, r=2, v=(−2,0), energia específica−2, momento angular específico3,2. Figura original com 12 marcadores uniformes em M. Não é ajuste de astro real.

## Reprodução
Da raiz do protótipo:
```sh
python3 -B -m unittest discover -s labs/kepler-anomalias -t .
```
Seis métodos: marcos/quadrantes; 30 raízes manufaturadas e seis comparações Decimal60 (210 bisseções e série de seno com110 termos); 60 estados com geometria/energia/momento; três áreas por soma poligonal com12000 segmentos; circular/sensibilidade/escala; contratos. Decimal independente não usa sin float na avaliação de referência; recebe a entrada float exata. Quadratura por triângulos converge, não fornece certificação geral.

## Fontes realmente consultadas em 29/10/2026
- [Júpiter AGA0106](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=AGA0106): página principal lida, mantém ativação01/01/2027, bibliografia nominal e conteúdo mais amplo. Não comprova turma2022. Mapa detalhado anterior baseado no programa2023 indexado, limitação preservada; vínculo IF2022/2 RN não alterado.
- [Bryan Weber — Circular and Elliptical Orbits](https://orbital-mechanics.space/time-since-periapsis-and-keplers-equation/elliptical-orbits.html): recorte das áreas e relações185–196, consulta parcial. Apoio à dedução área/tempo, sem copiar figuras, animações ou exemplo. A derivação local usa diretamente x dy−y dx.
- [Richard Fitzpatrick — Elliptic orbits, UT Austin](https://farside.ph.utexas.edu/teaching/celestial/Celestialhtml/node33.html): relações4.55–4.70 e interpretação geométrica consultadas parcialmente. A afirmação textual de mesmo quadrante não foi adotada: E=π/2 e e=0,6 já dá ν>π/2. Nesta aula só a metade superior/inferior é comum, e atan2 controla o ramo.
- PDF público IAG2025 e página UFRGS tiveram timeout; resultados de busca não substituíram leitura do corpo. Não usados como fonte do conteúdo. Bibliografia nominal continua não localizada no acervo conforme auditoria anterior; não foi buscada novamente nesta rodada.

Não copiar livros/PDFs pessoais para o site. As fontes são apoio complementar público, não equivalência curricular ou autoria de investigação de Jhuann.
