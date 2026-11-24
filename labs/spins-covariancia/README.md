# Correlação estática de dois spins

Dois spinsσ1,σ2=±1 com UMA ligação:H=−Jσ1σ2−h(σ1+σ2),T em energia(kB=1). N=2,M=σ1+σ2 adimensional. Não é `ising_ring(2)`:o anel existente exigeN≥3e contaria outra topologia. AnelN4/snippet antigo preservado. Rascunho assistido porIA,revisão pessoal pendente;sem dado experimental ou dinâmica.

Na raiz:

```sh
python3 -B -m labs.spins-covariancia.pair
python3 -B -m unittest discover -s labs/spins-covariancia -t .
```

Entradas positivas int/Fraction:a=exp(2J/T),b=exp(2h/T). a/b são odds prescritos, não energias ou campos. Pesos(++, +−, −+, −−) proporcionais a(ab²,b,b,a),obtidos multiplicando todos os pesos físicos pelo mesmo fator. Não confundir sua soma com partição física sem desfazer esse fator dependente do campo. `moments`normaliza e calcula correlação conectadaC12=⟨σ1σ2⟩−⟨σ1⟩⟨σ2⟩,variâncias locais eVarM. `response`retorna derivada emh e resposta por spin,além do elemento fora da diagonalC12/T;temperatura positiva em energia.

Campo0,b1:para a1/3,1,3,as covariâncias são−1/2,0,+1/2 eVarM1,2,3. EmT2,a resposta total é1/2,1,3/2. Resposta por spin divide por2. Coma3,probabilidades3,1,1,3sobre8,⟨M⟩0,VarM3. Aumentar flutuação não produz magnetização média não nula em campozero nesse sistema simétrico finito.

IdentidadeVarM=Varσ1+Varσ2+2C12,como caso deΣijCij. Campo comum permiteχtotal=VarM/T. Campo localhj dá∂⟨σi⟩/∂hj=Cij/T;fora da diagonal pode ser negativo,mesmo que resposta total a campo comum seja não negativa. Para magnetização por spinm=M/2,a resposta éVarM/(2T)=2Var(m)/T,nãoVar(m)/T. Não converter automaticamente para unidades de material real,volume ou convenção magnética.

Cinco testes:três referências;25casos exatos de soma/reflexão;27comparações com canonical existente e derivada central no campo físico;cinco limites independentes por outro laboratório e topologia;exemplo/desafio/contratos antigos. statmech.py eparamagneto-finito/spin.py reutilizados sem alteração. Não foi criado novo motor canônico genérico. As diferenças centrais não provam relação de resposta para toda entrada.

Derivação finita da probabilidade dá∂hp_s=p_s(M_s−⟨M⟩)/T;as hipóteses incluemTfixo,H0eMsem dependência adicional deh. Não confundir derivada emh com derivada em b (odds). Correlação aqui é de equilíbrio e entre partes,não autocorrelação temporal ou prova de causalidade em dados. Sem singularidade de transição de fase emT>0na soma finita positiva.

Fonte primária:DavidTong,StatisticalPhysics§1.3.1E1.20–1.22 e§5.2E5.192–5.194,corpos parcialmente consultados30/10/2026, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html e https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S5.html . Definição/normalização e energiaIsing;trechos de campo médio/criticalidade/correlação espacial vistos na busca não desenvolvidos ou copiados. Fonte usaBcomo parâmetro de energia;notaçãohlocal explicita convenção. Par de uma ligação,covariâncias,figura e código locais;semPDFprivado.
