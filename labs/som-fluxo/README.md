# Pressão,fluxo e energia acústica

Notas originais assistidas por IA,28/10/2026,revisão pessoal pendente.Não são medidas ou instrução de exposição sonora.

## Fontes e diferenças de notação

Nussenzveig,Curso de Física BásicaII,5ªedição2014/reimpressão2017,§6.3 pp.161–163/PDF162–164:recortes textuais consultados28/10 para pressão/deslocamento,potência e intensidade progressiva.Sem nova inspeção visual/leitura integral ou PDF servido.No livro u é deslocamento,nestas notas u é velocidade.
[OpenStaxUniversityPhysics1§17.3](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity):derivação de pressão,intensidade e onda progressiva consultada parcialmente28/10/2026.Não são adotados limites auditivos/números clínicos da fonte.Superposição,cálculos,figura e código próprios.Programa não reaberto nesta etapa;versão da turma não recuperada.

## Derivar

Acústica linear1D:ρu_t=−p′_x,p′_t=−ρc²u_x.Meio em repouso,homogêneo,adiabático,sem perdas.
p_R=Acos(kx−ωt);u_R=p_R/Z.p_L=Bcos(kx+ωt+φ);u_L=−p_L/Z,Z=ρc.Os sinais saem da equação de momento.
j=p′u=[p_R²−p_L²]/Z;J=(A²−B²)/(2Z).Para uma única onda:|J|=p_rms²/Z.Para duas,isso não vale com a pressão total.
Energia e=ρu²/2+p′²/(2ρc²).Sua conservação local segue das equações:∂e/∂t=−u p′_x−p′u_x=−∂(p′u)/∂x.A média das duas ondas é(A²+B²)/(2ρc²).Assim |J|≤c e_média.

## Exemplo sintético SI

ρ1kg/m³,c400m/s,Z400Pa·s/m,A2Pa.Uma onda:J0,005W/m²,u_pico0,005m/s,p_rms²2Pa².
Duas iguais:B2Pa,φ0.J0mas e_média0,000025J/m³.No antinó de pressão,pico4Pa,p_rms²8Pa²,u0.A conta8/400=0,020W/m² não é fluxo líquido.Nó de pressão:kxπ/2,pressão0,velocidade oscilante.Energia média total igual nos dois pontos.
A2/B1:J3/800=0,00375W/m²,diferente da soma dos módulos.

## Executar e interpretar

```sh
python3 labs/som-fluxo/acoustics.py
python3 -m unittest discover -s labs/som-fluxo -t .
```

Média em um período com amostras uniformes;fasesα=kx eτ=ωt em radianos.Campos em SI.A/B0–100Pa;ρ0,01–10⁴kg/m³;c1–10⁴m/s;fases de módulo≤10⁴;malha8–4096.Limites operacionais,não certificam linearidade para qualquer meio/pressão de equilíbrio.O programa não modela dispersão,absorção,ruído,incerteza ou campo próximo.
Testes:onda única,direção/unidades;contraexemplo estacionário;81combinações de amplitudes/fases versus médias analíticas e desigualdade;contratos.Sinais médios próximos de zero em float têm tolerância,não exatidão racional.

## Revisão20min

Derive o sinal das velocidades e o cancelamento cruzado.Calculе o exemplo,diferencie pressão/deslocamento/velocidade e explique energia positiva com fluxo líquido zero.Sem afirmar que uma leitura de pressão sozinha separa ondas incidentes e refletidas.Pendentes:campos reais,reflexão/eco,absorção e revisão pessoal.
