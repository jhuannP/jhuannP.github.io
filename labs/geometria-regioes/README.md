# Da estrutura de Lewis à geometria molecular

Material original preparado com apoio de IA em 28/10/2026. Revisão pessoal de Jhuann pendente. O laboratório é de contagem e álgebra vetorial, sem otimização molecular, cálculo de densidade eletrônica ou experimento.

## Recorte e sequência

Comece por uma estrutura de Lewis e conte regiões de ligação e pares isolados no átomo central. Uma ligação dupla ou tripla ocupa uma região para classificar a geometria básica; isso não significa distribuição ou intensidade de repulsão idênticas às de uma ligação simples. Dois pares isolados são duas regiões, não uma única região “sem átomo”.

No recorte de duas a quatro regiões: AX₂ linear; AX₃ trigonal plana; AX₄ tetraédrica; AX₂E angular com arranjo eletrônico trigonal plano; AX₃E piramidal trigonal com arranjo eletrônico tetraédrico; AX₂E₂ angular com arranjo eletrônico tetraédrico. A designa o centro, X um átomo ligado e E um par isolado. Não é uma tabela geral para radicais, metais de transição ou cinco/seis regiões.

CO₂: 16 elétrons de valência; O=C=O, sem par isolado no C. Duas regiões, linear. CH₄: 8 elétrons, quatro ligações, sem par isolado no C; quatro regiões, tetraédrica. NH₃: 8 elétrons, três ligações e um par isolado no N; arranjo eletrônico tetraédrico, forma piramidal. H₂O: 8 elétrons, duas ligações e dois pares isolados no O; arranjo eletrônico tetraédrico, forma angular. Nitrato/ressonância já tem aula de Lewis e fornece exemplo de três regiões no N; não se faz aqui soma de dipolos de um íon carregado.

## Ângulos e simetria

Um tetraedro regular tem direções proporcionais a (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1). Cada vetor tem norma √3; produtos entre vetores distintos valem −1, logo cosθ=−1/3 e θ≈109,47°. É um cálculo geométrico ideal. Não é o ângulo de toda molécula com quatro regiões.

Atkins cita H₂O≈104,5° e NH₃≈107° em p.104. São valores apresentados pelo livro, não resultados de `classify` ou medidas de Jhuann. VSEPR racionaliza formas e tendências, sem fornecer sozinho o número exato desses ângulos. Não se presume equivalência do recorte a teoria de orbitais ou hibridação como mecanismo literal.

Ligações polares não obrigam uma molécula neutra a ter dipolo permanente: contribuições equivalentes podem se cancelar por simetria. CO₂ linear é exemplo; H₂O angular não tem o mesmo cancelamento. O laboratório usa vetores adimensionais de comprimentos iguais dentro de cada arranjo, com pesos esquemáticos. Não calcula dipolos de ligação ou momento molecular em C·m/D, não usa cargas parciais medidas nem transforma cada par isolado em uma seta de dipolo. A soma de todos os vetores do tetraedro é zero; dobrar um peso deixa um vetor residual. Inverter globalmente a convenção de setas mantém a conclusão de nulidade.

## Executar

```sh
python3 geometry.py
python3 -m unittest test_geometry.py
```

Python padrão, sem dependências. `classify` recebe contagens já obtidas de Lewis, não uma fórmula química. Combinações não cadastradas são rejeitadas como fora do recorte, sem alegar impossibilidade química. `weighted_sum` e `dot` operam sobre vetores racionais tridimensionais; não são simulação da distribuição eletrônica. O exemplo angular de 90° do teste é sintético, não a geometria da água.

Quatro testes: normas/produtos de Gram e cancelamento dos três arranjos; alterar pesos/remover direções e caso angular; 48 transformações ortogonais por permutação de eixos e troca de sinais; contagens e contratos. Esses invariantes verificam a álgebra, sem validar um modelo quantitativo de dipolo real.

## Fonte, edição e limites

Atkins/Jones/Laverman, *Princípios de Química*, 7ª ed., Bookman 2018, exemplar autorizado. Consulta textual e inspeção visual parciais em 28/10/2026: Tópico 2E, p.104/PDF236 (ângulos citados no parágrafo inicial), p.107/PDF239 (regiões múltiplas, forma e notação), p.112/PDF244 (pares isolados e polaridade). Consulta parcial, sem copiar figuras, tabela de dipolos ou exercícios. Edição difere da 3ª citada no programa CCM0114; versão ministrada em 2023 não comprovada. Programa oficial não reaberto neste bloco. Os exemplos de contagem e os esquemas são próprios; PDF privado fora do site.

Próximo passo pessoal: reconstruir os três casos com oito elétrons, distinguir as duas geometrias da água e deduzir cosθ=−1/3; depois explicar por que a soma de vetores esquemáticos não fornece o dipolo da água. Faltam cinco/seis regiões, distorções gerais, teoria da ligação, orbitais moleculares, interações/sólidos e revisão pessoal.
