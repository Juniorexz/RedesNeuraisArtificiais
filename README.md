# RedesNeuraisArtificiais
 Redes Neurais Artificiais são técnicas computacionais que apresentam um modelo matemático inspirado na estrutura neural de organismos inteligentes e que adquirem conhecimento através da experiência.

Características Gerais das Redes Neurais


Uma rede neural artificial é composta por várias unidades de processamento, cujo funcionamento é bastante simples. Essas unidades, geralmente são conectadas por canais de comunicação que estão associados a determinado peso. As unidades fazem operações apenas sobre seus dados locais, que são entradas recebidas pelas suas conexões. O comportamento inteligente de uma Rede Neural Artificial vem das interações entre as unidades de processamento da rede.

A operação de uma unidade de processamento, proposta por McCullock e Pitts em 1943, pode ser resumida da seguinte maneira:

    Sinais são apresentados à entrada;
    Cada sinal é multiplicado por um número, ou peso, que indica a sua influência na saída da unidade;
    É feita a soma ponderada dos sinais que produz um nível de atividade;
    Se este nível de atividade exceder um certo limite (threshold) a unidade produz uma determinada resposta de saída.

Esquema de unidade McCullock - Pitts.

Suponha que tenhamos p sinais de entrada X1, X2, ..., Xp e pesos w1, w2, ..., wp e limitador t; com sinais assumindo valores booleanos (0 ou 1) e pesos valores reais.

Neste modelo, o nível de atividade a é dado por:

a = w1X1 + w2X2 + ... + wpXp

A saída y é dada po

                    y = 1, se a >= t ou
                    y = 0, se a < t.

A maioria dos modelos de redes neurais possui alguma regra de treinamento, onde os pesos de suas conexões são ajustados de acordo com os padrões apresentados. Em outras palavras, elas aprendem através de exemplos.

Arquiteturas neurais são tipicamente organizadas em camadas, com unidades que podem estar conectadas às unidades da camada posterior.
Organização em camadas.
Usualmente as camadas são classificadas em três grupos:

    Camada de Entrada: onde os padrões são apresentados à rede;
    Camadas Intermediárias ou Escondidas: onde é feita a maior parte do processamento, através das conexões ponderadas; podem ser consideradas como extratoras de características;
    Camada de Saída: onde o resultado final é concluído e apresentado.

Uma rede neural é especificada, principalmente pela sua topologia, pelas características dos nós e pelas regras de treinamento. A seguir, serão analisados os processos de aprendizado.

Processos de Aprendizado


A propriedade mais importante das redes neurais é a habilidade de aprender de seu ambiente e com isso melhorar seu desempenho. Isso é feito através de um processo iterativo de ajustes aplicado a seus pesos, o treinamento. O aprendizado ocorre quando a rede neural atinge uma solução generalizada para uma classe de problemas.

Denomina-se algoritmo de aprendizado a um conjunto de regras bem definidas para a solução de um problema de aprendizado. Existem muitos tipos de algoritmos de aprendizado específicos para determinados modelos de redes neurais, estes algoritmos diferem entre si principalmente pelo modo como os pesos são modificados.

Outro fator importante é a maneira pela qual uma rede neural se relaciona com o ambiente. Nesse contexto existem os seguintes paradigmas de aprendizado:

    Aprendizado Supervisionado, quando é utilizado um agente externo que indica à rede a resposta desejada para o padrão de entrada;
    Aprendizado Não Supervisionado (auto-organização), quando não existe uma agente externo indicando a resposta desejada para os padrões de entrada;
    Reforço, quando um crítico externo avalia a resposta fornecida pela rede.

Denomina-se ciclo uma apresentação de todos os N pares (entrada e saída) do conjunto de treinamento no processo de aprendizado. A correção dos pesos num ciclo pode ser executado de dois modos:

    1) Modo Padrão: A correção dos pesos acontece a cada apresentação à rede de um exemplo do conjunto de treinamento. Cada correção de pesos baseia-se somente no erro do exemplo apresentado naquela iteração. Assim, em cada ciclo ocorrem N correções.

    2) Modo Batch: Apenas uma correção é feita por ciclo. Todos os exemplos do conjunto de treinamento são apresentados à rede, seu erro médio é calculado e a partir deste erro fazem-se as correções dos pesos.

Treinamento Supervisionado


O treinamento supervisionado do modelo de rede Perceptron, consiste em ajustar os pesos e os thresholds de suas unidades para que a classificação desejada seja obtida. Para a adaptação do threshold juntamente com os pesos podemos considerá-lo como sendo o peso associado a uma conexão, cuja entrada é sempre igual à -1 e adaptar o peso relativo a essa entrada.

Quando um padrão é inicialmente apresentado à rede, ela produz uma saída. Após medir a distância entre a resposta atual e a desejada, são realizados os ajustes apropriados nos pesos das conexões de modo a reduzir esta distância.Este procedimento é conhecido como Regra Delta.
Regra Delta

Deste modo, temos o seguinte esquema de treinamento.

Iniciar todas as conexões com pesos aleatórios;

Repita até que o erro E seja satisfatoriamente pequeno (E = e)

Para cada par de treinamento (X,d), faça:

Calcular a resposta obtida O;

Se o erro não for satisfatoriamente pequeno E > e, então:

Atualizar pesos: Wnovo := W anterior + neta E X

Onde:

    O par de treinamento (X, d) corresponde ao padrão de entrada e a sua respectiva resposta desejada;
    O erro E é definido como: Resposta Desejada - Resposta Obtida (d - O);
    A taxa de aprendizado neta é uma constante positiva, que corresponde à velocidade do aprendizado.

Esquema de treinamento do Perceptron.

As respostas geradas pelas unidades são calculadas através de uma função de ativação. Existem vários tipos de funções de ativação, as mais comuns são: Hard Limiter, Threshold Logic e Sigmoid.
