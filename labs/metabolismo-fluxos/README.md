# Integração metabólica: quantidade não é fluxo

Modelo original de estudo, assistido por IA, com revisão pessoal pendente. Todos os valores são prescritos; nenhum foi obtido de uma célula, tecido, aluno ou projeto de pesquisa.

## Estados e limites biológicos

A é a quantidade de G6P; Y é um estoque efetivo de resíduos de glicogênio de seis carbonos. Ambos em μmol de unidades de seis carbonos. Y não conta polímeros inteiros. Volume constante; 4 μmol em 2 mL equivalem a 2 mM. Se o volume mudar, concentração e quantidade exigem balanços diferentes.

Fluxos em μmol/min: entrada J, glicólise g=k_g A, fase oxidativa das pentoses p=k_p A, síntese s=k_s A e mobilização m=k_m Y. Constantes em min⁻¹. São taxas efetivas lineares, sem saturação, mecanismos completos, ajuste ou resposta hormonal. Síntese/mobilização são vias agregadas distintas, não ida/volta de uma reação elementar.

G1P, UDP-glicose, ramificações, transporte e retorno não oxidativo das pentoses estão omitidos. Recursos de ATP/UTP, NADP⁺, água e fosfato são externos e não limitantes no modelo; seu inventário não é fechado. Não inferir custo energético, produção líquida de ATP, eficiência, viabilidade fisiológica ou equilíbrio termodinâmico a partir desse balanço reduzido.

## Equações e referência de carbono

A′=J−g−p−s+m, Y′=s−m; portanto (A+Y)′=J−g−p. O carbono acompanhado em produtos é 3(2g)+5p+p=6(g+p) μmol C/min. A produção por passagem oxidativa é de uma pentose, um CO₂ e dois NADPH. A glicólise produz dois piruvatos por unidade de seis carbonos. A contagem de NADPH é produção da etapa, sem balanço redox completo.

Com J=12, k_g=2 e k_p=k_s=k_m=1, A*=Y*=4 μmol. Fluxos g=8, p=4, s=m=4; entrada e saída de carbono são 72 μmol C/min. Os estoques constantes não eliminam a circulação.

Contramodelos: dobrar J e todos os k mantém os estoques e dobra os fluxos; dobrar apenas todos os k mantém os fluxos estacionários e reduz os estoques pela metade. Não são estimativas de parâmetros de um sistema real.

## Fora da estação e estabilidade

Em A=2,Y=4, as derivadas são 8 e −2 μmol/min; carbono acumula a 36 μmol C/min. Euler com h=1/4 min dá A=4,Y=7/2. O código exige h≥0, h(k_g+k_p+k_s)≤1 e hk_m≤1, condição suficiente de positividade para quaisquer estoques não negativos; não recorta valores negativos. Isso não certifica erro pequeno em uma trajetória.

O sistema contínuo tem traço negativo e determinante k_m(k_g+k_p)>0 nas hipóteses declaradas, justificando estabilidade linear. A propriedade não foi confundida com homeostasia de um organismo ou estabilidade de qualquer discretização.

## Reproduzir

Da raiz do protótipo:

```sh
python3 labs/metabolismo-fluxos/fluxes.py
python3 -B -m unittest discover -s labs/metabolismo-fluxos -t .
```

Aritmética int/Fraction, sem bool/float. Entradas e estoques não negativos; k_g+k_p>0, k_m>0. Seis métodos de teste: marcos literais e alteração de uma saída; 72 modelos estacionários contra solução independente do sistema 2×2 por determinantes; 12 estados fora da estação com livro-caixa independente dos carbonos de produtos; três escalas de taxas/entrada; 36 passos de Euler com positividade e balanço de carbono; contratos.

## Fontes e alcance — 29/10/2026

[Júpiter CCM0111](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0111), reaberto diretamente, captura indicada de três semanas antes. Ativação 15/07/2024; item 18 trata regulação e integração metabólica. Vigência não prova execução integral pela turma. Situação pessoal no histórico preservada do panorama, sem reabertura dos documentos neste bloco.

Nelson/Cox, *Princípios de Bioquímica de Lehninger*, 6ª edição portuguesa 2014, original de 2013: abertura do cap.15, p.587/PDF617, e §15.1 pp.588–589/PDF618–619, recortes de integração, estado estável e regulação. As duas últimas páginas foram inspecionadas visualmente, incluindo a relação entre fluxo de entrada/saída e estoque. §14.5 p.575/PDF605, recorte textual da fase oxidativa; cap.1/PDF51, recorte textual de estacionariedade/equilíbrio. O PDF privado não é servido. Diagramas, parâmetros e problemas são próprios; sem imagens, tabelas ou exemplos clínicos copiados.

O recorte inicia a conexão de estados, fluxos e regulação; tecidos, lipídios, compartimentos, hormônios e balanços completos continuam pendentes. Não certifica domínio pessoal ou experiência experimental.
