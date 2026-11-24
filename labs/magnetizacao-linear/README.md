# Magnetização linear: B,H e correntes ligadas

28/10/2026.Material original com apoio de IA,revisão pessoal pendente. Magnetostática,meio uniforme linear isotrópico e solenoide infinito. Não é bobina finita,material medido,ferromagneto com histerese ou origem quântica dos momentos.

M é densidade de momento magnético,A/m. Correntes ligadas: j_b=∇×M em A/m² e K_b=M×n̂ em A/m. M uniforme pode ter j_b=0 e K_b não nulo. Na lateral de cilindro magnetizado em+z,K_b aponta em+φ. Definir H=B/μ₀−M dá∇×H=j_livre. Isso não permite afirmar que H em qualquer geometria dependa só da corrente livre: contornos e∇·H=−∇·M importam.

Sob constitutiva M=χ_m H,B=μ₀(1+χ_m)H. χ_m eμ_r=1+χ_m adimensionais. No solenoide ideal,simetria e laço dão H=nI. n1000m⁻¹,I2A,χ1/1000: H2000,M2,B/μ₀2002 A/m. χ−1/1000 dá M−2,B/μ₀1998. χ0 dá vácuo no modelo. Parâmetros didáticos sem identificação de material. A saída B/μ₀ não é B em teslas; nenhum valor numérico de μ₀ foi inserido.

A circulação de H num laço de comprimentoℓ é corrente livre nℓI; a de B/μ₀ inclui também Mℓ. Inverter I inverte H,M,B neste recorte,sem remanência. Não extrapolar χ constante a saturação,histerese,anisotropia ou todos os campos de uma amostra real.

Fonte privada: NussenzveigIII,2ªed.,Blucher2015,§11.1 pp.216–219/PDF217–220 e§11.2 pp.219–221/PDF220–222 parcialmente por texto; p.220/PDF221 visualmente inspecionada em28/10/2026. Correntes,definições,constitutiva e unidades. Edição posterior à1997do programa; versão efetivamente usada na turma não comprovada. Sem leitura integral ou cópia de figuras/exemplos/PDF. Programa oficial previamente mapeado,não reaberto neste bloco. Números,figura e código próprios.

Da raiz:

```sh
python3 labs/magnetizacao-linear/solenoid.py
python3 -m unittest discover -s labs/magnetizacao-linear -t .
```

int/Fraction,sem bool/float,n≥0,χ>−1. Corrente com sinal,permeabilidade relativa positiva. Quatro testes: exemplos;54combinações de densidade de espiras,corrente,χ e comprimento para Ampère livre/total;inversão/linearidade/vácuo;contratos. Não resolve interfaces ou testa dados de materiais. Modelos microscópicos,spin,momento angular,geometrias finitas e revisão pessoal pendentes.
