
import gymnasium as gym
import ale_py

from config import ENV_ID

gym.register_envs(ale_py)


def avaliar(agente):
    env = gym.make(ENV_ID, obs_type="ram")

    try:
        estado, _ = env.reset()
        recompensa_total = 0.0
        terminado = False

        while not terminado:
            acao = agente.agir(estado)

            estado, recompensa, terminated, truncated, _ = env.step(acao)

            recompensa_total += recompensa
            terminado = terminated or truncated

        return recompensa_total

    finally:
        env.close()
