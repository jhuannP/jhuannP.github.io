# Campo de um fio — circulação, simetria e raio finito

27/10/2026. Notas de aula originais com apoio de IA; rascunho e revisão pessoal pendente. Aula `f3-corrente-campo`, aprofundamento do material anterior; exemplo externo, Python e desafio iniciais preservados e com domínio explicitado. Não comprova experimento, competência pessoal ou conclusão da disciplina.

## Fontes e vínculo curricular

[Programa oficialCCM0212](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212), item5(a), reaberto em27/10/2026. Ativação15/07/2025, compatível com aprovação2025/2 sem provar a versão ministrada; tentativa2024/2 tem versão não recuperada. Estado acadêmico reutiliza panorama dos históricos, sem nova leitura desses documentos.

[FeynmanII, capítulo13](https://www.feynmanlectures.caltech.edu/II_13.html), consulta parcial §§13–2,13–4,13–5 em27/10/2026: corrente como fluxo de densidade, regime estacionário, circulação e fio longo externo. A edição online é explicitamente indicada na bibliografia oficial; não há paginação dePDF neste acesso. Tradução Bookman2008 foi localizada anteriormente no acervo, sem nova leitura ou distribuição doPDF. A referência usa o fator1/(ε₀c²), escrito aqui comoμ₀ noSI. Não transportar valores numéricos sem conferir unidades.

A consulta é parcial, não leitura integral dos capítulos13–15. Deduções para o interior uniforme, valores de exemplo, perfil e verificações são próprios; não se copiam enunciados ou figuras. O exemplo externo original não passa a ser fórmula válida dentro do condutor.

## Pergunta, orientação e derivação

Cilindro de raioa>0, eixo z, corrente axial estacionáriaI distribuída uniformemente. I positivo aponta para+z. Meio modelado porμ₀, sem campo externo imposto. Hipótese infinita aproxima trecho longe de pontas, se o retorno tiver contribuição desprezível. Uma corrente física precisa de circuito; as fontes de alimentação e o retorno não são resolvidos aqui.

Contorno circular concêntrico, percurso anti-horário visto de+z, normal+z. Simetrias e condições do sistema permitem campo azimutal constante ao longo desse círculo. Logo2πrBφ=μ₀I interna. Não é a escolha geométrica do contorno que cria essa propriedade.

Jz=I/(πa²), emA/m². Para0≤r≤a, integrar essa densidade no disco dáI interna=I r²/a². Para r≥a, toda a seção é incluída eI interna=I. Assim:

- Interior: Bφ=μ₀I r/(2πa²), incluindo o limite regular zero no eixo.
- Exterior: Bφ=μ₀I/(2πr).
- Superfície: as duas dãoμ₀I/(2πa), continuidade neste modelo volumétrico sem lâmina de corrente adicional.
- Módulo: trocarI por|I|; componenteBφ tem sinal. InverterI inverte o vetor.

O campo no eixo não foi obtido dividindo por r=0; é o limite da solução regular com a simetria do sistema. O modelo de fio sem raio é singular e não fornece o interior. ParaI≠0, o módulo cresce dentro e decresce fora, tendo máximo na superfície. Definindoρ=r/a,β=Bφ/[μ₀I/(2πa)] paraI>0:β=ρ dentro eβ=1/ρ fora. A figura representa o perfil da componente, não linhas de campo espaciais.

## Exemplo com unidades e contraexemplo

I=6A,a=2mm. Para as contas apenas, useμ₀/(2π)≈2×10⁻⁷T·m/A; é aproximação numérica, não definição exata. Emr=1mm, corrente interna1,5A,B≈300μT. Na superfície2mm,B≈600μT. Emr=4mm,B≈300μT. Os comprimentos foram convertidos para metros antes da substituição. Dois raios distintos podem dar o mesmo módulo e encerrar correntes diferentes.

ParaI>0, no ponto(x>0,y=0) o vetor está em+y; no ponto(x=0,y>0), em−x. Força sobre carga exige aindaq e velocidade; não basta conhecerB.

Dois fios de raios5mm, centrosx=−2cm e+2cm, correntes+3A e−3A: no ponto central, cada campo aponta+y e tem aproximadamente30μT; total60μT. Um contorno que envolve ambos tem corrente algébrica zero e circulação zero, emboraB não seja zero em cada ponto. Não retirar umB constante da integral para essa geometria total sem simetria adequada.

## Laboratório opcional

`wire.py` usa Python padrão eFraction. Entradas exatasint/Fraction, sembool,float oustring. a>0,r≥0; coordenadas cartesianas podem ter qualquer sinal. Corrente pode ser negativa ouzero. CalculaI interna e o campo reduzidob=B/[μ₀/(2π)] emA/m, não tesla. A conversão para tesla exige multiplicar pelo fator escolhido; não confundir valor reduzido com campoSI.

O vetor cartesiano evita a raiz: b=I(−y,x)/a² dentro; b=I(−y,x)/(x²+y²) fora. No eixo usa a expressão interna e dá(0,0). Emr=a ambas as expressões coincidem. Não calcula força, resistência, material magnético, correntes alternadas ou retorno.

```sh
python3 -m labs.campo-fio.wire
python3 -m unittest discover -s labs/campo-fio -t .
```

Cinco testes selecionados: corrente encerrada comparada à integração radial da densidade uniforme; circulação por integração numérica do vetor cartesiano; limites, reescala, sinais, exemplo e superposição; referência de Biot–Savart para segmento fino; contratos de domínio.

Na referência independente, um segmento fino−L≤z≤L dáB finito/B infinito=L/√(L²+r²). Comz=r tanθ, integra-se numericamenteI cosθ/(2r) para o campo reduzido. Comparação emL/r=1,2,5,20,100; em100 a diferença relativa até a solução infinita é menor que5×10⁻⁵. Isso verifica o campo externo no limite longo de uma linha fina; não resolve por integração um condutor de raio finito ou prova que qualquer fio real seja infinito. Integração numérica é evidência de implementação, não substitui a derivação.

## Resoluções e revisão

1. Fator externo0,5, com ambos os pontos fora.
2. A lei magnetostática não basta para todo campo variável no tempo.
3. Fração encerrada1/4 emr=a/2.
4. Corrente1,5A emr=1mm.
5. Campo300μT nesse raio interno.
6. Campo600μT na superfície.
7. Campo300μT emr=4mm.
8. Campo zero no eixo deste modelo.
9. Direção+y paraI>0 emx>0,y=0.
10. Circulação zero não exige campo local zero.
11. Dobrar raio interno dobraB se ambos os pontos continuarem dentro.
12. A forma circular do contorno não garante a simetria do campo.

Atividade20min: desenhar círculos e correntes encerradas, reconstruir300,600,300μT e explicar o contraexemplo. Proposta em papel, sem alegar aplicação com alunos. Registrar dúvidas e avaliação pessoal permanece a cargo deJhuann.

Pendentes: integrarBiot–Savart em outras geometrias, corrente não uniforme, materiais, forças sobre distribuições, dipolos, campos de retorno e transientes. Sete grupos curriculares seguem parciais e dois seguem lacunas; nenhum grupo é declarado completo.
