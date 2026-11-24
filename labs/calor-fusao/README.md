# Calor, capacidade e fusão: decidir a fase antes da temperatura

Modelo ideal fechado para matéria e adiabático, a pressão fixa, sem trabalhos além de pressão; evaporação e perdas desprezadas. Gelo inicial a 0°C; água e recipiente na mesma Tw, com 0≤Tw<100°C. c e L constantes. Usamos entalpia H=U+pV para a aproximação a pressão fixa: gelo a 0°C como referência zero e água a 0°C com H=L por kg. Não se afirma conservar U ignorando o trabalho de pressão.

Parâmetros adotados no exercício, sem transcrever tabela ou alegar medição: c=4200 J/(kg K), L=336000 J/kg, gelo 0,10 kg e água 0,20 kg. Com Ccal=0 e Tw=20°C, Edisp=16800 J e Efus=33600 J. Fundem 0,05 kg e sobram 0,05 kg de gelo; líquido final 0,25 kg, Tf=0°C. Com Tw=40°C funde exatamente tudo a 0°C. Com Tw=60°C sobra energia 16800 J após fusão, dando Tf=40/3°C. Com Tw=20°C e recipiente Ccal=210 J/K, fundem 0,0625 kg; sobra gelo 0,0375 kg e Tf=0°C.

Regra: Edisp=(ma c+Ccal)Tw e Efus=mg L. Se Edisp<Efus, massa fundida=Edisp/L e Tf=0. Caso contrário, todo gelo funde e Tf=(Edisp−Efus)/[(ma+mg)c+Ccal], inclusive zero na igualdade. Calor específico tem J/(kg K), capacidade térmica J/K. O recipiente à mesma temperatura inicial foi explicitado; outra temperatura pede outro balanço.

Na raiz do site:

    python3 -m labs.calor-fusao.exact
    python3 -m unittest discover -s labs/calor-fusao -t .

Interface racional int/Fraction sem bool ou float. Gelo>=0, água>0, c/L>0, Ccal>=0 e faixa de Tw explícita. Cinco testes cobrem os três regimes, fronteira dos dois lados, recipiente, conservação de massa/entalpia em 72 configurações, sinais do calor, escala extensiva e contratos. O calor recebido pelo gelo inclui fusão e, quando todo ele funde, aquecimento da água formada; água inicialmente quente e recipiente perdem energia. O gráfico usa os parâmetros declarados e Ccal=0.

Exemplo, código e desafio anteriores sem transição preservados. Aula f2-calor ampliada para onze seções/doze exercícios, assistida por IA para revisão pessoal. Próxima revisão: justificar por que uma média sem calor latente escolhe fase errada para Tw=20°C. Gelo abaixo de zero, evaporação/ebulição, pressão variável, capacidades variáveis, perdas e tempo de equilíbrio não foram desenvolvidos; grupo curricular permanece parcial.

Fontes consultadas parcialmente por texto em 22/10/2026: Nussenzveig, Curso de Física Básica vol.2, 5ª ed., §8.2 pp.207–209 (PDF208–210), capacidade e calorímetro. Cabeçalhos confirmam paginação impressa, sem nova inspeção visual. [OpenStax vol.2 §1.5](https://openstax.org/books/university-physics-volume-2/pages/1-5-phase-changes) fundamenta mudança de fase/calor latente, com valores tabelados distintos dos parâmetros de exercício aqui adotados. Contas, figura, exercícios e código próprios; nenhum PDF privado reproduzido. Não é resultado de pesquisa ou domínio pessoal certificado.

Verificação: cinco testes novos e 13 de catálogo aprovados; 545 estruturas MathML conferidas. No navegador em 390 px, gráfico e fórmula legíveis; questão da massa fundida rejeitou 0,10 e aceitou 0,05 com vírgula decimal. Largura igual à tela e nenhum erro de console observado. Prévia: calor-fusao-mobile.jpg. Suíte global e demais painéis não foram revalidados integralmente. Catálogo: 501 aulas/3158 exercícios em rascunho. Saldo semanal após bloco: 91%; parada em 65%.
