# Rotor: componente axial, impulso e trabalho

30/10/2026. Rascunho original para revisão de Jhuann.

Eixo z fixo inercial;coordenadasx/y são perpendiculares,I=Σm(x²+y²)>0. Entradas int/Fraction emSI. Corpos rígidos comIconstante:τz=Iα,Lz=Iω,K=Iω²/2; não se presumeLvetorial paralelo aω em qualquer eixo. Torque axial total constante,tempo≥0. ω com sinal;Δθ=ω0t+αt²/2,impulsoτt,trabalhoτΔθ,potênciaτω. Não modela mancal real,flexão ou atrito não declarado.

Exemplo original:duas massas1kg emx±2m,I8;ω0=1,τ4,t2→α1/2,ω2,Δθ3,Lz8→16,K4→16,impulso8,trabalho12,potência4→8 emSI. Partículas têm rapidez4m/s no final eK8Jcada. Eixo paralelo deslocado1m muda distâncias para1e3 eI10,não muda massas.

Rearranjo separadoI8→4,Lz8:ω1→2,K4→8,ΔK4. Apenas estados finais com velocidades radiais nulas. I muda duranteo rearranjo;não aplicarτ=Iα comIconstante;lei éτ=d(Iω)/dt. Conservação axial não implica conservação deK;trabalho interno/reservas podem importar. Sem trajetória ou esforço de rearranjo calculados.

Fonte:NussenzveigI5ªed2013/reimpressão2017,§12.1pp304–306/PDF305–307,recortes textuais30/10/2026;p305/PDF306visual. Sem cópia de exemplo/figura/PDFprivado. [JúpiterCCM0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0112),reaberto30/10,ativação15/07/2024 posterior à turma2023/2;versão ministrada não comprovada.

```sh
python3 labs/rotor-eixo/rotor.py
python3 -B -m unittest discover -s labs/rotor-eixo -t .
```

Cinco testes: referência/trêsbalanços;27casos com energia por velocidades de partículas,impulso/trabalho e integral da potência;geometria/eixo/escalas;27rearranjos e exemplos/desafio anteriores;contratos. Não é validação experimental,pessoal ou dinâmica tensorial.
