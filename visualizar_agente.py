
import ale_py
import gymnasium as gym
import numpy as np

from agente import Agente
from config import ENV_ID


gym.register_envs(ale_py)


def carregar_agente():
    with np.load("resultados/melhor_agente.npz") as dados:
        agente = Agente()

        agente.W1 = dados["W1"].copy()
        agente.b1 = dados["b1"].copy()
        agente.W2 = dados["W2"].copy()
        agente.b2 = dados["b2"].copy()

    return agente


def visualizar_agente():
    agente = carregar_agente()

    env = gym.make(
        ENV_ID,
        obs_type="ram",
        render_mode="human"
    )

    recompensa_total = 0.0
    passos = 0
    acoes = {0: 0, 1: 0, 2: 0}

    try:
        estado, _ = env.reset()
        terminado = False

        while not terminado:
            acao = agente.agir(estado)
            acoes[acao] += 1

            estado, recompensa, terminated, truncated, _ = env.step(acao)

            recompensa_total += recompensa
            passos += 1
            terminado = terminated or truncated

    finally:
        env.close()

    print("\nRESULTADO DO MELHOR AGENTE")
    print(f"Fitness: {recompensa_total:.2f}")
    print(f"Passos: {passos}")
    print(f"Ações utilizadas: {acoes}")


if __name__ == "__main__":
    visualizar_agente()
