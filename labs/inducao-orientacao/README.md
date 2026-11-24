# Magnetismo e indução: orientação antes do sinal

Notas de aula próprias, assistidas por IA e em rascunho para revisão de Jhuann. Exemplos hipotéticos; não houve montagem, medidas ou certificação de domínio pessoal.

## Fontes consultadas parcialmente em26/10/2026

- [OpenStax, University Physics Volume2, §11.2](https://openstax.org/books/university-physics-volume-2/pages/11-2-magnetic-fields-and-lines): definição da força magnética por produto vetorial, direção e sinal da carga.
- [§13.1, Faraday](https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law): fluxo, fem e bobina com N voltas de mesmo fluxo.
- [§13.2, Lenz](https://openstax.org/books/university-physics-volume-2/pages/13-2-lenzs-law): oposição à variação do fluxo e sentidos de campo/corrente.

Consulta de trechos, sem leitura integral dos capítulos. Não se copiam figuras, exercícios ou demonstrações do livro. Exemplo afim, números, diagrama e código são próprios. Não houve nova consulta ao exemplar privado de NussenzveigIII neste bloco.

## Dois problemas diferentes

Força sobre uma carga: F_B=q(v×B). Nos eixos destros (+x direita,+y cima,+z saindo), v=(2,0,0)m/s e B=(0,0,3)T dão v×B=(0,−6,0). q=+1C produz F_y=−6N; q=−1C produz+6N. Números escolhidos para álgebra de sinais. A potência da contribuição magnética é F_B·v=0; isso não impede trabalho do campo elétrico induzido num circuito.

Indução em espira fixa: escolha normal e contorno positivo pela mão direita. Se a normal sai da tela, positivo é anti-horário visto de frente. Campo uniforme dá Φ=B·A=BAcosθ; θ é com a normal, não com o plano. A fem é uma circulação com unidade volt, não uma força em newtons nem, em geral, uma diferença de potencial eletrostático independente do caminho.

## Preservar o exemplo original

ΔΦ=+6Wb durante3s numa volta: fem média−2V. Apenas se a variação for linear esse valor também é a fem instantânea constante. Sem resistência e modelo de resposta, o exemplo não determina corrente. Fluxo constante5Wb durante2s dá fem média zero, como no desafio original.

## Novo modelo explícito

Área vetorial A=(0,0,1/5)m²; campo externo B(t)=(0,0,1+2t)T, t em segundos. Fluxo por espira Φ=1/5+(2/5)t Wb. Uma volta: ε=−2/5V. Com R total4Ω e aproximação resistiva sem autoindução/realimentação, I=−1/10A (horário); P=I²R=1/25W. O agente externo que mantém B variável fornece a energia; o código não o resolve.

No contraste B_z=1−2t, para0≤t<1/2s o campo ainda sai da tela, mas diminui: ε=+2/5V, I=+1/10A (anti-horário). O campo induzido agora sai, no mesmo sentido do externo. Lenz resiste à variação, não exige campo contrário em todos os casos. O campo induzido não é calculado numericamente nem suposto capaz de cancelar todo o externo.

Se invertermos A e o contorno positivo compatível, Φ,ε e I trocam de sinal; a circulação física não muda e P é invariante. N voltas fixas com mesmo fluxo por volta multiplicam ε por N; R deve ser a resistência total declarada. Não multiplicar duas vezes se o fluxo já for o encadeamento NΦ.

## Executar

Na raiz do site:

```sh
python3 -m labs.inducao-orientacao.induction
python3 -m unittest discover -s labs/inducao-orientacao -t .
```

`force` calcula vetor força com int/Fraction. `mean_emf` recebe fluxos por volta, duração positiva e N inteiro positivo. `fixed_loop` usa campo afim externo, área vetorial fixa não nula, R total positiva e tempo não negativo; informa fluxo por volta, taxa, fem, corrente resistiva e potência. Retorna números racionais exatos. Não infere orientação visual de qualquer desenho: o usuário fornece vetores nos mesmos eixos. Entradas bool/float são rejeitadas.

Cinco testes: exemplo de força e ortogonalidade em729 pares de vetores; projeção de fluxo/campo constante;81 cenários afins comparados a diferenças exatas entre extremos; inversão da orientação/rotação dos eixos, sinais e potência; exemplo original e contratos. Testes conferem implementação, não provam leis físicas nem o regime de uma bobina real.

## Respostas dos exercícios novos

- F_y=−6N para carga positiva e+6N para negativa.
- Fluxo0,6Wb com B=3T e A=0,2m² alinhados; zero com campo paralelo ao plano.
- Taxa de campo+2T/s dá ε=−0,4V e I=−0,1A, dados A/R do modelo.
- Taxa−2T/s dá I=+0,1A.
- Três voltas com taxa de fluxo por volta+0,4Wb/s dão−1,2V.
- Dissipação0,04W; mantida por5s, energia0,2J. A duração é hipótese explícita dessa pergunta.

Próxima revisão pessoal de20min: escolher a normal, prever os dois sentidos da figura e reconstruir a cadeia B(t)→Φ(t)→ε→I. Não marcar estudo concluído antes da revisão pessoal. Campos de fios/solenoides, força em condutores, espira móvel, autoindução e circuitos RL permanecem pendentes.
