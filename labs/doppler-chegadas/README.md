# Doppler por eventos de chegada

Rascunho didático para revisão pessoal e reforço escolar. Python opcional; não é medição sonora.

Meio homogêneo estacionário, som linear não dispersivo, propagação direita com rapidez c>0, movimentos colineares uniformes estritamente subsônicos. Fonte inicialmente em x=0, observador x=D>0. Velocidades assinadas u_s,u_o em relação ao meio, positivas para a direita. A crista n é emitida em t_e=n/f. Sua posição após emissão é x=u_s t_e+c(t−t_e). Igualar a x_o=D+u_o t dá t_a=[D+(c−u_s)t_e]/(c−u_o). Exigimos observador à frente da fonte no instante de emissão: D+(u_o−u_s)t_e>0. Assim a chegada ocorre depois da emissão nesta família. Não atravessar o encontro e reutilizar a fórmula para raios à esquerda.

T_obs=(c−u_s)/[f(c−u_o)], f_obs=f(c−u_o)/(c−u_s), λ_direita=(c−u_s)/f. Distância inicial altera atraso, não frequência em movimento uniforme. Não se confunde rapidez em relação ao meio com rapidez relativa ao observador.

Entrada em SI (m,s,Hz,m/s), int ou Fraction, índice n inteiro0..10000. Números prescritos:c300,f20,D120,u_s60,u_o−30. Chegadas4/11,2/5,24/55s, intervalo2/55s,f_obs55/2Hz. Mesma aproximação90m/s por u_s90,u_o0 dá200/7Hz, diferente. Não há choque, reflexão/eco, vento variável, amplitude, som gerado ou Doppler da luz. Não mede velocidade astronômica.

## Fontes lidas em29/10/2026

Nussenzveig,Curso de Física Básica2,5ªed Blucher2014,§6.9(a) pp.182–184/PDF183–185,consulta textual parcial;p184/PDF185 também visual para equações6.9.6–6.9.9 e distinção entre velocidades no meio e relativa. Sem leitura do cone de Mach,figuras/problemas copiados ou distribuição do PDF privado.

OpenStax Physics§14.3 https://openstax.org/books/physics/pages/14-3-doppler-effect-and-sonic-booms :recortes textuais de cristas/Eqs14.11–14.12 consultados parcialmente; não vídeos/experimentos/choques. A frase de Teacher Support que reduz o resultado à velocidade relativa não é adotada como geral: as próprias fórmulas e Nussenzveig distinguem os dois movimentos. A afirmação sobre comprimento de onda ao mover apenas o observador também não é usada para alterar o espaçamento no meio. A convenção algébrica local explicita essas diferenças. Figuras,números,código e exercícios originais. Percurso próprio,sem auditoria ou equivalência curricular brasileira.

## Verificar

```sh
python3 -B -m unittest discover -s labs/doppler-chegadas -t .
python3 labs/doppler-chegadas/events.py
```

Cinco métodos:75 eventos por encontro de trajetórias e diferenças de chegadas;nove combinações de frequência por espaçamento independente de cristas no mesmo instante;marcos e contraexemplo de mesma velocidade relativa;três distâncias;contratos e janela antes do encontro. Figura posição-tempo usa as trajetórias do modelo,com tempo crescendo para baixo. Não representa amplitude ou deslocamento das moléculas do ar. Testes não substituem revisão conceitual ou uso com aluno.
