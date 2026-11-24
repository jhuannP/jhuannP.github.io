# Energia livre e acoplamento — primeiro recorte de metabolismo

22/10/2026. Material original em rascunho, pendente de revisão de Jhuann. Não são dados da IC nem parâmetros fisiológicos do ATP.

## Fonte e limites

Nelson e Cox, *Princípios de Bioquímica de Lehninger*, sexta edição, Artmed 2014/original 2013, §13.1, páginas impressas 506–511/PDF 536–541. Consulta parcial por extração local: sistema aberto, energia livre padrão e real, aditividade, cinética e necessidade de intermediários para acoplamento. O início de 13.2 aparece no fim do recorte, mas não é leitura temática deste bloco. Não houve leitura integral do capítulo ou reprodução de figuras, exemplos e exercícios. O modelo abaixo usa espécies genéricas e valores próprios.

## Modelo

Alvo A→B com ΔG°=+12 e doadora D→E com ΔG°=−20 kJ/mol. Soma 1:1: A+D→B+E, ΔG°global=−8 kJ/mol. Atividades adimensionais aA=aD=aE=1, aB=Q. Portanto Qalvo=Qglobal=Q e Qdoadora=1. T=300 K, R=0,008314 kJ/(mol K), RT=2,4942 kJ/mol. ΔGalvo=12+RT lnQ e ΔGglobal=−8+RT lnQ.

Em Q=1, global −8 kJ/mol; em 10,≈−2,257 kJ/mol; em 100,≈+3,486 kJ/mol. O padrão negativo não impõe o mesmo sentido em qualquer composição. Q*=exp[8/(RT)] resolve a condição global de equilíbrio. O controle aceita somente log10Q inteiro −3…3 e não alcança Q* exatamente. Os valores de Q representam cenários de atividades, não uma coleta ou mistura celular simulada no tempo.

Somar reações não implementa um mecanismo de acoplamento. Não há previsão de velocidade, fluxo, mecanismo, concentração final, rendimento celular ou ATP real. As constantes padrão químicas destas espécies genéricas não são automaticamente valores bioquímicos transformados.

## Ler a figura

Eixo horizontal log10Q, adimensional; vertical ΔG em kJ/mol da reação como escrita. Azul: global; preto tracejado: alvo; pontilhado: zero. Marcador azul: escolha. Escalas fixas −3…3 e −30…30 kJ/mol. A linha do alvo continua 20 kJ/mol acima da global porque ΔGdoadora=−20 em todos os cenários. Não é gráfico temporal ou cinético.

## Executar e verificar

Na raiz do protótipo:

```sh
python3 labs/acoplamento-energia/experiment.py
python3 -m unittest discover -s labs/acoplamento-energia -t .
```

Três testes: soma independente de potenciais químicos μ°A=0,μ°B=12,μ°D=20,μ°E=0 e relação RTln(Q/Q*); monotonicidade, incrementos e sinais; contratos. Os potenciais são uma construção sintética consistente, não dados de substâncias reais. Sete referências JSON calculadas em Decimal 60 a partir dos mesmos parâmetros para confrontar JavaScript. Isso verifica implementação e consistência algébrica, sem validação experimental.

Aula 12 seções/10 exercícios. Primeiro recorte de introdução ao metabolismo; glicólise, pentoses, Krebs, fosforilação e fotossíntese continuam pendentes. Mecanismos documentados de transferência e balanços de matéria/ATP exigem desenvolvimento antes de ofertas de ensino ou alegações de domínio.


## Verificação final e continuidade

761 testes Python aprovados; suíte JavaScript com 278 demonstrações/834 cenários básicos e referências adicionais aprovada; 449 estruturas MathML conferidas. Navegador: controle por teclado de Q=1 para Q=100 mudou o sinal de −8 para aproximadamente +3,48622 kJ/mol; resposta 3,4862 aceita no exercício. Tela 390 px sem transbordamento horizontal e sem erros de console observados. Viewport restaurado; prévia `acoplamento-energia-mobile.jpg` na raiz.

Biologia I: nove aulas/101 exercícios, nove grupos parciais e dez lacunas. Catálogo geral 487 aulas/2537 exercícios. Nenhum conteúdo declarado completo ou domínio certificado. Próxima revisão: explicar a diferença entre ΔG padrão/atual e mecanismo/velocidade. Próxima alternância global: revisar sequência e pendências de Computação II. Saldo após bloco 74%; parada 65%.
