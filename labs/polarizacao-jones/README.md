# Polarização: amplitudes, filtros e mistura

Modelo original:onda plana monocromática em+z,componentes transversais complexas e=(Ex,Ey). Campo físico Re[e exp(i(kz−ωt))]; mesma impedância e normalização de intensidade relativa I/Iref=|Ex|²+|Ey|². Intensidade absoluta exigiria o fator do meio e a escala do campo. Um estado puro tem norma1; depois dos filtros pode ter norma menor. Não renormalize se deseja intensidade relativa à entrada.

Analisador ideal de eixo u=(cosθ,sinθ):P=eixo×eixo†,saída u(u†e). Para entrada linear de ânguloα,a transmissão écos²(θ−α). A saída transmitida tem direção do analisador. Entrada x: filtros0°,90° dãozero;0°,45°,90° dão1/4. Com entrada não polarizada,primeiro filtro custa1/2 e a sequência dá1/8. Não há ganho de energia:cada etapa individual é contrativa; inserir um filtro muda a transformação da preparação transmitida.

Circular e=(1,i)/√2 é plenamente polarizada,não mistura. No ponto fixo e convenção temporal declarada,o campo real gira de+x para+y ao avançar um quarto de período. Não usamos rótulos direita/esquerda dependentes da convenção de observação. Um analisador linear transmite1/2 para qualquerθ,tanto nesse estado quanto na mistura incoerente50/50 de x/y. Isso não torna os estados iguais. Placa ideal diag(1,−i) transforma circular em linear45°; analisador45° transmite1 no caso puro e1/2 na mistura. Fases globais não alteram intensidades; fase relativa pode alterar o resultado.

```sh
python3 labs/polarizacao-jones/polarization.py
python3 -m unittest discover -s labs/polarizacao-jones -t .
```

Complex float e biblioteca padrão,sem dependências. Os valores de extinção podem ficar próximos de10⁻³² por arredondamento trigonométrico,não vazamento experimental. Máximo12 filtros/componentes; mistura usa soma de intensidades de preparações incoerentes unitárias,pesos não negativos somando1 com tolerância. Apenas estados puros têm vetor único neste modelo; não se soma amplitudes de componentes de uma mistura. A rotina não implementa formalismo geral de matriz densidade,instrumentos,dispersão,reflexão,Brewster ou absorção real. Seus testes são exemplos finitos,não validação de aparelho.

Fontes consultadas parcialmente29/10/2026:
- Nussenzveig,Curso de Física Básica4,2ªed2014,§§5.2–5.3,pp.121–126/PDF122–127,texto sobre amplitudes complexas,intensidade,elipse e casoslinear/circular. Algumas equações ausentes na extração não foram tomadas como leitura literal. Metadados emtexto:2ªreimpressão2017/1ªdigital2018. Extração integral do arquivo emcache gerou avisosFlate/ExtGState;não significa leitura integral. Sem nova inspeção visual,nem distribuição dePDF ou figura do livro.
- [OpenStaxUP3§1.7](https://openstax.org/books/university-physics-volume-3/pages/1-7-polarization),consulta parcial da seçãoMalus:eq1.6 e fator1/2 para entrada não polarizada. Reflexão,Brewster e aplicações não desenvolvidos aqui.

Os dados,desenho,redação vetorial,código e exercícios são próprios. A placa e comparação pura/mistura são derivações do modeloJones apresentadas aqui,não reprodução de exemplo do livro. Ponte com dois níveis não é derivação da regra deBorn a partir de eletromagnetismo clássico. Revisão pessoal pendente.
