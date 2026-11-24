# Dois níveis, degenerescência e grandezas canônicas

Rascunho para revisão pessoal. Sistema finito em equilíbrio canônico,T>0,energias0/Δ>0 e degenerescências inteiras g0,g1 fixas. Não é ajuste de molécula,conjunto com interação,cinética,temperatura negativa ou experimento.

`probabilities(w,g0,g1)` recebe int/Fraction w∈[0,1],com w=exp(−Δ/kBT) no interior. Pontas0/1 são limites, não dois valores finitos de temperatura para Δ>0. Degenerescências1..10^6. Resultado são populações dos níveis, não de cada microestado.

`thermodynamics(x,g0,g1)` usa x=Δ/kBT>0 finito. Logaritmo do quociente de pesos e softplus evitam exp(+x);resultados podem sofrer underflow a zero em frio extremo,não provar ocupação matematicamente nula em T>0. Retorna p,U/Δ,S/kB,C/kB,F/(kBT),logZ. Zero de energia no fundamental. Energia deslocada por constante muda U/F,mas não população,S/C. Espectro e degenerescências independentes de T são necessários à derivação de capacidade. Não chamamos o quociente de pesos de taxa.

Exemplo próprio:g0=1,g1=3,w1/3. Nível fundamental1/2,excitado1/2;cada excitado1/6. S/kB=ln2+(ln3)/2,acima da entropia de dois níveis agrupados ln2. Se energia livre efetiva já incluiu degenerescência,não multiplicar por g novamente. Aqui F é Helmholtz canônica;ΔG° de enovelamento a pressão constante tem outro contexto,não conversão automática deste sistema.

## Fonte consultada em29/10/2026

David Tong,Statistical Physics,§1.3.1–1.3.3,recortes textuais de pesos/normalização,energia/flutuações/entropia e agrupamento por degenerescência. https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html . Leitura parcial das relações gerais;sem copiar exemplo de dois estados,N partículas,exercícios ou figuras. Deduções do modelo degenerado,figura e código próprios. Nenhum exemplar privado relido,oferta curricular/versão histórica atualizada ou formalização de domínio pessoal. Percurso complementar.

## Verificação

```sh
python3 -B -m unittest discover -s labs/boltzmann-degenerescencia -t .
python3 labs/boltzmann-degenerescencia/levels.py
```

Cinco métodos:27 enumerações racionais de microestados;16 estados contra soma direta de probabilidades,entropia e flutuação de energia;marcos;extremos/monotonicidade em oito estados;contratos. Verifica contas finitas,código e identidades termodinâmicas do modelo,não realidade física ou revisão pessoal. Painel anterior continua limitado a degenerescências iguais.
