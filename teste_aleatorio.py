
import ale_py
import gymnasium as gym
import numpy as np

from config import ENV_ID


gym.register_envs(ale_py)


def avaliar_aleatorio(seed):
    env = gym.make(ENV_ID, obs_type="ram")

    try:
        env.action_space.seed(seed)
        estado, _ = env.reset(seed=seed)

        recompensa_total = 0.0
        terminado = False

        while not terminado:
            acao = env.action_space.sample()

            estado, recompensa, terminated, truncated, _ = env.step(acao)

            recompensa_total += recompensa
            terminado = terminated or truncated

        return recompensa_total

    finally:
        env.close()


def main():
    resultados = []

    for seed in range(5):
        fitness = avaliar_aleatorio(seed)
        resultados.append(fitness)

        print(f"Execução {seed + 1}: Fitness = {fitness:.2f}")

    print("\nRESULTADO DO AGENTE ALEATÓRIO")
    print(f"Média: {np.mean(resultados):.2f}")
    print(f"Melhor: {np.max(resultados):.2f}")
    print(f"Pior: {np.min(resultados):.2f}")


if __name__ == "__main__":
    main()
