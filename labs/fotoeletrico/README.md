# Efeito fotoelétrico e fluxo de fótons

Modelo didático original para revisão de Jhuann. Superfície hipotética, sem dados experimentais ou resultados da IC.

## Fontes consultadas em 16/10/2026

- [OpenStax University Physics III 6.2](https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect): trechos de energia, limiar, irradiância e módulo do potencial de corte. Não leitura integral do capítulo ou reprodução de exercícios/figuras.
- [NIST, definições das unidades base SI](https://www.nist.gov/si-redefinition/definitions-si-base-units): h=6,62607015×10⁻³⁴ J·s, e=1,602176634×10⁻¹⁹ C e c=299792458 m/s são valores definidos. Operações numéricas continuam arredondadas.

Livros privados identificados na bibliografia do curso permanecem no acervo; não houve nova leitura desses exemplares neste bloco. Nenhum PDF privado servido. Eficiência de 0,20 é hipótese própria, não dado do livro ou material real.

## Energia e eventos

O controle é r=f/f₀, f₀=φ/h. Energia por fóton rφ; Kmax=(r−1)φ apenas para r≥1. Abaixo, Kmax fica ausente em vez de zero ou negativo. Na borda o balanço dá Kmax=0, mas a corrente com luz fica sem previsão. Sem luz, taxa e corrente são zero em qualquer r.

Área A=1 mm², irradiância I em W/m², taxa Γ=IA/(hf). Acima do limiar estipula-se eficiência η=0,20 e coleta integral: taxa eletrônica ηΓ e corrente ideal de saturação eηΓ. Não há curva corrente–tensão ou modelo de onset na borda, dependência de η com f, reflexão, carga espacial, temperatura ou eventos multifóton. A corrente não é uma medida.

Vs é módulo teórico da tensão retardadora, eVs=Kmax. Valores em eV e V coincidem numericamente; são grandezas distintas. Se I=0, o limite por evento continua hipotético, sem elétron emitido ou corte medido. Ao mudar φ com r fixo, a frequência absoluta muda; relatório mostra THz e nm.

## Reprodução e testes

Na raiz: `python3 -m unittest discover -s labs/fotoeletrico -t .`.

Quatro testes: balanço e conversões, frequência/comprimento de onda/limiar; separação irradiância/frequência e efeito de potência fixa; 36 referências Decimal de 60 dígitos com constantes em strings; luz desligada e domínio. `reference.json` contém 36 configurações JS/Python, incluindo borda e irradiância zero. Concordância entre linguagens complementa as verificações analíticas e de alta precisão.

## Pendências

Distribuição de energias, medidas e incertezas, superfícies reais, rendimento espectral, curva de coleta, efeitos térmicos e multifóton. Física IV segue parcial e aguarda revisão pessoal.
