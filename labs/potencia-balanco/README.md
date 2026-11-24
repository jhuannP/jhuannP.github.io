# Potência e balanço de energia

Modelos originais com forças prescritas, produzidos com apoio de IA para estudo e revisão pessoal. Não são medições de um motor ou resultados de pesquisa.

## Hipóteses e unidades

Partícula clássica de massa constante, referenciais inerciais, unidades SI: kg, m, s, N, J e W. P=F·v, com velocidade e trabalho no mesmo referencial. O trabalho de cada força soma para a variação da energia cinética; a potência de uma força isolada não precisa ser dK/dt.

O código aceita apenas int/Fraction, sem bool/float, para manter as contas exatas. Vetores têm entre uma e três componentes. No carrinho, massa>0, velocidade inicial≥0 e tração≥resistência≥0, t≥0. Essas restrições mantêm movimento não negativo no referencial da pista. O parâmetro boost é a velocidade de outro observador; mudar o observador não altera a lei física da resistência. Não usamos o sinal da nova velocidade para redefinir a força.

## Carrinho prescrito

m=2 kg, v₀=1 m/s, tração +6 N, resistência −2 N e duração 2 s, sem trabalho de peso/normal. Resultante 4 N, aceleração 2 m/s², velocidade final 5 m/s e deslocamento 6 m.

| Grandeza | Tração | Resistência | Resultante |
|---|---:|---:|---:|
| Potência inicial (W) | 6 | −2 | 4 |
| Potência final (W) | 30 | −10 | 20 |
| Trabalho (J) | 36 | −12 | 24 |
| Potência média (W) | 18 | −6 | 12 |

A energia cinética cresce de 1 a 25 J. A área de P_net(t)=4+8t corresponde aos 24 J; a potência final não deve ser confundida com a média.

Para um observador com u=+2 m/s em relação à pista, a velocidade vai de −1 a +3 m/s, e o deslocamento entre os mesmos instantes é 2 m. Trabalhos: 12−4=8 J; K′ vai de 1 a 9 J. P′=P−F·u e ΔK′=ΔK−u·Δp verificam a consistência. O trabalho resistente sobre a partícula, sozinho, não permite chamar −W_res de calor em qualquer referencial; seria preciso ampliar o sistema, incluindo pista e transferências.

## Modelo não linear separado

m=2 kg e v(t)=1+t² m/s, para t expresso em segundos. A força 4t N produz P=4t+4t³ W. De 0 a 1 s, o trabalho é 3 J e a média 3 W. A potência no instante médio é 2,5 W: em geral, ela não substitui a integral. Os coeficientes polinomiais carregam as unidades SI implícitas indicadas; não se trata de somar grandezas de dimensões diferentes.

## Reprodução e referências independentes

Da raiz:

```sh
python3 labs/potencia-balanco/power.py
python3 -B -m unittest discover -s labs/potencia-balanco -t .
```

Seis testes: marcos literais; trinta combinações de modelo/duração integradas por trapézio, comparadas com trabalhos e diferença cinética; dezesseis combinações de boost/tempo para os balanços galileanos; quatro integrais cúbicas por Simpson, além do contraponto no ponto médio; geometria vetorial; contratos. Trapézio e Simpson são referências de integração independentes das fórmulas de trabalho retornadas. São exatos nesses polinômios, não métodos gerais de simulação certificados.

Uma primeira invocação do teste cúbico produziu um float por t/2 para t inteiro. A chamada foi corrigida para Fraction(t)/2, preservando o contrato de aritmética exata; os seis testes passaram depois da correção.

## Fontes — 29/10/2026

[Júpiter 4302111, versão 1](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=4302111&verdis=1), aberto diretamente: ativação 01/01/2015 e desativação 31/12/2025. Potência consta no conteúdo programático. Vigência inclui o período cursado, mas não comprova execução integral pela turma. A ementa contém apenas “ok”; o mapa usa o programa.

Young/Freedman, *Física I — Mecânica*, Sears e Zemansky, 14ª edição brasileira, Pearson 2016, reconferida na CIP e copyright. A marca de produção em 2015 não foi tomada como ano bibliográfico. §6.4, recortes pp.209–210/PDF228–229 para definições, unidades e produto escalar; p.210/PDF229 visualmente inspecionada. Exemplo, figura e contrapontos próprios. Não foram reproduzidas figuras, aplicações biológicas, tabelas ou exercícios do livro; PDF privado não servido.

[OpenStax, University Physics I §7.4](https://openstax.org/books/university-physics-volume-1/pages/7-4-power): consulta parcial nas definições de taxa, integral e produto escalar, sem dados, exemplos ou figuras incorporados. Transformação galileana e modelos prescritos foram desenvolvidos para este laboratório.

Motores elétricos, eficiência real, corpos extensos, contato real, deformação e experimentos continuam fora do recorte. Revisão pessoal pendente; a existência da página não certifica domínio nem encerra o programa da disciplina.
