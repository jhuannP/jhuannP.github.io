# Torque e equilíbrio de uma barra

Aula original `ef-torque-equilibrio`,10 seções/10 exercícios, rascunho para reforço. Pré-requisitos: forças, unidades e equações de primeiro grau. Python opcional; nenhum experimento realizado.

## Modelo e raciocínio

Torque no plano é xFᵧ−yFₓ relativo ao ponto escolhido, com anti-horário positivo. Seu módulo é força vezes braço perpendicular. Força resultante zero não garante torque zero. Para barra rígida inicialmente em repouso, exigimos balanços translacionais e rotacional. Reações em contatos simples por baixo devem ser não negativas; valores negativos questionam esse modelo.

Exemplo próprio L3m,P120N em d1m,W60N uniforme: R_B70N,R_A110N. Momentos à esquerda210−120−90=0; à direita−330+240+90=0. Não é divisão igual entre apoios. Extensão formal com carga além do apoio dá reação negativa, sem tratar o contato impossível como solução física.

## Fontes e limites

Nussenzveig, *Curso de Física Básica1*,5ª ed. (rosto/PDF4), §11.3 pp.281–282/PDF282–283, consulta textual parcial em27/10/2026: torque, componente perpendicular, braço. Sem leitura integral ou nova inspeção visual do PDF; não copiadas figuras ou exercícios.

[OpenStax CollegePhysics2e §9.2](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium), início sobre torque; [§9.3](https://openstax.org/books/college-physics-2e/pages/9-3-stability), início sobre estabilidade, parcialmente consultados. Não se adotam detalhes de aplicações humanas da fonte. Ângulo definido aqui entre vetor do ponto de referência à aplicação e força; sinal pela convenção explícita. Modelo/diagrama/balanços próprios. Sem auditoria BNCC/vestibular ou cálculo de deformação/capacidade real de estrutura.

## Verificação opcional

```sh
python3 labs/torque-apoios/balance.py
```

Quatro testes: exemplos/contato,300 casos de cargas com balanço de forças e momentos em quatro origens,625 configurações verificando mudança de origem e um binário, contratos. Frações exatas, sem simulação física. Os testes não provam rigidez/apoios reais. L é distância entre apoios; o peso W do modelo atua em L/2. A extensão fora do intervalo usa W=0. Com uma barra não uniforme ou com peso em outra posição, é preciso reformular o momento do peso.

Revisão em duas sessões de20min: desenhar braços e sinais; depois resolver reações e conferir pelo outro apoio. O balanço estático não demonstra estabilidade. Atrito, deformação,3D, dinâmica de rotações, revisão pessoal e uso com aluno pendentes.


## 27/10/2026 — torque e equilíbrio para reforço escolar

Nova `ef-torque-equilibrio`,10 seções/10 exercícios: braço perpendicular, sinal e torque planar; força/torque resultantes, gangorra, barra uniforme com dois apoios, reação negativa e estabilidade. Exemplo próprio L3m,P120N a1m,W60N no centro dá R_A110N/R_B70N; momentos pela outra extremidade fecham. Extensão formal com carga fora do apoio usa W0 e exige geometria compatível. Peso W do código atua em L/2; outra distribuição requer reformular. Sem experimento, deformação, cálculo de capacidade ou inferência de dados reais.

Fontes parciais em27/10/2026: Nussenzveig1,5ª ed. identificada no rosto/PDF4, §11.3 pp.281–282/PDF282–283, torque/componente perpendicular/braço, extração textual sem nova inspeção visual ou leitura integral. OpenStaxCollegePhysics2e§9.2 https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium e§9.3 https://openstax.org/books/college-physics-2e/pages/9-3-stability , inícios sobre torque e estabilidade. Diagrama, equações do exemplo e questões próprios; sem copiar aplicações humanas, figuras ou exercícios. Sem auditoria de matriz escolar.

Quatro testes em `labs/torque-apoios/balance.py`: exemplos/contato,300 arranjos de cargas com balanços em quatro origens,625 identidades de mudança de origem e binário, contratos. Frações exatas; verificação do modelo, não de estrutura real.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou90 e aceitou110 para apoio esquerdo; documento390/390px, console sem erros observados. Figura inicialmente faltava ponta de uma seta, corrigida e reinspecionada em `torque-apoios-mobile.jpg`; setas não afirmam escala comum de força. Viewport restaurada. Windows real, leitor de tela, revisão pessoal e uso com aluno pendentes.

Física escolar17 aulas/200 exercícios, sem introduções curtas e sem cobertura integral certificada. Global51 trilhas/577 aulas/5286 exercícios,142 introduções curtas. Próxima ação:duas sessões de20min para braços/sinais e reações com conferência pelo outro apoio. Próxima elaboração global:conferir a introdução de integrais trigonométricas em Cálculo2, após localizar fonte, mantendo alternância. Saldo semanal antes/depois66%;parada operacional65% preservada.
