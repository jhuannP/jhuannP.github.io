# SN1: modelos e limites de inferência

Rascunho assistido por IA para revisão pessoal, sem protocolo, dados ajustados, previsão de síntese ou experiência de bancada. O modelo de decaimento assume etapa efetiva irreversível de primeira ordem com k constante, produto inicial zero e estequiometria1:1. Concentração em mol/L,tempo em s,k em s⁻¹. Não representa retorno do grupo de saída,acoplamento de etapas,eliminação,rearranjos ou produto formado com atraso por intermediário acumulado.

`decay(S0,k,t)=S0 exp(−kt)` recebe reais finitos não negativos. É solução ideal, não ajuste de reação. O produto S0−S vale apenas no modelo efetivo1:1. Um esquema SN2 com nucleófilo em grande excesso constante tem k_obs=k2[Nu] e pode reproduzir a mesma curva,sem provar SN1. Comparação ao variar Nu pressupõe demais condições e constantes comparáveis; solvente/meio podem mudar k.

`stereo(r)` usa Fraction0..1:fração r de eventos com duas faces equiprováveis,restante só inversão. Inversão=1−r/2,retenção=r/2. r3/5 gera7/10 e3/10,excesso normalizado2/5. Não é probabilidade calculada de uma molécula ou estimativa da fração real de carbocátions livres. Mesmo histograma pode vir de contribuição de pares iônicos ou de rota SN2. Os rótulos são relações geométricas e não troca automática de R/S;igualar produto a par de enantiômeros requer as hipóteses da aula.

## Fontes lidas parcialmente em29/10/2026

Brown/Poon,Introduction to Organic Chemistry,6ªed Wiley2016,§7.4B pp.199–200/PDF219–220 e início p201/PDF221. Leitura textual parcial;p199 também visual para etapas,pares e carga do oxônio. A formulação ideal de faces iguais do livro é distinguida da ressalva de pares iônicos. Sem copiar exemplos específicos,diagramas,proporções experimentais ou disponibilizar PDF privado.

McMurry,OpenStax Organic Chemistry§11.4 https://openstax.org/books/organic-chemistry/pages/11-4-the-sn1-reaction :recortes de cinética,intermediário e limitação por pares iônicos lidos parcialmente; sem copiar exemplo ou figura. Números e modelo de mistura são próprios. IUPAC ion pair abertura direta403; não alegada leitura do corpo. MapaCCM0224 mantém consulta anterior27/10 e ativação2025 encontrada22/10,versão ministrada não comprovada;programa não reaberto neste bloco.

## Verificações

```sh
python3 -B -m unittest discover -s labs/sn1-evidencias -t .
python3 labs/sn1-evidencias/models.py
```

Cinco métodos:36 estados por exponencial Decimal70 independente;cinco meias-vidas e balanço1:1;11 misturas por enumeração independente de20 eventos;quatro tempos indistinguíveis de pseudo-primeira ordem e perturbação de Nu;contratos. Testes não provam mecanismo real,estereoquímica de uma amostra ou aplicação pessoal.
