# Carga diante de plano aterrado

29/10/2026. Cenário ideal original para revisão de Jhuann; método padrão, sem reivindicação de descoberta, equipamento ou medição.

Plano infinitoz0,condutor ocupandoz≤0,aterradoφ0;vácuoz>0,carga realq≠0 em(0,0,a),a>0. Imagem−q em(0,0,−a)é ferramenta para calcular o exterior, não carga pontual real no metal. k=1/(4πε0) noSI;valoresk2,q3,a2 são unidades normalizadas compatíveis,não constantes do vácuo emSI. Singularidade da carga e interior são excluídos do cálculo externo.

φ=kq(1/r+−1/r−),r±²=x²+y²+(z∓a)². Na superfície,tangenciais cancelam eEz=−2kqa/(rho²+a²)^(3/2). Comnormal+z,σ=ε0Ez=−qa/[2π(rho²+a²)^(3/2)]. Código `surface` retorna **2πσ**,nãoσ,e carga total no disco de raioR:−q[1−a/sqrt(a²+R²)]. Ao levarR→∞,carga total−q. O condutor aterrado não é imposto neutro.

Força na carga real usa apenas campo induzido: Fz=−kq²/(4a²). Integração independente de anéis reais:deu1para0, u=a/sqrt(rho²+a²),dQ=qdu e contribuição de força kq²u³/a²du;integra−kq²/(4a²). Potencial induzido na carga=−kq/(2a). Energia configuracional,referidaaa→∞ e excluindo autoenergia pontual infinita,éU=−kq²/(4a)=qφind/2. A carga imagem muda quando a real muda;energia de dois pontos reais qφind não é a energia deste sistema.

Derivação deU:trabalho quase-estático externo desde infinito,ou montagem deq emaltura fixa,integrando potencial induzido proporcional à carga já inserida. Não se copia a carga imagem como uma segunda partícula física. Afastara2→4 comk2,q3 exige9/8 de trabalho externo;U inicial−9/4,final−9/8;força inicial−9/8. Fonte de aterramento ideal emV0,não circuito real/perdas/radiação.

## Código

`python3 -m labs.carga-plano.plane`

`python3 -B -m unittest discover -s labs/carga-plano -t .`

Potencial/campo/superfície emfloat finito,com limites de arredondamento e cancelamento perto deφ0. Não certifica entradas arbitrariamente extremas nem limite de precisão. Force_energy é referência exata int/Fraction,bool/float rejeitados. Geometria excluiz<0 eauto-campo,q0,a≤0,k≤0. Seis testes:exemplo;contorno eGauss;gradiente numérico em três pontos/três componentes;quadratura independente de anéis para três modelos;trabalho porquadratura/escalas;contratos. A quadratura cúbica de força é exata em aritmética ideal, não por isso toda quadratura é exata.

## Fontes

Feynman/Leighton/Sands,Lições de Física,volII,edição definitiva brasileiraBookman2008,§§6–7/6–8,pp6–9 a6–11/PDF92–94:consulta textual parcial29/10/2026;p6–11/PDF94 inspecionada visualmente para equações6.28–6.30 que não apareceram na extração textual. Início da seção seguinte sobre esfera aparece na mesma página, não desenvolvido. Sem leitura integral,figura ou exercício copiado,PDF privado não distribuído.

Versão oficial online,somente os mesmos trechos de método/plano: https://www.feynmanlectures.caltech.edu/II_06.html . Página exibe aviso inicial deJavaScript,mas corpo pertinente foi recuperado. NussenzveigIII foi pesquisado por nome do método sem localização confirmada; não lhe atribuir o recorte de imagens.

JúpiterCCM0212 reaberto29/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212 . Ativação15/07/2025,itens3(f,g),sem prova da versão ministrada2025/2 e sem versão da tentativa2024/2. Prova de contorno,integrações,energia,números efigura locais próprios;edições portuguesa e online não têm paginação intercambiável.

Próxima revisão20min:verificarφ0 no plano e calcularF/U,explicando fator1/2. Em outra sessão,integrarσ e a força de anéis. Placas finitas,condutor isolado,outras geometrias e revisão pessoal pendentes.
