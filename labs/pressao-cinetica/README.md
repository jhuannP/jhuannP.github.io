# Pressão por colisões e segundos momentos

28/10/2026. Material original com apoio de IA, revisão pessoal pendente. Gás clássico diluído, massas iguais, paredes fixas e reflexão especular elástica. População homogênea/estacionária e simetria por inversão explicitadas para o argumento de feixes; não se demonstra equilíbrio a partir disso.

Uma molécula que chega à parede direita com v_x>0 muda seu momento em−2mv_x; a parede recebe+2mv_x. Um grupo de densidade n_i produz n_i S v_x Δt impactos médios. Impulso por tempo e área dá2mn_i v_x². Somar apenas incidentes e usar pares opostos de mesmo peso permite P_x=nm⟨v_x²⟩. O fator um terço adicional exige segundos momentos iguais nas três direções. Média de v_x nula não implica média de v_x² nula.

Seis velocidades±300e_x,±300e_y,±300e_z m/s, m=10⁻²⁶kg e V=6×10⁻²⁵m³: n=10²⁵m⁻³,⟨v_x²⟩=30000m²/s²,P_x=P_y=P_z=3000Pa e U_tr/V=4500J/m³. A população tem segundos momentos isotrópicos, mas não uma distribuição inteiramente isotrópica ou Maxwell. Três velocidades+300e_x e três−300e_x têm mesma energia, mas pressões normais9000,0,0Pa; a média das três continua3000Pa e não pode substituir cada componente.

P V=2U_tr/3 vale no recorte isotrópico para cinética translacional. Rotação, vibração e interações não estão em U_tr. Combinar com P=nk_B T requer o contexto de gás ideal em equilíbrio; não se mede temperatura termodinâmica de uma lista arbitrária pelo código. N é número de partículas,n=N/V densidade numérica, não mols.

## Código

`moments.py` usa int/Fraction, sem bool/float; massa/volume positivos e lista não vazia de vetores3D com parceiros opostos de mesma multiplicidade. Calcula matriz mΣv_i v_j/V e componentes normais, energia e média. A matriz é o segundo momento cinético de uma população sem fluxo médio neste modelo; não um cálculo completo de tensões de um fluido real. Não simula posições, impactos, colisões intermoleculares, termalização ou distribuição contínua.

Da raiz:

```sh
python3 labs/pressao-cinetica/moments.py
python3 -m unittest discover -s labs/pressao-cinetica -t .
```

Cinco testes: exemplo;64combinações de impulso/tempo de retorno de uma partícula livre em caixa retangular contra m v_x²/V;27pares de velocidades/162permutações dos eixos e identidade do traço/energia; anisotropia/escala de densidade; contratos. O voo livre de uma partícula é uma verificação independente do fator cinético médio, não dinâmica molecular de gás com interações.

## Fontes e limites

Nussenzveig, Curso de Física Básica,vol.II,5ªed.,Blucher2014 (edição previamente identificada). §11.3 pp.290–292/PDF291–293 por texto em28/10/2026; p.291/PDF292 renderizada e inspecionada visualmente para impulso e contagem de impactos. Parte de§11.2 na p.290 lida como contexto. Sem leitura integral, reprodução de figura/exercício ou distribuição do PDF. População, contraexemplo, figura e código próprios. Programa CCM0122 já mapeado, não reaberto neste bloco; versão efetivamente usada na turma não comprovada.

Distribuições contínuas, Maxwell, colisões intermoleculares, equilíbrio e caminho livre médio continuam pendentes. Revisão20min: derivar os dois fatores v_x, explicar a remoção do fator2 e a introdução de1/3, reconstruir3000Pa e refutar a pressão escalar no exemplo anisotrópico. Revisão pessoal não realizada pelo agente.
