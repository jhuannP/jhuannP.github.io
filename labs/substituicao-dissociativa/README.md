# Substituição dissociativa: recaptura e aproximação

Rascunho original. Execute `python3 substitution.py`,sem dependências adicionais. Parâmetros e espécies são hipotéticos, sem ajuste, medição ou identificação de complexo real.

## Esquema e unidades

Cₓ→I+X com k₁; I+X→Cₓ com k₋₁; I+Y→Cᵧ com k₂. A primeira saída forma um intermediário de coordenação menor. X e Y livres são fixados em reservatórios; o produto não retorna na janela modelada. a=k₁, b=k₋₁[X], c=k₂[Y],em s⁻¹. k₋₁ e k₂ estão em M⁻¹s⁻¹. Temperatura, solvente e demais condições fixos.

As frações normalizadas x,z,y do metal obedecem x′=−ax+bz,z′=ax−(b+c)z,y′=cz,com estado inicial(1,0,0). A soma permanece1. Estado estacionário aproximado do intermediário fornece z≈ax/(b+c) e k efetivo=ac/(b+c). Não é equilíbrio e não encerra todos os balanços de ligantes se os reservatórios deixarem de ser constantes.

A probabilidade de captura no modelo de duas saídas com taxas constantes é a integral de c exp[−(b+c)t],isto é,c/(b+c). Os números a0,02,b2,c3 s⁻¹ dão3/5 e0,012 s⁻¹. Dobrar[Y] dá c6,k0,015;dobrar[X] dá b4,k3/350. A redução pela recaptura não é argumento de equilíbrio final. A lei não inclui retorno de Cᵧ e não calcula constante de formação ou substituição.

## Solução completa e camada inicial

As taxas positivas de decaimento satisfazem r²−(a+b+c)r+ac=0. No código,gap=√[(a−c)²+b²+2b(a+c)], r rápido=(a+b+c+gap)/2 e r lento=2ac/(a+b+c+gap). Essa escrita evita subtrair números próximos na taxa lenta. Para gap>0:

z(t)=a[exp(−r lento t)−exp(−r rápido t)]/gap;

y(t)=1−[r rápido exp(−r lento t)−r lento exp(−r rápido t)]/gap;

x=1−z−y. O código usa expm1 para reduzir cancelamento e trata separadamente b=0,a=c: x=exp(−at),z=at exp(−at),y=1−(1+at)exp(−at). Não se promete precisão para parâmetros arbitrariamente extremos.

A curva reduzida de ordem dominante é y≈1−exp(−k efetivo t),desprezando z no estoque. Não somar essa curva e x aproximado com z estimado e esperar conservação exata. y′(0)=0 no sistema completo e k efetivo na redução: há transiente inicial. a/(b+c) pequeno sugere separar escalas,mas os erros devem ser confrontados na janela necessária,sem garantia automática de tolerância.

## Fontes — consulta parcial em27/10/2026

- Miessler,Fischer e Tarr,Química Inorgânica,5ª edição brasileira,Pearson2014,§12.2.1 p.432/PDF447,trecho de labilidade/inércia após a tabela;§12.3.1 p.434/PDF449,esquema D e aproximação. Extração textual parcial,sem nova inspeção visual ou leitura integral. Tabela de taxas e exemplos reais dos autores não foram reproduzidos. Modelo, números, solução completa, comparação, figura e exercícios próprios; exemplar privado não distribuído.
- [Júpiter CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214),reaberto em27/10/2026,ativação15/07/2024,compatível com2024/2,sem comprovar a versão ministrada. Apoio ao item10 de cinética/reatividade.
- IUPAC GoldBook,[stable](https://goldbook.iupac.org/terms/view/S05900) e[labile](https://goldbook.iupac.org/terms/view/L03432): apenas trechos recuperados por busca. Aberturas diretas retornaram403. Reforçam distinguir termodinâmica de reatividade e explicitar o sentido de lábil; não se alega leitura integral da recomendação.

Aula inicial de cinética de coordenação,sem mecanismos gerais A/I,estereoquímica,transferência de elétrons,ativação de ligantes ou validação experimental. Não conclui a química de um complexo real. Revisão pessoal pendente.

## Verificação

Cinco testes locais: solução completa contra RK4 das três equações em16 combinações caso/tempo; conservação/positividade; derivadas por diferenças centrais em4 tempos e condição inicial; raiz dupla e limite longo; competição e3 erros de aproximação observados,além de um caso sem separação forte e contratos. Comparar cálculos do mesmo modelo não valida o mecanismo químico. O domínio do código é a>0,b≥0,c>0 e t≥0.
