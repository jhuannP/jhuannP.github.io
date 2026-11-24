# Potencial, referência e trabalho de uma sonda

Material original em rascunho para revisão de Jhuann; não é evidência de domínio pessoal ou resultado da IC.

Fontes esféricas prescritas no vácuo, sem resposta à sonda: esfera volumétrica uniforme ou casca superficial, raio R e carga Q. Em SI, k=1/(4πε₀). Com zero no infinito, exterior V₀=kQ/r; interior da esfera V₀=kQ(3R²−r²)/(2R³); interior da casca V₀=kQ/R. Na casca não nula, V é contínuo e Eᵣ só tem limites na camada. Não representa camada dipolar.

Painel: R=ε₀=1, como em Gauss. Gráfico mostra 4πV; tabela V, Eᵣ e ΔU sem esse fator. O parâmetro `shift` é **4πC**, de modo que V=V₀+shift/(4π). A fixo em r=2; B varia. ΔV é calculado antes de somar a referência, evitando cancelamento desnecessário. q=±1 é sinal de uma sonda sem retroação, e q=0 é o caso neutro. Não se integra trajetória ou acessibilidade a partir de K inicial.

ΔU=qΔV e Wₑₗ=−ΔU. Sob trabalho apenas elétrico, ΔK=Wₑₗ; no transporte quase estático compensado por força externa, ΔK≈0 e Wexterno=ΔU. Não confundir energia de uma sonda com autoenergia da distribuição.

## Reprodução

Na raiz do protótipo:

```sh
python3 labs/potencial-esferico/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes novos verificam: gradiente numérico e derivadas de um lado; integral angular independente de Coulomb para casca, incluindo superfície por substituição u=1−t²; integral de camadas para esfera; trabalho por integração radial por trechos; invariância à referência, sinal da sonda e domínios. A referência angular usa Simpson com 2000 painéis; não é estimativa universal de erro. São 36 comparações de gradiente fora da camada, 21 quadraturas angulares e 10 integrais de camadas, além das combinações de referência/trabalho. `reference.json` guarda 30 configurações Python para comparação com o modelo JavaScript.

## Fontes consultadas parcialmente em 16/10/2026

- [Feynman II, 4–3/4–4](https://www.feynmanlectures.caltech.edu/II_04.html): definição integral, referência e gradiente. Edição oficial online; não se presume a paginação da tradução privada.
- [OpenStax II, 7.2](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference): definições de potencial/diferença e trabalho.
- [OpenStax II, 7.3](https://openstax.org/books/university-physics-volume-2/pages/7-3-calculations-of-electric-potential): integral de Coulomb para distribuições e limite da referência no infinito para linha infinita.
- [OpenStax II, 7.4](https://openstax.org/books/university-physics-volume-2/pages/7-4-determining-field-from-potential): gradiente e simetria radial.

As expressões por partes de esfera/casca foram derivadas dos campos da aula anterior e verificadas por integrais; sem transcrição de exemplos, exercícios ou figuras dessas fontes. Não se declarou leitura integral dos capítulos nem de livros do acervo. Pendentes: dipolos, condutores, geometrias gerais, energia de montagem e revisão pessoal.
