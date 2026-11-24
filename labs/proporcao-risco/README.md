# Proporção e contração: comparar riscos

29/10/2026. Rascunho original para revisão de Jhuann.

Bernoulli iid, K soma de n resultados, p fixo prescrito para avaliar riscos. Regras p̂=K/n e T=(K+1)/(n+2). Perda quadrática para alvo p,não variância. E[T]=(np+1)/(n+2),Bias=(1−2p)/(n+2),Var=np(1−p)/(n+2)². MSE soma de variância e viés². Proporção tem risco p(1−p)/n.

n4: riscoT1/36 constante, risco proporção p(1−p)/4. T melhora se p(1−p)>1/9,piora quando menor. Em p1/2:1/36 versus1/16; em p0:1/36 versus0. Em p1/4:viés1/12,var1/48. Sem dominância uniforme,prova de optimalidade ou interpretação posterior automática. Suavização não adiciona observações reais,não corrige coleta enviesada e não informa erro de uma estimativa concreta.

Para cada p, MSE(T)≤n/[4(n+2)²]+1/(n+2)²→0; Markov no erro² dá convergência em probabilidade. Critério de momentos é suficiente aqui,não definição universal necessária de consistência.

Fonte: Magalhães/Lima,Noções7ªedição2010/reimpressão2011,§7.2 pp229–233/PDF244–248, consulta textual parcial29/10/2026;p229/PDF244 visual para definições. Não copiados exemplos/atividades; modelo,curvas e enumeração locais. Sem nova consultaPVA.

```sh
python3 labs/proporcao-risco/risk.py
python3 -B -m unittest discover -s labs/proporcao-risco -t .
```

Cinco testes: amostras ordenadas independentes dos pesos binomiais,n1..6/cinco p; fórmulas fechadas,seis n/seis p; constância n4 em41p e falta de dominância; valores/simetria/limite deMSE; contratos. n1..100,p int/Fraction;bool/float rejeitados. Sem validação de população real ou uso com aluno.
