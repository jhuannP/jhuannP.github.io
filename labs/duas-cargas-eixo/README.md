# Duas cargas no eixo: campo, potencial e singularidades

22/10/2026. Rascunho original para revisão de Jhuann. Valores e posições didáticos; não são dados da IC ou de experimento.

## Fontes

[Feynman II, capítulo 4](https://www.feynmanlectures.caltech.edu/II_04.html), consultas parciais aos trechos 4–2 e 4–3, e [capítulo 6, 6–2](https://www.feynmanlectures.caltech.edu/II_06.html), consultado parcialmente em 22/10/2026. Coulomb, soma de contribuições, potencial e par oposto apoiam o recorte. A leitura é da edição oficial online em inglês, sem transferir paginação à tradução privada. Não se afirma leitura integral; não foram copiados desenhos, exemplos, exercícios ou código das referências. k=9×10⁹ é uma aproximação didática em SI, sem usar a antiga definição histórica da permissividade como afirmação atual.

## Modelo e contrato

q1=+1 nC em −1 m e q2=s×1 nC em +1 m, s=−1 ou +1. Fontes fixas, vácuo e observação axial. Com k arredondado, k×1 nC=9 N m²/C. Para cada fonte: Ex=9sign(x−xfonte)/|x−xfonte|² e V=9sign/|x−xfonte|. O código usa deslocamento/|deslocamento|³ para Ex, sem perder direção. Potencial com referência no infinito.

No centro, cargas iguais: Ex=0, V=18 V; cargas opostas: Ex=18 N/C, V=0. Em x=2 m no par oposto: Ex=−8 N/C, V=−6 V. A sonda negativa inverte a força em relação ao campo; não muda o campo calculado das fontes fixas.

Python `axial` aceita x int/Fraction em qualquer posição axial racional e s inteiro −1 ou 1, rejeitando bool e float. Pontos nas fontes devolvem None para os totais e para a contribuição singular; a contribuição da outra fonte permanece finita. O painel JS restringe x a quartos entre −3 e 3 m e usa os dois sinais. Não há regularização arbitrária, movimento de fontes ou solução de condutores.

O par oposto tem carga total zero e momento dipolar para −x, módulo 2×10⁻⁹ C m. O cálculo do painel é exato no modelo axial de duas fontes e não usa aproximação de dipolo distante. Campo geral, limites quantitativos da aproximação e radiação permanecem pendentes.

## Ler a figura

Fontes no eixo e observação num círculo acima dele. Apenas a coordenada horizontal tem significado espacial, em escala. Setas de comprimento fixo mostram sentido do campo, sem escala de módulo; não aparecem em campo zero ou singularidade. A tabela fornece cada contribuição e o total com unidades. Não se desenham linhas de campo ou trajetórias de partículas.

## Executar e verificar

Na raiz do protótipo:

```sh
python3 labs/duas-cargas-eixo/experiment.py
python3 -m unittest discover -s labs/duas-cargas-eixo -t .
```

Quatro testes: campo confrontado com derivada centrada independente de V em pontos regulares; paridades por reflexão e casos de referência; integral de trabalho em três intervalos que não atravessam fontes, para os dois sinais; singularidades e contratos. Derivada e integral usam aproximação numérica controlada, não são prova exata por si só. JSON com 50 estados: 25 posições×2 sinais, incluindo quatro singularidades, produzidos com Fraction e confrontados com JS. Sem validação experimental ou afirmação de cobertura tridimensional.

Aula 14 seções/12 exercícios, preservando os anteriores e a demonstração pontual original como apoio adicional. Próxima revisão: explicar cancelamento vetorial versus escalar e identificar o domínio antes de calcular. Restam geometrias gerais, condutores, dipolo distante, autoenergia e radiação.


## Verificação final e continuidade

773 testes Python aprovados; suíte JavaScript 281 demonstrações/843 cenários básicos e referências adicionais aprovada; 455 estruturas MathML conferidas. Navegador: alternância de sinais no centro produziu (E,V)=(0,18) e (18,0) nas unidades declaradas; ponto x=1 m marcou singularidade; exercício de campo zero aceitou 0. Tela 390 px sem transbordamento horizontal, sinais das fontes legíveis e sem erros de console observados; viewport restaurado. Prévia `duas-cargas-eixo-mobile.jpg`.

Física III 14 aulas/75 exercícios: cinco recortes desenvolvidos e nove introduções. Catálogo 487 aulas/2567 exercícios. Nenhum grupo completo, revisão pessoal pendente. Próxima revisão: E versus V e domínio das fontes; próxima alternância global: análise numérica. Saldo semanal informado após o bloco: 100%; parada em 65%.
