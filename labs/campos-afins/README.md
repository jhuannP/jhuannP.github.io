# Campo afim: valor, derivadas e quatro arestas

Laboratório original e sintético, coordenadas cartesianas abstratas. `Affine(A,b)` representa F(r)=Ar+b no plano, incorporável em3D com Fz=0 e sem dependência de z. `operators()` dá divergência e componente z do rotacional; não são componentes do próprio campo.

`F=(2x−3y+1,x−y+2)`: F(1,2)=(−3,1), div1,curlz4. Quadrado[0,2]²:fluxo externo4,circulação anti-horária16. Soma pelas quatro arestas usa ponto médio, exato somente porque o campo é afim em cada aresta; não é integrador genérico para campos curvos. Side>0,int/Fraction,sem diferenças finitas no algoritmo.

`quadratic_gradient(a,b,c,p)` para phi=a*x²+b*x*y+c*y²; derivada central é exata para o polinômio quadrático nos testes, não garantia para funções gerais.

`vortex(p)=(-y/r²,x/r²)` rejeita a origem. Produto com derivada da parametrização circular por ângulo(-y,x)é1: integral0..2π=2π. A função não implementa cálculo simbólico do rotacional; curl0fora da origem é derivado na aula. Não atribuir curl0à origem ou aplicar Stokes ao disco que a contém.

Da raiz: `python3 -B -m unittest discover -s labs/campos-afins -t .` e `python3 labs/campos-afins/fields.py`.

Referências públicas parcialmente consultadas30/10/2026: [NIST DLMF1.6(iii)](https://dlmf.nist.gov/1.6#iii), E19–E22,E29–E30; [DLMF1.5(i)](https://dlmf.nist.gov/1.5#i), derivadas parciais, regra da cadeia e igualdade de mistas sob regularidade. Exemplos, contas de arestas, testes e figura locais. Sem transcrição de figura/exercício. Revisão pessoal pendente.
