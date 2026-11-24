# Continuidade e Bernoulli com alturas distintas

Modelo próprio: escoamento estacionário incompressível ideal, mesmo tubo de corrente, valores aproximadamente uniformes em cada seção. Sem perdas ou bomba; z cresce para cima. Continuidade geral usa fluxo de massa e, para densidade constante, Q=A v com velocidade média normal. Usar essa média diretamente na energia exige a redução uniforme adotada aqui.

Exemplo SI: A1=4×10⁻⁴ m², A2=10⁻⁴ m², v1=1 m/s, ρ=1000 kg/m³, g=10 m/s² didático, z1=0, z2=1 m, p1 absoluta=200000 Pa. Q=4×10⁻⁴ m³/s=0,4 L/s; v2=4 m/s. Δp cinética=−7500 Pa e gravitacional=−10000 Pa; p2=182500 Pa. B=p+ρv²/2+ρgz vale 200500 Pa em ambas as seções. Trabalho de pressão por m³: 17500 J, igual a 7500 J de aumento cinético mais 10000 J de aumento potencial.

A mesma referência deve ser usada para p1 e p2. Subtrair pressão atmosférica fictícia 100000 Pa dá manométricas 100000 e 82500 Pa, com mesma diferença. Manométrica negativa não significa absoluta negativa. Uma previsão absoluta fisicamente incompatível pede revisão das hipóteses; não se calcula cavitação. Áreas iguais e descida de um metro dão mesma rapidez e aumento de 10000 Pa. Horizontalidade recupera só a parcela cinética; repouso recupera o limite hidrostático.

Na raiz do site:

    python3 -m labs.bernoulli-altura.exact
    python3 -m unittest discover -s labs/bernoulli-altura -t .

Inteiros/Fraction em SI, sem float ou bool. Áreas, densidade e g positivos; rapidez inicial não negativa. Pressões e alturas aceitam referências do chamador; o código não descobre se um número está em SI ou é pressão absoluta. Cinco testes verificam referência, trabalho por volume, continuidade e inversão em 81 configurações racionais, mudanças de referência, limites estático/horizontal/descendente e contratos. Nenhum dado experimental ou resultado da IC usado.

Aula f2-escoamento ampliada para onze seções/doze exercícios. Exemplo, Python, desafio e painel horizontais anteriores preservados. Figura original tubo.svg não está em escala. Notas preparadas com apoio de IA para revisão pessoal. Próxima revisão: reconstruir Δp e explicar por que uma descida pode aumentar pressão sem diminuir rapidez. Viscosidade, perfis, bombas, transientes, compressibilidade e problemas integradores permanecem pendentes; o grupo curricular segue parcial.

Fontes consultadas parcialmente por extração textual em 22/10/2026: Nussenzveig, Curso de Física Básica vol.2, 5ª ed., Blucher 2014 (reimpressão 2017), §2.2 p.32/PDF33 e início de §2.4 pp.35–36/PDF36–37. Página 38/PDF39 consultada para aplicações/limites; não se desenvolveu Torricelli. Cabeçalhos confirmam as páginas impressas, sem nova conferência visual. [OpenStax University Physics vol.1 §14.6](https://openstax.org/books/university-physics-volume-1/pages/14-6-bernoullis-equation) como apoio parcial. Contas, figura e exercícios próprios; nenhum livro privado reproduzido.

Verificação: cinco testes novos e 13 de catálogo aprovados; 544 estruturas MathML conferidas. No navegador em 390 px, figura e fórmula legíveis; questão de Δp rejeitou +17500 e aceitou −17500. Largura igual à tela e nenhum erro de console observado. Prévia: bernoulli-altura-mobile.jpg. Não houve revalidação integral da suíte global nem do painel horizontal, preservado. Catálogo: 501 aulas/3148 exercícios em rascunho. Saldo semanal após bloco: 92%; parada em 65%.
