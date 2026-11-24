# De Broglie: escolher o regime e conferir as unidades

Notas de aula originais em rascunho para revisão de Jhuann. Apoio parcial ao item24 de CCM0222; não encerra difração em cristais, fenda dupla quântica ou teoria de pacotes. Pré-requisitos: momento, energia cinética, relatividade especial e fase de onda. Nenhum dado experimental ou resultado de IC é apresentado.

## Da fase ao momento

Uma componente exp[i(kx−ωt)] repete a fase no espaço com comprimento2π/|k|. Usando p=ℏk e ℏ=h/(2π), resulta λ=h/|p|. O sinal do momento informa a direção; o comprimento é positivo. Em SI, (J·s)/(kg·m/s) é metro. Uma onda plana tem densidade espacial constante e não pode ser normalizada como estado de uma partícula na reta inteira; um pacote localizado envolve vários momentos. Não inferimos uma trajetória senoidal.

## Da energia ao comprimento

Elétron livre, energia cinética K>0, energia de repouso E₀=m_ec²:

- Aproximação não relativística: K=p²/(2m), portanto λ_nr=hc/√(2E₀K).
- Relação relativística: E²=p²c²+E₀², E=K+E₀, logo p²c²=K²+2KE₀ e λ_rel=hc/√[K(K+2E₀)].

O ganho K=eU vale para aceleração ideal a partir do repouso e sem perdas, com U o módulo positivo da diferença de potencial aceleradora. A carga real do elétron é−e; o sinal do trabalho depende do sentido do percurso. U=150V dá K=150eV, não energia total150eV.

Neste laboratório adotamos E₀=511000eV arredondado para fins didáticos. Não é um valor exato do SI. h=6,62607015×10⁻³⁴J·s, c=299792458m/s e e=1,602176634×10⁻¹⁹C são valores definidos; a aritmética float usada no programa não é exata. O código deriva hc≈1239,841984eV·nm e a massa SI a partir do mesmo E₀, mantendo coerência entre as duas rotas. Não propaga incertezas de constantes ou de medições.

| K do elétron | λ_nr (nm) | λ_rel (nm) | (λ_nr−λ_rel)/λ_rel |
|---|---:|---:|---:|
| 150eV | 0,100137 | 0,100130 | 0,00734% |
| 100keV | 0,0038783 | 0,0037014 | 4,78% |

Casas adicionais ajudam a confrontar as fórmulas com os mesmos parâmetros arredondados; não representam precisão experimental. Para fóton, E=pc e λ=hc/E; com E=150eV dá8,266nm. Não se usa hc/K para elétron massivo.

## Qual aproximação atende à tolerância?

Com r=K/E₀>0, λ_nr/λ_rel=√(1+r/2). O erro relativo com denominador λ_rel é ε=√(1+r/2)−1. Como ambos os lados são positivos, ε≤τ equivale a r≤2[(1+τ)²−1]. Para τ=0,01, r≤0,0402 e K≤20542,2eV, cerca de20,5keV. Esse critério se refere somente a λ no modelo livre adotado. Não garante a mesma precisão para velocidade, energia ou outra aproximação física. A figura mostra o erro, não λ, e marca r=0 como limite aberto: λ não é finito quando K=0.

Para r pequeno, o código calcula ε por r/[2(√(1+r/2)+1)], evitando subtração de números quase iguais. A fronteira da tolerância usa2τ(2+τ).

## Exemplo geométrico separado

Duas aberturas finas coerentes e idênticas, separadas por d, incidência normal e campo distante: diferença de caminho aproximadamente dsenθ; fase2πdsenθ/λ. As direções construtivas satisfazem dsenθ=mλ. Com λ=0,10nm e d=0,20nm adotados exatamente neste exemplo, m=1 dá30°; m=3 não tem direção real. |mλ/d|=1 é o limite rasante de90°, não uma previsão de intensidade finita. O código retorna None para |mλ/d|>1, sem truncar o argumento de arcsen.

É geometria ideal de interferência, não lei de Bragg de planos cristalinos ou experimento realizável já validado. Coerência, interação com aberturas, difração de cada abertura e intensidades exigem outros modelos. Não se alterou a cobertura curricular de fenda dupla ou difração cristalina, que continuam lacunas.

## Verificação executável

Execute `python3 labs/debroglie-regimes/wavelength.py`. Seis testes: rota SI por p=γmv confrontada com cálculo em eV e reconstrução estável de K em16 energias; exemplos numéricos; escalas e comparação dos regimes; critério confrontado com desigualdade racional exata em três tolerâncias; direções permitidas/impossíveis e limites; contratos. Não valida adequação a uma experiência real.

Por limite didático e de representação float, o código aceita energias entre10⁻⁶eV e10⁹eV. Esse intervalo não é domínio físico universal da relação de Broglie nem garantia de validade de um elétron livre real. A fórmula não relativística pode ser calculada fora de seu regime para comparação, com erro explicitado; o programa não afirma que ela se torne fisicamente adequada.

## Fontes efetivamente consultadas

- [USP — CCM0222](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0222), reaberto em27/10/2026, ativação01/01/2025; item24 ondas de de Broglie. Versão efetivamente ministrada não comprovada.
- Nussenzveig, *Curso de Física Básica*, volume4, segunda edição identificada,2014/digital2018: §7.8 pp.224–226/PDF225–227, leitura textual parcial em27/10/2026 no acervo privado autorizado. Relação de Broglie, energia não relativística e discussão da evidência de difração. Sem nova inspeção visual, leitura integral, cópia de exercício ou distribuição do livro. Não se copiou o exemplo experimental histórico ou sua figura.
- [OpenStax University PhysicsVolume3 §6.5](https://openstax.org/books/university-physics-volume-3/pages/6-5-de-broglies-matter-waves), consulta parcial em27/10/2026: relações de momento/fase e expressão relativística em K,E₀. Apoio complementar; exemplos numéricos próprios, sem reprodução de exercícios.
- [NIST — Meet the Constants](https://www.nist.gov/si-redefinition/meet-constants), consulta parcial em27/10/2026 para os valores definidos de h,c,e. O valor adotado de E₀ é arredondamento didático compatível com0,511MeV; não se apresenta como constante exata. A busca NIST também retornou um valor mais preciso de energia de repouso, mas as tentativas de abrir a ficha e o cartaz2022 falharam: não são contadas como leitura integral ou usadas para alegar precisão superior neste laboratório.

Exposição, deduções de erro, gráfico, código e exercícios preparados para estas notas. Material assistido por IA, com revisão conceitual/didática pessoal pendente.

## Próxima revisão — vinte minutos

Reconstrua p²c²=K(K+2E₀), compare150eV com100keV e derive r≤0,0402. Explique por que dobrar p e dobrar K não são a mesma operação. Termine distinguindo uma escala de onda, um estado localizado e o exemplo geométrico de duas aberturas.
