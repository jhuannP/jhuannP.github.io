# Correlação 1D e sua adjunta

Notas originais em rascunho para revisão de Jhuann. Operação complementar,sem disciplina cursada,CNN treinada ou resultado de pesquisa comprovados.

## Fonte e recorte

[D2L1.0.3§§7.2.1 e7.2.5](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html),consulta parcial29/10/2026: correlação,janelas,tamanho e convenção de inversão. A fonte usa2D; nossa redução1D,exemplos,matriz,derivadas,figura e código são próprios. Sem reprodução de figura,código ou exercício da fonte;nenhum framework instalado/executado.

## Modelos separados

Script float e desafio anteriores da aula preservados/executados; painel convolutionWindow preservado,com suas escolhas de stride/padding. Novo laboratório restringe passo1,padding0,um canal,sem bias/dilatação,até30 componentes inteiras/Fraction. A validação racional adicional não certifica todos os limites numéricos do script anterior.

x=(2,−1,3,0),k=(1,2) produz y=(0,5,3). Com g=(1,−2,1) fixo,L=g·y=−7:dx=(1,0,−3,2),dk=(7,−7). Verificação g·y=x·dx=k·dk=−7. Não somar os dois últimos produtos para tentar recuperar L; a operação é bilinear.

Outra função: alvo t=(1,1,1),L=½Σ(y−t)²=21/2. Agora g=(−1,4,2),dx=(−1,2,10,4),dk=(0,13). Trocar pela média divide perda/gradientes por3. Diferenças centrais coincidem exatamente para a função quadrática por coordenada isolada em aritmética racional; isso não elimina erros gerais de aproximação/arredondamento.

## Executar

Na raiz: `python3 labs/correlacao-adjunta/correlation.py`; testes: `python3 -m unittest discover -s labs/correlacao-adjunta -t .`.

Oráculos: matriz diagonal independente em243 entradas/kernel pequenos,produtos internos e diferenças de coordenada em dois passos racionais. Sem inversão de operador,construção de arquitetura ou treinamento. Aᵀg é retorno do gradiente,não reconstrução de x.

## Próxima revisão

Reconstruir janelas e acumulação; separar as duas perdas. Para amostras físicas,a diferença precisa de espaçamento e análise de erro. Passo,padding,canais,treino integrado,generalização e revisão pessoal continuam pendentes. Nenhuma marca de estudada preenchida.
