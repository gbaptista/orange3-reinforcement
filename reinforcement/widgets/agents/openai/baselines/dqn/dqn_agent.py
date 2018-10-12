from baselines import deepq

from ..openai_agent import OpenAIAgent


class DQNAgent(OpenAIAgent):
    name = 'DQN Agent (OpenAI Baselines)'

    def learn_iteration_callback(self, lcl, _glb):
        if(self.should_keep_learning()):
            # TODO:
            # is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
            # result = self.train_episode()
            # self.train_results = np.append(self.train_results, result)

            self.update_progress()

            return False
        else:
            self.on_finish(self)

            return True

    def start_learning(self):
        total_timesteps = int((self.episodes + self.seconds)
                               * 2)

        deepq.learn(
            self.environment,
            network='mlp',
            lr=1e-3,
            total_timesteps=total_timesteps,
            buffer_size=50000,
            exploration_fraction=0.1,
            exploration_final_eps=0.02,
            print_freq=10,
            callback=self.learn_iteration_callback
        )
