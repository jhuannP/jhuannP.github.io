# van’t Hoff e Kirchhoff — laboratório original

K termodinâmico adimensional, mesma reação e mesmos estados padrão a pressão padrão fixa. ΔrG°=−RTlnK e dΔrG°/dT=−ΔrS° dão dlnK/dT=ΔrH°(T)/(RT²). A forma diferencial não exige ΔH constante; tirar ΔH da integral exige essa aproximação.

Com T0 e H0=ΔrH°(T0), Cp=ΔrCp° constante no intervalo, H(T)=H0+Cp(T−T0). Integrando:

ln[K(T)/K(T0)]=H0/R(1/T0−1/T)+Cp/R[ln(T/T0)+T0/T−1].

Exemplo próprio: T0=300K,T=400K,K0=2,H0/R=1200K. Para Cp=0,lnrazão=1 eK=2e≈5,43656. Para Cp/R=4,o incremento adicional é4[ln(4/3)−1/4]≈0,150728,logoK≈6,32099. Os parâmetros são sintéticos; não equivalem a uma reação real ou dado tabulado. Use valores calculados pelo script para arredondamentos.

```sh
python3 labs/vant-hoff-kirchhoff/equilibrium.py
python3 -m unittest discover -s labs/vant-hoff-kirchhoff -t .
```

Float,biblioteca padrão,R aproximado8,314462618J mol⁻¹K⁻¹. T/T0 entre200–1000K,|H0|≤200kJ/mol,|Cp|≤500J mol⁻¹K⁻¹,|lnK0|≤100 são limites didáticos do código,não domínio físico universal. O programa avalia lnK antes de exponenciar. log1p reduz perda ao formar ln(T/T0),mas não certifica estabilidade geral ou ausência de cancelamento no termo de Cp muito perto deT0.

Quatro testes:fixture sintética;36 integrais por Simpson contra fórmula e mudança de referência coerente emH;derivada central e inversão da reação;contratos. Quadratura e diferenças finitas são conferências,não prova universal. Nenhuma transição de fase,não idealidade,incerteza ou ajuste real modelados.

Fonte privada:Levine,Physical Chemistry,6ªed.,copyrightMcGraw-Hill2009 confirmado nas páginas iniciais do texto extraído(nome do arquivo diz2008). §6.3 pp.182–184/PDF200–202,consulta textual parcial29/10/2026,derivação,integral e efeito deCp. Sem nova inspeção visual ou leitura integral. Exemplo,dedução redigida,figura,código e exercícios próprios;sem copiar exemplo ou exercício do livro,sem distribuirPDF.

Complemento:[University of Washington,CHEM452§§6.2 e6.5](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/chemical_equilibrium.html),consulta parcial29/10/2026 sobreGibbs/K e temperatura. A convenção de pressão em trechos da página varia entreatm/bar;não transferida ao modelo. Reação/estado padrão precisam ser mantidos consistentes. Tentativa de abrir páginaCSUEastBay retornou502:não conta como leitura. Revisão pessoal pendente.
