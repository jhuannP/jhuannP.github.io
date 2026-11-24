# Hidrostática: pressão local e força integrada

Rascunho original, pendente de revisão pessoal. Fluido homogêneo incompressível em repouso, g=10m/s², superfície plana. Parede retangular vertical desde a superfície até H, largura b perpendicular ao corte. p₀ em kPa no controle e convertido para Pa; atua na superfície e uniformemente na face externa. Essa última condição justifica cancelar a contribuição de referência na força líquida.

Δp=ρgz; pabs=1000p₀+Δp; Frel=ρgbH²/2; Fum lado=1000p₀bH+Frel. Centro da força líquida em2H/3 paraH>0. H=0: área e força zero, centro não definido. O centro de um lado sob pressão absoluta não é o mesmo e não é exibido. A consulta z é uma fração deH e não muda a integração.

Setas no corte codificam pressão relativa com escala200px/60kPa, não força ou velocidade. O gráfico tem profundidade na horizontal e pressão emkPa na vertical, absoluta azul/relativa preta tracejada, somente no trecho molhado. Largura não altera pressão e dobra força quando duplicada. DuplicarH quadruplicaFrel neste recorte. Nada é resultado experimental ou dimensionamento estrutural.

## Fontes públicas consultadas parcialmente

- [OpenStax University Physics I14.1](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure): pressão, unidades, equilíbrio de fatia e densidade constante/variável.
- [14.2](https://openstax.org/books/university-physics-volume-1/pages/14-2-measuring-pressure): absoluta e manométrica, com referência explícita.
- [14.4](https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy): empuxo e peso do fluido deslocado.

Consulta dos trechos pertinentes; sem figuras, tabelas ou exercícios copiados. Integração da parede, momento, código e verificações são próprios. Não houve nova consulta a PDF privado. A referência externa não define a versão histórica da disciplina de Jhuann.

## Reproduzir

Na raiz:

```sh
python3 labs/hidrostatica-parede/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:81estados de pressão/referência/gradiente;54paredes contra integração de Simpson em frações exatas para força linear e momento quadrático; invariantes de largura/altura/referência/consulta;H=0 e domínio.54referências JSON cruzadas com JS. O teste de Simpson é independente das expressões fechadas usadas no painel; a precisão exata para polinômios não valida aplicações com propriedades variáveis.

Ainda faltam manômetros, camadas, compressibilidade, superfícies curvas, escoamentos e ensaios com incerteza. A versão atual não encerra hidrostática, FísicaII ou o objetivo da biblioteca.
