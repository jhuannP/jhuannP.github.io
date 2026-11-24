# Simetria de translação num sistema de duas partículas

27/10/2026. Aula original em elaboração,13 seções/12 exercícios. Revisão pessoal de Jhuann pendente. Pré-requisitos: Newton, derivadas, momento, energia e centro de massa.

## Hipótese e prova

Duas partículas em1D interagem por U=k(x₁−x₂−ℓ₀)²/2. Não há suporte, atrito ou massa da mola. A translação ativa de ambas em a mantém a deformação; derivar a identidade em a dá F₁+F₂=0. Somar Newton dá dP/dt=0. O resultado diz respeito ao momento total, não aos dois momentos individuais. Não é prova geral de Noether.

O exemplo usa massas1 e3kg, k3N/m,ℓ₀2m, R₀0m,V1m/s,deformação inicial1m e velocidade relativa inicial zero. Massa reduzida3/4kg,ω2rad/s,P4kg·m/s,E7/2J. Separação sempre entre1 e3m; não há sobreposição das partículas. O comprimento ℓ₀ pertence ao modelo de potencial, sem geometria tridimensional ou massa própria do conector.

## Revisar em dois blocos

1. Derive a identidade da translação, as duas forças e dP/dt. Compare mover fisicamente só as partículas em uma armadilha fixa com mudar os rótulos das coordenadas.
2. Derive as inversas x₁=R+(m₂/M)(ℓ₀+r),x₂=R−(m₁/M)(ℓ₀+r). Abra K e mostre o cancelamento do termo cruzado. Verifique as velocidades em t=π/4s.

Execute `python3 labs/simetria-translacao/system.py` na pasta do protótipo. A rotina verifica invariância e forças por diferenças centrais exatas do potencial quadrático, decomposição cinética e solução analítica por Newton, balanços e diferenças finitas. Não integra uma EDO numericamente nem produz dados de experimento. A figura mostra duas configurações transladadas, sem apoios fixos.

O caso k(t) e a armadilha externa são discutidos para separar hipóteses, sem simulações desses casos. Momento constante não garante energia mecânica constante quando há controle externo dependente do tempo. Ampliar o sistema para incluir o controlador exige um modelo novo.

## Fontes e alcance

- [USP CCM0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0112), reaberto em27/10/2026. Objetivos incluem simetria e conservação. Ativação15/07/2024 posterior à turma; versão efetiva da turma não recuperada. Aprovação e material preparado não certificam domínio pessoal.
- Nussenzveig, Curso de Física Básica, vol.1,5ªed.,Blucher2013, quarta reimpressão2017: §8.1 pp.186–188/PDF187–189, reconferência textual parcial do acervo autorizado para momento total, forças externas e CM. Sem leitura integral, nova inspeção visual ou distribuição do PDF.
- [Feynman LecturesI §52–2](https://www.feynmanlectures.caltech.edu/I_52.html#Ch52-S2), consulta textual pública parcial de translações e relevância do ambiente, em27/10/2026. O corpo da seção foi recuperado apesar do aviso inicial de JavaScript. Sem transcrição de figuras ou exemplos. O exemplo de mola e sua demonstração são próprios.

Rotações, formulação variacional de Noether, campos com momento, relatividade, outras interações e validação experimental permanecem pendentes. O grupo curricular continua Parcial.
