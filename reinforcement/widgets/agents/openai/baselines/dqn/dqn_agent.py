from ..openai_agent import OpenAIAgent
from baselines import deepq


class DQNAgent(OpenAIAgent):
    name = 'DQN Agent (OpenAI Baselines)'

    def callback(self, lcl, _glb):
        # TODO: update orange progress

        # stop training if reward exceeds 199
        is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
        return is_solved

    def train(self, episodes, seconds, ow_widget, ow_widget_on_finish):
        total_timesteps = 100000

        total_timesteps = episodes

        deepq.learn(
            self.environment,
            network='mlp',
            lr=1e-3,
            total_timesteps=total_timesteps,
            buffer_size=50000,
            exploration_fraction=0.1,
            exploration_final_eps=0.02,
            print_freq=10,
            callback=self.callback
        )
