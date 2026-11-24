# Velocidades e referenciais

Rascunho original para revisão. Execute `python3 velocities.py` sem dependências adicionais. Entradas são números exatos `int` ou `Fraction`, representando velocidades divididas por c. Floats são recusados neste laboratório, inclusive os números escritos como0.5; use Fraction(1,2).

## Convenção e dedução

S′ se move em S a v no eixo x. Escreva b=v/c. Das transformações passivas x′=γ(x−vt) e t′=γ(t−vx/c²), tomando a razão dos diferenciais ao longo da mesma trajetória, obtemos a′=(a−b)/(1−ab), onde a=u/c. A inversa é a=(a′+b)/(1+a′b). Velocidades com sinal não são módulos. O exemplo a′=b=1/2 retorna4/5; a=3/5,b=4/5 retorna−5/13.

A identidade 1−a′²=(1−a²)(1−b²)/(1−ab)² prova que uma trajetória material continua subluminal. Para a=±1, a′=±1. Os referenciais têm sempre |b|<1: não se constrói referencial de repouso da luz.

Em S, velocidades+4c/5 e−4c/5 podem dar taxa de aproximação8c/5. A velocidade do segundo no repouso do primeiro é−40c/41. A primeira taxa compara posições simultâneas em S; não é velocidade de um sinal medida no repouso de um dos corpos.

Para a forma inversa e a≠0, a soma galileana a_G=a′+b tem erro relativo exatamente|a′b|, usando a relativística como referência. Se a′+b=0, o erro absoluto é zero e o relativo não é definido. Isso é análise longitudinal da aproximação, sem abranger erros float, componentes transversais ou dados reais.

## Extensão plana

D=1−baₓ; aₓ′=(aₓ−b)/D e aᵧ′=aᵧ/(γD). O y não muda, mas o tempo muda. A identidade

1−aₓ′²−aᵧ′² = (1−b²)(1−aₓ²−aᵧ²)/D²

preserva o disco causal. Para (0,3/5),b=3/5, a resposta é(−3/5,12/25); norma²=369/625. Para luz inicialmente(0,1), resulta(−3/5,4/5), com norma1. A direção muda, a rapidez não.

As fórmulas físicas valem para qualquer boost subluminal. **Restrição computacional:** a versão plana deste laboratório exige γ racional para manter Fraction em todas as operações. Usa raiz inteira de numerador/denominador e recusa, por exemplo, b=1/2. Isso não é limitação da relatividade. Boosts±3/5,±4/5,±5/13 e zero permitem os testes exatos. Sem generalizar para todos os boosts ou alegar precisão de um solver geral.

## Fontes e alcance da leitura

- Nussenzveig, Curso de Física Básica vol.4,2ª edição revista2014,digital2018,§6.6 pp.164–165/PDF165–166. Extração textual parcial reconferida em27/10/2026 a partir do título em p.164; exemplo de múons da seção anterior não usado. Transformações longitudinais/transversais e identidade causal. Algumas expressões têm extração imperfeita; álgebra própria conferida separadamente. Sem leitura integral, nova inspeção visual ou distribuição do exemplar privado.
- [OpenStax, UniversityPhysicsVol3,§5.6](https://openstax.org/books/university-physics-volume-3/pages/5-6-relativistic-velocity-transformation): recorte da dedução por incrementos e componentes, parcialmente consultado em27/10/2026.
- [Júpiter CCM0222](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0222), reaberto em27/10/2026, ativação01/01/2025; itens7–8 de Lorentz/velocidade limite. Não comprova a versão ministrada ou domínio pessoal.

Figuras, parâmetros, deduções, exercícios e código são originais. A figura compara vetores de velocidade; não trajetórias, fotografias ou fontes astrofísicas. Não cobrimos boosts não colineares, aceleração/forças, instrumentos, gravitação ou dados observacionais.

## Verificações

Cinco testes: identidade causal e inversa em357 combinações colineares, incluindo luz;567 estados planos/boosts confrontados com matriz de Lorentz aplicada a deslocamentos antes de calcular velocidades, inversa e identidade de norma;125 composições triplas colineares;81 casos de erro da aproximação galileana, exemplos e contratos. As provas algébricas na aula completam o que uma grade finita de testes não demonstra. Revisão pessoal pendente.
