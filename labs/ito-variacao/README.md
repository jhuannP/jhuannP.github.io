# Itô, variação quadrática e somas finitas

Rascunho para revisão pessoal. Não gera Brownian motion,não simula EDE,não valida IC. `square_sums` recebe uma lista prescrita de até4096 incrementos int/Fraction e estado inicial racional,retorna valor final,soma à esquerda,direita,ponto médio e soma dos quadrados. A identidade algébrica exata não transforma uma sequência prescrita em trajetória browniana.

`brownian_errors` fornece momentos teóricos sob n incrementos gaussianos independentes N(0,T/n),T≥0,n inteiro1..10^6: E Q=T,Var Q=2T²/n,MSE(L−I)=T²/(2n),I=(W_T²−T)/2,W0=0. Na malha uniforme,L=(W_T²−Q)/2. Logo MSE=VarQ/4,pois E Q=T. Isso prova convergência L2 neste caso; não é igualdade Q=T em toda malha nem convergência quase certa por uma única verificação finita. Dobrar n divide MSE por2;quadruplicar n divide norma L2 por2.

`ito_polynomial` calcula deriva b f′+σ²f″/2 e difusão σf′ para polinômio independente de tempo,coeficientes crescentes até grau8. x,b,σ são valores racionais pontuais; não estima coeficientes,resolve uma EDE ou assume que W tenha derivada. Para f=x²,b=−2x,σ3,x2,retorna−7 e12. A fórmula geral exige hipóteses de Itô; a comparação com derivadas não verifica condições probabilísticas.

## Fontes consultadas em29/10/2026

Pavliotis,Stochastic Processes and Applications,Springer2014,§3.4 pp.66–68/PDF79–81:recortes textuais de gerador e fórmula integrada; p67/PDF80 também visual para Lemma3.2,Eq3.51 e regularidade C1,2. Sem leitura integral do capítulo,cópia de exemplos ou PDF privado. Localização +13 verificada no recorte,não presumida global.

MIT OCW6.265/15.070J,Fall2013,Lecture17 de13/11/2013,PDF pp.1–4,consulta textual parcial da definição,teorema e esboço: https://live.ocw.mit.edu/courses/15-070j-advanced-stochastic-processes-fall-2013/d9d7372cbf65d56aa8aa9d59ba0ab2e8_MIT15_070JF13_Lec17.pdf . Sem vídeo,prova completa generalizada ou cópia de exercício. Derivação quantitativa de erros,figura,sequências prescritas e código próprios. O percurso é complementar,não disciplina formal cursada ou equivalência USP;nenhuma oferta foi reconferida.

## Verificar

```sh
python3 -B -m unittest discover -s labs/ito-variacao -t .
python3 labs/ito-variacao/ito.py
```

Cinco métodos:162 sequências prescritas por telescopagem;15 combinações n/T por quartos momentos gaussianos e pares independentes,com segunda conferência pela isometria e erro de aproximação do integrando;162 estados polinomiais contra estênceis independentes exatos até grau4;marcos;contratos. Testes verificam contas/código,não a lei browniana de dados ou teorema geral. Não houve Monte Carlo;figura tem momentos teóricos.
