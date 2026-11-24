# Atrito: testar o regime antes da fórmula

Notas, parâmetros, figura e código originais assistidos por IA para revisão pessoal. Percurso próprio de reforço, sem equivalência integral a uma grade brasileira.

Bloco pontual de massa m sobre piso horizontal fixo, sem aceleração vertical, força aplicada horizontal F. N=mg apenas sob essas condições. Modelo seco ideal com 0≤μk≤μs. Se v=0, testar f necessário=−F e |F|≤μsN; no limite, repouso permanece admissível e o código escolhe esse ramo. Se limite excedido, início no sentido F e atrito cinético contrário. Se v≠0, f=−μkN sign(v), mesmo se F for menor que o limite estático. v é relativa ao piso.

Parâmetros escolhidos: m4kg,g10m/s²,μs0,5,μk0,3. N40N,limite20N,cinético12N. F10/v0→f−10,a0;F24/v0→f−12,a3;F10/vpositivo→f−12,a−0,5. F10/vnegativo→f+12,a+5,5. Não inferir movimento só de F.

Sem empurrão e inicialmente v6m/s: a−3m/s² até t2s,distância6m. Trabalho de atrito−72J e energia inicial72J. Ao parar,reavaliar ramo estático;não prolongar a aceleração cinética para inverter artificialmente o movimento. O código só calcula força/aceleração local e NÃO integra a trajetória. Potência f v≤0 para piso fixo;isso não é teorema sobre trabalho de atrito estático em todo sistema com apoio móvel.

```
python3 -m unittest discover -s labs/atrito-escolar -t .
python3 labs/atrito-escolar/contact.py
```
Somente int/Fraction,sem float/bool;aritmética exata dos valores idealizados,não precisão de medição. Testes de limiar,dependência da velocidade,243pares de reflexão/dissipação e contratos. Contato perdido,inclinação,rolamento,fluido e atrito dependente de velocidade fora do modelo.

## Referências e alcance — consulta parcial em28/10/2026

- Nussenzveig, Curso de Física Básica1:Mecânica,5ªed2013,reimpressão2017 confirmadas em folha de rosto/PDF4 e copyright/PDF5. §5.2(ii) pp.115–117/PDF116–118 parcialmente consultadas por texto para leis empíricas,ajuste estático,cinético e limites. Sem nova inspeção visual ou leitura integral;exercícios,figuras e tabelas não reproduzidos. Exemplar privado autorizado,não servido no site.
- OpenStax College Physics for AP Courses2e §5.1: https://openstax.org/books/college-physics-ap-courses-2e/pages/5-1-friction — consulta parcial aos modelos e desigualdade estática. Não copiamos tabelas ou exercícios;coeficientes escolhidos sem atribuição a um material real. Primeira tentativa de Physics/5.1 indisponível,não é fonte lida.

Pendentes:incerteza e ensaios reais,planos inclinados,sistemas com mais corpos,rolamento e revisão de Jhuann. A fonte universitária foi adaptada ao nível escolar;Python é opcional e não é pré-requisito.
