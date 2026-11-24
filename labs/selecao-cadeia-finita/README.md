# Seleção, mutação e uma população finita por várias gerações

Extensão original assistida por IA; revisão de Jhuann pendente. Reutiliza `labs/mutacao-selecao/cycle.py` via importlib,sem alterar esse laboratório. Não apresenta dados ou projeto antigo como concluído.

Haploides,M cópias constantes,um locus/dois alelos,pesos1+s e1,seleção→mutaçãoA→a→binomial. Sem fonte deA. `matrix`:M1…8,s0…10,μ0…1;int/Fraction,sem bool/float. Vetor de lei temM+1 pesos não negativos somando1. `history` propaga vetor-linha0…20 gerações. `summary` retorna média/variância,CDF de perda,sobrevivência e média entre sobreviventes(None se probabilidadezero). Zero absorvente permite interpretarπt(0)comoPr(τ0≤t);não transportar isso para modelos com mutação reversa.

Exemplo prescritoM4,s1,μ1/4,P0=1/4:primeira lei(2401,4116,2646,756,81)/10000. ValoresF(k/4):0,3/10,1/2,9/14,3/4. E[P2]=62091/200000=.310455,distinta deF(E[P1])=9/26. Na geração8,média≈.200372425,perda acumulada≈.648753817. Figura original conecta pontos discretos;sem sorteios/semente/MonteCarlo.

Prova própria:paraμ>0,F(p)≤1−μ,entãoT_i0≥μ^M em todos os estados. Condicional a qualquer história sobrevivente,chance de continuar≤1−μ^M. LogoPr(τ0>t)≤(1−μ^M)^t→0,Eτ0≤μ^(−M),E[P_t]≤Pr(τ0>t)→0. Não usa independência entre gerações. ParaM4,μ1/4,limite deEτ0 é256,sem afirmar igualdade/prazo individual. Paraμ0 a prova não conclui perda certa deA. Modelos grandes e limites de tempo não intercambiados sem prova.

## Executar da raiz do protótipo
```sh
python3 -m labs.selecao-cadeia-finita.chain
python3 -B -m unittest discover -s labs/selecao-cadeia-finita -t .
```
Seis métodos:marcos/média não fechada;16 modelos com enumeração de histórias completas de duas gerações (M1…4×s0/1×μ0/1/4),contribuições individuais normalizadas independentemente;momentos condicionais e variância total;36 modelos de absorção (M1…6×s0/1×μ1/4,1/2,1)comseis passos,limites/CDF/primeiro ingresso/sobreviventes;quatro casos neutros de média constante/fronteiras;contratos. Testes finitos verificam código,a demonstração dá o limite geral. Não resolve tempos médios por inversão de matriz ou compara algoritmos de simulação.

## Fontes consultadas parcialmente em29/10/2026
- [JúpiterCCM0211](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211),reaberto,ativação15/07/2025:itens10,11b e13;turma ministrada não comprovada. Aprovação preservada e lacuna de produto audiovisual não preenchida por esta aula.
- [RickDurrett,ProbabilityModelsforDNASequenceEvolution](https://sites.math.duke.edu/~rtd/Gbook/PM4DNA_0317.pdf),2ªed.copyright2008,§1.2pp5–6/PDF14–15:recortes textuais da matriz binomial,condicionamento e fronteiras neutras;sem nova conferência visual/leitura integral. A fonte usa2N cópias em população diploide neutra,não o nosso cicloM haploide com seleção/mutação. Não copiar a chance neutra de fixação para o modelo seletivo. Busca também retornou trechos de difusão do capítulo7;não foram usados como corpo de fonte deste recorte.
- ThePrincetonGuidetoEvolution,CharlesF.Baer,IV.2Mutation,p317/PDF331:recorte textual reconferido no cache autorizado para discussão qualitativa de equilíbrio/finito. Copyright2014 previamente conferido difere de2013 do programa;sem nova inspeção visual ou transplantar fórmula com outra convenção de seleção. Modelo,prova,parâmetros,figura e exercícios locais próprios. PDF privado não distribuído.

Outros processos,migração,mutação reversa,diploidia,seleção sazonal/inferência e evidência empírica de Jhuann continuam pendentes. Uma lei propagada não é uma trajetória ou medida biológica.
