# Orbitais atômicos, estados e probabilidade

27/10/2026. Notas de aula originais com apoio de IA, em rascunho; revisão pessoal de Jhuann pendente. Nova aula com15 seções/12 exercícios, exemplo de contagem e figura analítica original. Bloco conceitual e de integração, sem código Python necessário ou experimento realizado.

## Modelo e conceitos

O orbital é uma função de onda espacial, não trajetória. No modelo hidrogenoide central não relativístico, a base estacionária é rotulada por n inteiro positivo, ℓ=0,…,n−1 e mℓ=−ℓ,…,+ℓ. O spin acrescenta ms=±1/2. No modelo de ocupação por spin-orbitais, Pauli impede duplicar o conjunto dos quatro números; cada orbital espacial admite no máximo dois elétrons com projeções opostas. Spin não é rotação de uma esfera material.

Subcamada:2ℓ+1 orbitais; camada:Σ(2ℓ+1)=Σ[(ℓ+1)²−ℓ²]=n² orbitais, capacidade máxima2n². Em n=3, há3s, 3p, 3d, total 1+3+5=9 orbitais/18 elétrons máximos. Isso não especifica ocupação ou ordem energética em átomos reais. 2d não existe; (3,2,−2,+1/2) é permitido, (3,3,0,+1/2) não é.

Na convenção usual, pz corresponde a mℓ=0; px e py são combinações de mℓ=±1. Bases reais e complexas descrevem o mesmo subespaço; não atribuir a px, py automaticamente os rótulos−1,+1. No Coulomb ideal de um elétron, energia depende de n; não generalizar degenerescência de subcamadas a átomos polieletrônicos ou modelos com correções/campos. Nós, configurações, Hund, equação de Schrödinger completa e funções angulares detalhadas ainda pendentes.

## Densidade local e radial 1s

Para o hidrogênio 1s ideal, ψ=(πa0³)⁻¹ᐟ²exp(−r/a0), com a0 uma escala positiva de comprimento. Densidade por volume ρ=|ψ|²=exp(−2r/a0)/(πa0³), em unidades de comprimento⁻³. Probabilidade em região=∫ρdV; um ponto isolado tem massa zero.

Pela simetria esférica, a casca de espessura dr tem volume4πr²dr; portanto p(r)=4πr²ρ(r)=4r²exp(−2r/a0)/a0³, em unidades de comprimento⁻¹. A densidade local é máxima no núcleo, mas a densidade radial vale zero ali e tem máximo em r=a0. Isso não coloca o elétron numa órbita circular.

Com s=r/a0, p(r)dr=4s²exp(−2s)ds. Integração por partes duas vezes:

∫4s²exp(−2s)ds=−exp(−2s)(2s²+2s+1)+constante.

A expressão entre0 e∞ vale1, normalizando a distribuição. Derivada8s(1−s)exp(−2s), positiva até 1 e negativa depois. Acumulada F(R)=1−exp(−2S)(1+2S+2S²), S=R/a0. Logo P(r≤a0)=1−5exp(−2)≈0,323323584, enquanto P(r=a0)=0. As curvas adimensionais da figura são πa0³ρ=exp(−2s) e a0p=4s²exp(−2s), com escalas verticais diferentes. Integração, figura e comparação originais, sem transcrição dos livros.

## Fontes e alcance

Atkins, Jones e Laverman, Princípios de Química,7ª ed., Bookman, 2018. Tópico1D: §§1D.2–1D.3 pp.31–34/PDF163–166 e §§1D.5–1D.6 pp.38–39/PDF170–171 consultados parcialmente em 27/10/2026; p.33/PDF165 inspecionada visualmente. Página do PDF contada desde1. Sem leitura integral; partes da extração são equações em imagem. Exemplar privado localizado e identificado anteriormente, sem redistribuição. Edição difere da 3ª indicada no programa de CCM0114.

[USP — CCM0114](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114), reaberto27/10/2026: estrutura eletrônica inclui orbitais/representação e configurações; ativação15/07/2024 posterior à turma2023. Versão da turma não recuperada. Aprovação2023/2 vem do panorama acadêmico existente, sem novo exame do histórico neste bloco. Conteúdo preparado não comprova aprendizagem pessoal.

[OpenStax Chemistry2e §6.3](https://openstax.org/books/chemistry-2e/pages/6-3-development-of-quantum-theory), consulta parcial27/10/2026 para fundamentos, números quânticos e Pauli. Apoio complementar. A aula evita tratar ilustrações de círculos ou analogias de spin como movimentos materiais literais.

## Exercícios e revisão

Respostas dos12 itens:2;5;10;9; conjunto(3,2,−2,+1/2); não repetir ms no mesmo orbital; combinações lineares; fator4πr²; máximo em r/a0=1; aproximadamente0,3233236; zero para raio isolado; máximo da densidade por distância. Dicas e explicações completas na aula.

Duas revisões propostas de 20min após a aula de espectros: listar estados e justificar capacidades; depois derivar o fator de casca e reconstruir normalização, máximo e massa da esfera. Dúvidas e avaliação pessoal deixadas em branco. Não há experimento, estimativa de dados, resolução de configuração polieletrônica ou domínio pessoal certificados.

Conferência da entrega:14 testes de catálogo e722 estruturas MathML aprovados. Integrais radiais por Simpson comparadas à acumulada em quatro raios, erro<1e−11. Navegador390px: exercício12 rejeitou órbita e aceitou máximo de densidade radial pelo Enter; figura inspecionada, sem transbordamento horizontal e sem erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
