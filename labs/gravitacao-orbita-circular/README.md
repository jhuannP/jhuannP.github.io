# Gravitação e círculo orbital

Rascunho original para reforço escolar. Use papel,calculadora e diagrama;Python não é pré-requisito. `python3 orbit.py` executa os cinco testes opcionais,sem bibliotecas adicionais.

## Modelo

Campo newtoniano exterior de corpo esférico,μ=GM,corpo central aproximado fixo por m≪M. Órbita circular sem atmosfera,propulsão,rotação ou outros corpos. r=R+h é distância ao centro. g=μ/r² e F=mg. A resultante centrípeta é a gravidade,não outra força a ser somada: μm/r²=mv²/r. Logo v=√(μ/r),T=2πr/v e T²=4π²r³/μ. A justificativa geométrica de v²/r usa pequenos arcos e mudanças vetoriais de velocidade,com limite indicado para aprofundamento.

Exemplo sintético:μ4,0×10¹⁴m³/s²,R6,0×10⁶m,h4,0×10⁶m,m500kg. r10⁷m,g4m/s²,F2000N,v6324,555m/s e T9934,588s. Não são valores adotados da Terra. Dobrar m dobra F,sem mudar g/v/T no modelo. Dobrar r dá fatores1/4,1/√2,2√2 para g,v,T. O raio e a velocidade não podem ser escolhidos livremente e ainda descrever o mesmo círculo gravitacional.

Na queda livre conjunta,a balança ideal pode ficar sem compressão mesmo com gravidade atuando. Distinguimos força gravitacional e força normal de apoio. Não modelamos marés,contato,arrasto ou o interior de um planeta. Ação/reação atua em corpos diferentes;fixar o corpo central é aproximação,não ausência de reação.

## Código opcional

A parte algébrica usa SI,com parâmetros finitos positivos e h≥0. Sinaliza saídas inválidas ou fora da faixa numérica;isso não garante precisão para quaisquer parâmetros extremos. O integrador separado usa unidades normalizadas μ=1,r=1,v=1 e estado inicial(1,0,0,1). Resolve a aceleração vetorial por RK4 e compara com a solução circular analítica após2π. Não possui eventos de colisão ou integração de outras geometrias,energia orbital geral,relatividade ou observações.

A figura mostra o satélite à direita,velocidade para cima e força para o centro. É um diagrama instantâneo,sem escala,não uma fotografia ou medição. A gravidade fornece a resultante centrípeta.

## Fontes parcialmente consultadas em27/10/2026

- [OpenStax Physics§7.2](https://openstax.org/books/physics/pages/7-2-newtons-law-of-universal-gravitation-and-einsteins-theory-of-general-relativity): recortes da lei de Newton,direção,massas e distância ao centro. Não reproduzidos exemplos numéricos,figuras ou a discussão de relatividade geral.
- [OpenStax Physics§7.1](https://openstax.org/books/physics/pages/7-1-keplers-laws-of-planetary-motion): condições do sistema e relações orbitais,recortes. Derivação nesta aula restrita ao círculo,sem tratar toda órbita como circular ou demonstrar as três leis gerais.

Texto,deduções,numeração,exercícios,código e figura próprios. Não consultada matriz brasileira ou prova específica neste bloco;sem alegar cobertura de vestibular ou equivalência curricular. Sem experimento,observação astronômica ou resultado da IC. Revisão pessoal e uso com aluno pendentes.

## Verificações e próxima ação

Cinco testes:exemplo/unidades;24pares raio/massa com escalas/identidades;três refinamentos RK4 contra círculo analítico após uma volta,conservação aproximada do raio e queda do erro;direções/perpendicularidade;contratos. Erros medidos são deste caso,sem garantia global de tolerância. Teste numérico não valida uma órbita real.

Em20min,desenhe R+h,force a distinção entre velocidade e força,derive v²=μ/r e reconstrua os fatores de massa/raio. Depois explique como ausência de apoio pode coexistir com gravidade. Windows real e leitor de tela não testados.
