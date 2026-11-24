# Comprimento, simultaneidade e eventos

22/10/2026. Rascunho didático original assistido porIA, pendente de revisão pessoal. Não são dados observacionais ou comprovação de pesquisa de Jhuann.

## Modelo e convenção

Barra em repouso em S′:extremidades x′/L₀=0e1. Movimento longitudinal com β=v/c em S, referenciais inerciais/eixos paralelos. L₀0,5..4m, β−0,8..0,8. Desenho usa τ=ct/L₀ e u=x/L₀, com escalas iguais. Boost para S′:(τ′,u′)=γ(τ−βu,u−βτ); inversa troca o sinal deβ.

Par0: A=(0,0),B=(0,1/γ) em S; em S′,B′=(−β,1). Mede L=L₀/γ em S. Par1: A′=(0,0),B′=(0,1); em S,B=(γβ,γ). Esse segundo par mede L₀ em S′, mas sua separação espacial γL₀ não é comprimento medido em S quando β≠0. As linhas de universo u=βτ e u=βτ+1/γ delimitam as extremidades.

O intervalo(cΔt)²−(Δx)² é conservado para o mesmo par. Trocar de par pode mudar esse valor; não se usa essa troca como teste de invariância. O painel marca a simultaneidade pela construção do par, sem classificar ruído de ponto flutuante como diferença temporal física. Tabela e figura usam os mesmos eventos.

No padrãoβ0,6/L₀2m:γ1,25,L1,6m. Par0 em S:(cΔt,Δx)=(0;1,6)m; em S′:(−1,2;2)m. Par1 em S:(1,5;2,5)m; em S′:(0;2)m. Invariantes−2,56m² e−4m² correspondem a pares distintos.

Não há fotografia, emissão/recepção de luz, perspectiva, deformação, aceleração, tensão, mudança de extensão própria ou gravitação. Alterar L₀ muda a escala física, não a forma normalizada. β negativo inverte sinais temporais sem mudar L. β0 faz coincidir os pares; β±1 não pertence ao domínio.

## Fonte consultada parcialmente

Nussenzveig, *Curso de Física Básica*, volumeIV, segunda edição2014, segunda reimpressão2017 e edição digital2018, exemplar privado autorizado. §6.5(a):pp.160–161/PDF161–162 lidas; p.160 visualmente inspecionada. Primeiro parágrafo de p.162/PDF163 consultado para distinguir fotografia e corte simultâneo. Extração incluiu páginas vizinhas, que não sustentam cobertura de outros tópicos. Cabeçalhos no corpo conferidos, sem supor paginação a partir do sumário.

Modelo, redação, exercícios e diagramas próprios. Não copiadas figuras, enunciados ou páginas do livro. Nenhum PDF/imagem da fonte foi incorporado ao site. A consulta não conclui efeitos cinemáticos, aspectos visuais, relatividade ou a disciplina.

## Verificação

Na raiz:

```sh
python3 labs/medida-comprimento/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:30casos exatos com frações, resolvendo interseção entre linha de universo e corte;136estados de boost/inversa/invariante/extremidades; escala/sinal/repouso e diferença entre pares; domínio.30referências Python/JS com coordenadas dos eventos, comprimentos, simultaneidade e invariantes. Tolerâncias de cálculo não substituem as identidades derivadas na aula ou revisão conceitual.

## Composição e interação

Tese visual: linhas de universo fixam o objeto, enquanto o corte de simultaneidade muda os eventos da medida. Plano: definir medida→derivar relação→comparar pares→conferir invariante→praticar. Controles: β inclina linhas; par troca o corte; L₀ muda valores físicos mantendo o desenho normalizado. Sem animação de uma barra mecanicamente encolhendo. Eixos e tabela explicitam unidades; janela quadrada respeita a escala das duas coordenadas.

## Pendências

Revisão de Jhuann; origens/testes, situações de medição mais gerais e fundamentos quânticos. Fotografia, aceleração e relatividade geral permanecem fora deste modelo. Nenhum grupo completo.
