# Arrhenius — notas de aula

Rascunho original assistido por IA; revisão de Jhuann pendente. Não certifica domínio ou conclusão de disciplina.

## Modelo e derivação

k(T)=A exp(−Ea/RT), com A e Ea constantes no intervalo. A tem a unidade de k, T é absoluta em K, Ea está em J/mol e R=8,314462618 J mol⁻¹ K⁻¹ (valor arredondado adotado). Escolha k* de mesma unidade: ln(k/k*)=ln(A/k*)−Ea/(RT). Subtrair entre T₁ e T₂ elimina A e k*: ln(k₂/k₁)=(Ea/R)(1/T₁−1/T₂). A inclinação de ln(k/k*) contra1/T é −Ea/R em K; contra1000K/T é −Ea/(1000KR), adimensional. Com log₁₀, dividir a inclinação por ln(10).

A inversão de dois pontos é Ea=R ln(k₂/k₁)/(1/T₁−1/T₂). Exige T positivos distintos e k positivos de mesma lei e unidade. Dois pontos determinam uma reta; não validam o modelo ou mecanismo. Próximos entre si, tornam a energia sensível a erros.

## Exemplo próprio e resoluções

Ea/R=6000K, Ea=49886,775708J/mol=49,886775708kJ/mol; k300=0,002s⁻¹. De300para330K: diferença de recíprocos1/3300K⁻¹, logaritmo20/11, fator6,1606470843, k330=0,01232129417s⁻¹. Meia-vida de primeira ordem:346,57359s a300K e56,25604s a330K. Ensaios isotérmicos separados; T variável exigiria integrar k(T(t)).

Respostas dos exercícios1–8:49,886775708;20/11;6,1606470843;0,01232129417;56,25604;−20/11;−6000K;−6. Questão9: unidades coerentes J/mol e K. Questão10: não comprova mecanismo. Questão11: A também importa. Questão12: ln(0) não é finito; limite de detecção requer tratamento experimental próprio.

Contraexemplo de comparação: na mesma T, A_b/A_a=exp(−10), Ea_b−Ea_a=−5RT dá k_b/k_a=exp(−5)<1 apesar da menor Ea_b. Isso compara constantes na mesma unidade; velocidades ainda dependem das leis e concentrações. Não supor que catalisadores apenas trocam Ea com A fixo.

## Código e verificação

Na raiz do protótipo:

```sh
python3 -m unittest discover -s labs/arrhenius-temperatura -t .
```

API SI explícita: `log_ratio` retorna ln(k₂/k₁); `rate_ratio` retorna seu exponencial se representável; `infer_ea` retorna J/mol. Ea negativa é permitida como parâmetro aparente; não interpretada automaticamente como barreira elementar negativa. Float/int finitos, sem bool; temperaturas e taxas estritamente positivas. Limites de representação geram erro, não razão zero silenciosa. A unidade de k e o protocolo são declarados pelo usuário; código não pode verificar a consistência física de rótulos ausentes.

Cinco testes: caso20/11; 27 comparações com Decimal a60 dígitos usando duas constantes absolutas A exp(−Ea/RT), em vez da identidade da razão; inversão/composição e escala comum da unidade de k; transbordamento/subfluxo e cálculo logarítmico; contratos. Sem regressão ou estimação de incerteza. Não instalar dependências; diagrama SVG original de comparação, sem escala gráfica ou figura reproduzida.

## Referências e limites

USP, CCM0124: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124 . Item8 inclui Arrhenius; ativação01/01/2025, reaberto em27/10/2026, posterior à turma2024/1. Versão da turma não recuperada.

Levine, Physical Chemistry, sexta edição2009, §16.8 pp.541–543/PDF559–561: leitura parcial em27/10/2026. P.542/PDF560 inspecionada visualmente, confirmando sinal da inclinação e exigência de logaritmos adimensionais; a imagem no exemplar não mostrou os traços da figura16.9, e não foi usada para inferir dados. Exemplar privado não distribuído. Sem leitura integral do capítulo; exemplos e números próprios.

Apoio público parcial: https://openstax.org/books/chemistry-2e/pages/12-5-collision-theory . Contexto de Arrhenius e colisões; não generalizar a interpretação de barreira elementar para qualquer Ea aparente. A definição local Ea(T)=RT²d ln(k/k*)/dT permite variação com T. Ela não equivale automaticamente a ΔH de reação ou ΔG‡. Ainda faltam ajuste de múltiplos pontos com dados reais e incertezas, mecanismos microscópicos e discussão quantitativa de catálise. Nenhuma medida ou resultado científico de Jhuann foi criado.

## Registro pessoal

Data: ____ · raciocínio reconstruído: ____ · dúvida: ____
