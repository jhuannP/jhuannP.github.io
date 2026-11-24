# Gravitação: energia específica e regime

Modelo newtoniano original, massa central dominante e fixa, μ=GM>0, sem arrasto, propulsão ou relatividade. Raio r é distância ao centro; para esfera, usar somente região externa r≥R. Valores sintéticos em unidades coerentes; não são constantes terrestres.

`circular` devolve **quadrados** v²,ℓ²,v_escape² e **T²/(4π²)**, além de energias por massa K/m,U/m,E/m. Não devolve velocidade, momento angular ou período diretamente. Int/Fraction, μ/r positivos. Em SI: μm³/s², rm, energias específicasm²/s², ℓm²/s, período s.

μ8,r2: v²4,K/m2,U/m−4,E/m−2,ℓ²16,T²/(4π²)=1,v_escape²8. r8: energia específica−1/2, velocidade ao quadrado1,período8vezes o anterior. Isso compara dois estados circulares,não simula transferência ou custo de combustível.

`surface_change(8,2,1/5)`: variação exata4/11 versus aproximação2/5, erro relativo+1/10. Para z=0, ambas0 e erro relativoNone, não0/0. Modelo de superfície usa R2 em exemplo separado, sem alterar o raio circular anterior.

` specific_energy` calcula estado radial/tangencial genérico; energia negativa não certifica circularidade. O teste de energia zero usa componentesvr2,vt2 para v²8; não é lançamento puramente tangencial. O corpo deve seguir trajetória externa sem colisão para interpretar escape ideal. Inward radial collapse não é resolvido aqui.

Da raiz: `python3 -B -m unittest discover -s labs/gravidade-energia -t .` e `python3 labs/gravidade-energia/orbit.py`.

Fontes locais parcialmente consultadas30/10/2026: NussenzveigI,5ªedição2013/reimpressão2017,§7.5pp176–177/PDF177–178,§10.6p245/PDF246; p177/PDF178inspecionada visualmente. [JúpiterCCM0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0112),item10,ativação15/07/2024,posterior à aprovação2023/2;versão ministrada não comprovada. Exemplos,código,figura e testes locais;sem cópia de atividade/figura ouPDFprivado. Revisão pessoal pendente.
