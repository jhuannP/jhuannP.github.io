# Dipolo linear: potência por faixa angular

Rascunho original, 29/10/2026. Pré-requisitos: onda eletromagnética, Poynting, média temporal, integrais e coordenadas esféricas. Fonte principal privada autorizada: Nussenzveig, Curso de Física Básica vol.3, 2ª ed. revista/ampliada (2015; reimpressão2017; digital2018), §12.8, pp.269–273/PDF270–274. Consulta textual parcial com cabeçalhos conferidos nesta data; sem nova inspeção visual ou leitura integral. PDF privado não disponibilizado. Feynman II §21–4, https://www.feynmanlectures.caltech.edu/II_21.html , consulta parcial: tempo retardado, campos próximos/distantes e orientação. Não equivale à paginação da tradução. Figura, exemplos, contas angulares e código próprios.

Júpiter CCM0212, https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212 , reaberto29/10, ativação15/07/2025, item8(c,d). Versão ministrada não comprovada; histórico acadêmico preservado. Tentativa no portal alternativo falhou; página uspdigital forneceu o programa. Este recorte transforma a lacuna de dipolo em cobertura parcial, não cobre todos os campos ou eletromagnetismo.

Modelo clássico prescrito p(t)=p0 cos(ωt) z, vácuo, fonte pequena d<<λ, r>>λ e r>>d; velocidades internas não relativísticas. Fórmulas da aula são da ordem radiativa em1/r; campos próximos não calculados. A potência média exige energia fornecida à fonte, não oscilação perpétua sem custo. P'=a²w⁴P exige p0 eω tratados como controles independentes; não equivale a manter corrente de antena fixa.

O laboratório integra exatamente a densidade g(μ)=3(1−μ²)/4 para anéis completos em azimute, μ=cosθ, com limites racionais. Não resolve Maxwell, não calcula campo próximo, antena real ou emissão quântica. Fração isotrópica é comparação explícita, não hipótese do dipolo. Sem integração em subfaixas de azimute. Razões de potência são relativas e adimensionais; sem constantes SI arredondadas.

Da raiz: `python3 -m unittest discover -s labs/dipolo-angular -t .`; `python3 labs/dipolo-angular/angular.py`. Quatro testes: fixtures,231 intervalos com reflexão/partição/positividade, integração independente emθ por30.000pontos médios totais e escalas,contratos. Verificações numéricas não certificam toda função ou regime físico.

Revisão pessoal20min: reconstruir dΩ, obter5/32 no cone60° e11/16 no anel60–120°, explicar por que a isotropia daria1/4 e1/2. Campos completos, multipolos, radiação relativística, emissão atômica e validação experimental pendentes. Não é evidência de domínio pessoal ou resultado de pesquisa.
