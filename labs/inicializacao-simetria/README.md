# Inicialização: simetria e escala sob hipóteses

Laboratório original sobre a rede existente2→H→1,tanh,logit eBCE. Importa initialize,forward,gradients,update,loss de dense_net.py sem alteração. Não cria treinador,otimizador ouframework. Rascunho assistido porIA,revisão pessoal pendente;casos sintéticos não são pesquisa ou validação externa.

Da raiz:

```sh
python3 -B -m labs.inicializacao-simetria.symmetry
python3 -B -m unittest discover -s labs/inicializacao-simetria -t .
```

`paired(outgoing)`cria duas unidades comW/bzero e pesos de saída explícitos,para inspecionar uma atualização existente. x=(1,0),y1:comv=(1,2),h0,z0,p1/2,gradientesW=(-1/2,0),(-1,0). Com passo1/10,novas linhas(1/20,0),(1/10,0). Pesos de entrada iguais sozinhos não garantem gradientes iguais;os fatores de saída importam. Simetria preservada exige parâmetros correspondentes e regras/estados de atualização iguais. Sem dropout ou ruído independente neste experimento.

SeW,b,v todos começam0,gradientesW,b,vficam0nesse modelo,enquantocpode aprender uma constante. Não generalizar a todo modelo linear ou toda arquitetura. Biaseszero com pesos distintos não impõem simetria por si.

`variance_factors(fan_in,fan_out)`int1..1000sem boolretornaFraction:VarW=2/(nin+nout),amplitude²=6/(nin+nout),fatores idealizadosninVarW enoutVarW. Para2→4:1/3,1,2/3,4/3. Média dos fatores1não significa ambos1. Uniforme contínua centrada em±atem variânciaa²/3. Fórmulas de propagação pressupõem somas lineares,independências e centragem apropriadas;backward e nãolinearidade são aproximações de escala,não identidades do treino real.

O geradorLCGantigo é determinístico de32bits e gera uma grade finita;seus pesos reais não são amostras contínuas perfeitamente independentes. Testes de faixa/repetição não certificam qualidade estatística ou variância populacional. Não se alterou o contrato antigo nem se verificou novamente equivalênciaPython/navegador,pois ambosnúcleos ficaram intactos. Repetibilidade depende também de ordem,dados,arquitetura e atualizações.

Cinco testes:contraste com vdistintos e derivada de perda por diferenças finitas;oitopassos simétricos eoitopassos todoszero;64paresdedimensões;340configurações exatas de sinais independentes para n1..4e contraexemplo correlacionado;nove inicializações existentes/faixas/contratos. Enumeração usa pesos de variânciaunitária e aplica escala analítica,sem alegar amostrar a distribuiçãoLCG. Sem avaliação de convergência ou generalização.

Fonte primária:Dive intoDeepLearning1.0.3,§5.4.1.3 e§5.4.2.2,corpo parcialmente consultado30/10/2026, https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html . Formulação local explicita pesos de saída e condições da simetria,em vez de universalizar igualdade deW. Exemplo,figura e código próprios;sem copiar exercícios ou rodar frameworks.
