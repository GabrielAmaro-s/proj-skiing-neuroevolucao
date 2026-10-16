# Neuroevolução no Atari Skiing

Projeto desenvolvido para a disciplina de Fundamentos de Inteligência Artificial, com o objetivo de implementar um algoritmo evolutivo capaz de otimizar os pesos de uma rede neural que controla um agente no ambiente `ALE/Skiing-v5`.

## 1. Implementação

O agente utiliza uma rede neural feedforward com a seguinte arquitetura:

- **Entrada:** 128 valores da memória RAM do Atari, normalizados entre 0 e 1.
- **Camada oculta:** 16 neurônios com ativação `tanh`.
- **Saída:** 3 neurônios correspondentes às ações NOOP, RIGHT e LEFT.

A ação é escolhida pelo maior valor produzido na camada de saída (`argmax`).

O algoritmo evolutivo utiliza:

- População de 20 agentes.
- 30 gerações.
- Seleção por torneio com 3 candidatos.
- Elitismo dos 2 melhores agentes.
- Reprodução por cópia dos pesos, sem crossover.
- Mutação por ruído gaussiano.

O fitness corresponde à recompensa acumulada durante cada episódio. Como as recompensas do Skiing são negativas, valores maiores (menos negativos) representam melhor desempenho.

## 2. Experimentos

Foram realizados três experimentos com diferentes configurações de mutação:

| Experimento | Taxa de mutação | Intensidade | Melhor fitness |
|---|---|---|---|
| A | 1% | 0,05 | -7902 |
| B | 10% | 0,20 | -6528 |
| C | 40% | 0,50 | -6528 |

Os experimentos B e C apresentaram o maior fitness observado.

Os históricos de cada execução e o gráfico comparativo estão disponíveis em `resultados/experimentos/`.

## 3. Comparação com agente aleatório

Foi implementado um agente que seleciona ações aleatórias, avaliado em cinco episódios.

| Métrica | Fitness |
|---|---|
| Média | -15901,60 |
| Melhor | -14364 |
| Pior | -16817 |

Os melhores episódios dos agentes evoluídos apresentaram recompensas superiores às observadas no agente aleatório.

Entretanto, a comparação é exploratória, pois não foram realizadas múltiplas execuções independentes de cada configuração evolutiva.

## 4. Resultados e limitações

Os experimentos demonstraram melhora do fitness ao longo do processo evolutivo.

Na visualização de um agente treinado, observou-se predominância da ação NOOP, indicando que a melhora na recompensa não necessariamente corresponde à aprendizagem de uma estratégia eficiente para ultrapassar as bandeiras.

A avaliação também está sujeita à aleatoriedade do ambiente, o que pode produzir recompensas diferentes para uma mesma rede neural.

## 5. Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o treinamento principal:

```bash
python main.py
```

Execute os experimentos A, B e C:

```bash
python experimentos.py
```

Execute a comparação com o agente aleatório:

```bash
python teste_aleatorio.py
```

Visualize o agente treinado:

```bash
python visualizar_agente.py
```

## 6. Arquivos de resultados

- `resultados/fitness.csv`: histórico do treinamento principal.
- `resultados/fitness.png`: gráfico de evolução do fitness.
- `resultados/melhor_agente.npz`: pesos do melhor agente do treinamento principal.
- `resultados/experimentos/fitness_A.csv`, `fitness_B.csv` e `fitness_C.csv`: históricos dos experimentos.
- `resultados/experimentos/comparacao.png`: comparação entre os experimentos.
- `resultados/experimentos/resumo.csv`: resumo dos resultados.
- `resultados/experimentos/melhor_agente_A.npz`, `melhor_agente_B.npz` e `melhor_agente_C.npz`: pesos dos melhores agentes de cada experimento.