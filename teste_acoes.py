
import gymnasium as gym
import ale_py

from config import ENV_ID

gym.register_envs(ale_py)


env = gym.make(
    ENV_ID,
    obs_type="ram",
    render_mode="human",
    repeat_action_probability=0.0
)

estado, info = env.reset(seed=42)

terminado = False
passos = 0
recompensa_total = 0.0

while not terminado:

    # O agente não vira para nenhum lado
    acao = 0

    estado, reward, terminated, truncated, info = env.step(acao)

    recompensa_total += reward
    passos += 1

    terminado = terminated or truncated

env.close()

print("Passos:", passos)
print("Fitness:", recompensa_total)
