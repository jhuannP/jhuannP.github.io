# LayerNorm: eixos, epsilon e gradiente

Notas originais,28/10/2026. Referência pública: PyTorch LayerNorm, https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html . stable redirecionou para2.15;consulta parcial à definição,eixos finais,divisorN,parâmetros afins e uso de estatísticas da entrada em treino/avaliação. Sem instalar/executar PyTorch ou presumir versão local. Exemplo,deduções,figura e rotina de gradiente próprios;sem nova leitura de livro privado.

Operação vetorial isolada,1–100componentes,reais de módulo≤1e6,epsilon de1e−12 a1e6;sem rede completa,tensores gerais,estado de otimizador ou estatísticas móveis. Cada linha deve ser chamada separadamente para normalizar o último eixo de uma matriz. Não foi incorporada à MLP ou ao treinoXOR.

Da raiz: `python3 -m unittest discover -s labs/layernorm-eixos -t .`; `python3 labs/layernorm-eixos/norm.py`.

Quatro testes:fixture/constante,invariantes,40vetores para diferenças centrais de dx/dgamma/dbeta(420componentes),contratos. Derivada fornecida é VJP de uma perda escalar,com upstream fixo. Soma dx≈0 reflete invariância a deslocamento comum,não ausência de aprendizado. Não oferece análise certificada de arredondamento extremo nem validação de generalização.

Revisão20min:para x=(1,3),eps3,reconstrua μ2,var1,s2,z=(−1/2,1/2),variância1/4;depois aplique gamma(2,4),beta(1,0),obtendo y=(0,2). Com upstream(1,0),gammaunitário,obtenha dx=(3/16,−3/16). Revisão pessoal e uso numa rede permanecem pendentes.
