# Seleção de relatos — notas de aula

Rascunho original, assistido por IA; revisão pessoal de Jhuann pendente. Não comprova domínio pessoal. Sem dados reais ou taxas estimadas.

## Pergunta e modelo

H é o estado, R o sinal binário e S o registro. Cada tentativa ocorreu e foi concluída; sabemos se foi registrada. P(H)=1/2, P(+|H)=3/4 e P(+|Hᶜ)=1/4. Para cada par estado/sinal, fornecer q=P(S|estado,sinal). A massa de uma célula é P(estado)P(sinal|estado)q para S; usar 1−q para Sᶜ. Somar as células desejadas antes de normalizar. Nenhuma independência geral foi presumida.

## Duas tabelas de massas exatas

| Estado/sinal | A registrado | A omitido | B registrado | B omitido |
|---|---:|---:|---:|---:|
| H,+ | 3/16 | 3/16 | 3/16 | 3/16 |
| H,− | 1/8 | 0 | 1/16 | 1/16 |
| Hᶜ,+ | 1/16 | 1/16 | 3/32 | 1/32 |
| Hᶜ,− | 3/8 | 0 | 9/32 | 3/32 |
| Total | 3/4 | 1/4 | 5/8 | 3/8 |

A: guardar metade dos positivos e todos os negativos. B: guardar metade sob H e três quartos sob Hᶜ, independente do sinal dado o estado. B é um mecanismo hipotético, não presume acesso prático ao estado oculto.

## Resoluções e conferências

1. Antes do filtro: P(H|+)=(3/8)/(1/2)=3/4.
2. A: P(S)=3/4.
3. A: P(H|S)=(5/16)/(3/4)=5/12.
4. A: P(H|+,S)=(3/16)/(1/4)=3/4.
5. B: P(+,S)=3/16+3/32=9/32.
6. B: P(H|S)=(1/4)/(5/8)=2/5.
7. B: P(H|+,S)=(6/32)/(9/32)=2/3.
8. B: P(H|Sᶜ)=(1/4)/(3/8)=2/3.
9. B: P(+|S)=(9/32)/(5/8)=9/20.
10. Fatores iguais e positivos dentro do sinal observado cancelam; não basta igualar taxas marginais.
11. Evidência zero: a razão elementar é indefinida; None no laboratório.
12. Registros sozinhos não identificam em geral o processo dos omitidos.

Conferência por partição: no B, (5/8)(2/5)+(3/8)(2/3)=1/2. No A, (3/4)(5/12)+(1/4)(3/4)=1/2. Após conhecer S, as taxas do sinal só permanecem iguais às originais no B porque S depende apenas do estado por hipótese. No A, é necessário atualizar também essas taxas.

## Fonte e limites

Leitura textual parcial reconferida em 27/10/2026 dos exemplares privados: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §2.2, pp.54–55 e59 (PDF69–70/74); Marcos N. Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, §1.3, pp.28–30 e35 (PDF19–20/22, páginas duplas). A extração de PVA intercala colunas. Sem nova inspeção visual dos livros neste bloco e sem leitura integral dos capítulos. Fundamentos: definição, produto, total, Bayes e independência condicional. Protocolos, tabelas, código, figura e exercícios próprios. Não distribuir os PDFs privados.

Noções p.54 e PVA p.28 mencionam uma extensão em condição de massa zero; este laboratório prefere None, sem tratar divisão por zero como válida. Não é modelo de não resposta contínua, correção causal, inferência de taxas ou avaliação real de agentes. Uma omissão só é evidência interpretável quando o experimento e seu registro são conhecidos.

## Executar

Na raiz do protótipo:

```sh
python3 -m unittest discover -s labs/selecao-relatos -t .
```

Cinco testes: exemplos; oráculo independente com 64 sorteios equiprováveis por configuração (25 configurações e nove filtros cada); cancelamento em 81 configurações; evento impossível; contratos. API local aceita int/Fraction, rejeita float/bool e probabilidades inválidas. `condition` consome a tabela válida produzida por `joint`, não tabelas arbitrárias.

## Registro pessoal

Data: ____ · reconstrução sem consultar: ____ · dúvida: ____
