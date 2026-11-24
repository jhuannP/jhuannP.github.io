# Força e aceleração relativísticas

29/10/2026. Rascunho assistido por IA; revisão pessoal pendente. Pré-requisitos: cálculo, vetores, Lorentz e energia/momento.

## Modelo e roteiro

Massa invariante m>0 constante, referencial inercial, |v|<c, F=dp/dt com p=mγv. A força é tridimensional coordenada, não quadriforça ou transformação entre observadores. Deduza dγ/dt=γ³(v·a)/c² e depois F=mγa+mγ³(v·a)v/c². Separe as direções em relação à velocidade instantânea: F∥=mγ³a∥ e F⊥=mγa⊥. A inversa é a=[F−(F·β)β]/(mγ).

Exemplo vetorial prescrito: β=(3/5;0;0), F=(1;1;0) N, m=1 kg. γ=5/4; a=(64/125;4/5;0) m/s². Não há diferentes massas inerciais atribuídas a cada direção; há uma mesma massa e derivadas diferentes.

## Força constante a partir do repouso

F>0 ao longo de x, x(0)=0 e p(0)=0. q=Ft/(mc), γ=√(1+q²), β=q/γ, X=Fx/(mc²)=γ−1=q²/(γ+1) e A=ma/F=γ⁻³. Os retornos de `trajectory` são adimensionais; não confundir q com segundos ou X com metros. Para voltar às unidades: t=(mc/F)q, v=cβ, x=(mc²/F)X, a=(F/m)A.

|q|γ|β|X|A|
|---|---|---|---|---|
|0|1|0|0|1|
|3/4|5/4|3/5|1/4|64/125|
|4/3|5/3|4/5|2/3|27/125|

Conferências: K=mc²(γ−1)=Fx, dX/dq=β e dβ/dq=A. Para q pequeno, X≈q²/2 e β≈q. Uma força perpendicular a v tem potência nula naquele instante, mas pode mudar a direção do momento.

No movimento retilíneo, α=γ³|a|=F/m é a magnitude da aceleração própria. Com rapidez η=asinh q, c dη/dτ=F/m. Não generalizar esse resultado para forças vetoriais arbitrárias. A aceleração coordenada depende do referencial; ambas as definições devem ser explicitadas.

## Código e verificação

```sh
python3 labs/forca-relativistica/dynamics.py
python3 -B -m unittest discover -s labs/forca-relativistica -t .
```

`trajectory` usa biblioteca padrão e 0≤q≤10000 como limite didático. X racionalizado evita subtração de números quase iguais. `acceleration` usa vetores 3D e unidades coerentes de força/massa; β é sem dimensão. Sem motor, gravitação, radiação emitida ou integração de campos. Números prescritos não são observações.

Cinco métodos de teste: marcos racionais; sete valores por Decimal70; diferenças centrais em cinco instantes; derivada vetorial de p em18 combinações normalizadas com c=1 (três velocidades, três forças, duas massas); contratos. A derivada numérica é um caminho independente com tolerância, não prova universal ou validação experimental.

## Fontes realmente lidas

- Nussenzveig, Curso de Física Básica4, Ótica, Relatividade e Física Quântica, 2ªed., Blucher2014. Consulta parcial29/10/2026 ao fim de§6.9/início§6.10, p.176/PDF177: momento e F=dp/dt; página inspecionada visualmente porque equações estavam ausentes no OCR. Recorte textual de p.177/PDF178 sobre derivação da energia; equações dessa extração incompletas, não usadas como transcrição. pp.178–179/PDF179–180 só inspecionadas parcialmente como apoio/localização, sem nova conferência visual. Não lido capítulo integral, PDF privado não distribuído.
- [Feynman Lectures I, §15–8](https://www.feynmanlectures.caltech.edu/I_15.html#Ch15-S8), corpo parcialmente consultado29/10/2026, definição de dinâmica por momento e consequência de força constante. Abertura mostrava aviso JS junto do corpo; busca interna recuperou a seção. Trechos adotam massa histórica m(v)=γm₀; esta aula usa m invariante=m₀ da fonte. Sem copiar exemplos, números ou figura.
- [Programa CCM0222](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0222): consulta anterior27/10 mantida, item11; não reaberto neste bloco. Não comprova versão ministrada ou domínio pessoal.

Deduções por componentes, exemplos, figura e testes são próprios. Revisão pessoal e confrontação com dados reais pendentes. Não cobre gravitação, buracos negros ou transformação geral de forças; a próxima ponte para esses assuntos exige outros conceitos.
