# Três regimes de amortecimento

22/10/2026. Rascunho original para revisão de Jhuann, sem dados experimentais ou da IC.

## Modelo e convenção

Massa-mola livre com resistência linear −bv: m=1 kg, k=4 N/m, x(0)=1 m e v(0)=0. Painel varia b de 0 a 8 kg/s e lê t de 0 a 10 s. Soluções dos três regimes, com b crítico 4 kg/s; energia E=v²/2+2x² e potência E′=−bv². A dissipação é transferência de energia mecânica ao ambiente, sem destruição da energia total.

Convenção própria: γ=b/(2m). Nussenzveig II usa ρ para resistência e γ=ρ/m, o dobro do parâmetro desta aula. Os critérios de regime são convertidos explicitamente.

## Fontes

Consulta parcial ao exemplar privado de Nussenzveig, *Curso de Física Básica 2*, quinta edição revista e ampliada, Blucher 2014, terceira reimpressão 2017: §§4.1–4.2, páginas impressas 95–101, PDF 96–102. Equação, condições iniciais, regimes e balanço instantâneo de energia lidos por extração local. A parte inicial de §4.3 aparece na última página, mas não foi usada como referência temática. Não houve leitura integral do capítulo, cópia de figuras ou reprodução dos exemplos e exercícios. A comparação de retorno foi limitada às condições iniciais e ao critério declarado; inspeção em janela finita não é prova assintótica.

## Exploração

- b=0: oscilação sem dissipação; E=2 J.
- b=2: γ=1 s⁻¹, ωd=√3 s⁻¹; oscilação com decréscimo da energia.
- b=4: crítico, x=(1+2t)e^(−2t), v=−4t e^(−2t), em unidades SI com t em segundos.
- b=8: superamortecido; neste PVI, aproximação a zero mais lenta que a crítica em tempos longos.
- Tempo de leitura move apenas o marcador, sem alterar a curva.

Escalas do gráfico fixas: tempo0–10 s e deslocamento −1,2 a 1,2 m. Azul é b escolhido; tracejado é o crítico. Em b=4 coincidem. O painel apresenta energia e potência instantâneas, sem aproximá-las por uma exponencial média. A demonstração subamortecida anterior permanece como apoio adicional.

## Implementação e verificação

`experiment.py` aceita int/float finitos, b em [0,8] e t em [0,10], rejeitando bool. Fórmulas separadas por regime; raiz lenta racionalizada e expm1 evitam cancelamentos no superamortecido. A implementação permite avaliar perto do crítico, mesmo que o controle use passo 0,5.

Na raiz do protótipo:

```sh
python3 labs/amortecimento-regimes/experiment.py
python3 -m unittest discover -s labs/amortecimento-regimes -t .
```

Quatro testes: integração RK4 independente da EDO para 24 combinações, incluindo aproximações ao crítico; condições iniciais e limite crítico; balanço E+∫bv²=E0 por Simpson e monotonicidade para seis resistências; contratos. Referências JSON: 32 estados calculados por recorrência de coeficientes da EDO em série de Taylor com 80 dígitos e 300 termos, não pelas fórmulas fechadas dos ramos. JavaScript confrontado com essas referências.

Limites: oscilador linear livre, sem atrito seco, resistência quadrática, força externa ou identificação experimental. A ausência de oscilações não significa parada em tempo finito. Condições iniciais arbitrárias, critério de acomodação e problemas integradores ainda precisam desenvolvimento. Aprovação dos testes não substitui revisão conceitual.


Verificação final: 755 testes Python aprovados; suíte JavaScript com 276 demonstrações/828 cenários básicos e referências adicionais aprovada; 441 estruturas MathML conferidas. No navegador, b=4 e b=8 classificados corretamente por teclado, exercício de b crítico aceito, largura 390px sem transbordamento horizontal e sem erros de console observados. Rótulos do gráfico ampliados e escala vertical final −1,2 a 1,2 m para preservar os sinais. Prévia `amortecimento-regimes-mobile.jpg` na raiz.

Aula atual: 14 seções/12 exercícios. Física II: 14 aulas/112 exercícios, cinco introduções curtas e nove recortes desenvolvidos; dez grupos ainda parciais. Catálogo geral 485 aulas/2517 exercícios. Revisão pessoal pendente. Próxima alternância: sequência de Química I; próxima revisão deste tema: reconstruir condições iniciais e balanço. Saldo após o bloco: 75%; parada em 65%.
