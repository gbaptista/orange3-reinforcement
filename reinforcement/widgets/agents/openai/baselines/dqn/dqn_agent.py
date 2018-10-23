import numpy as np

from baselines import deepq

from ..openai_agent import OpenAIAgent


class DQNAgent(OpenAIAgent):
    name = 'DQN Agent (OpenAI Baselines)'

    def callback(self, local_variables, global_variables):
        return not self.keep_running

    def step_callback(self, new_state, reward, done, info):
        if done:
            train_result = {'steps_to_finish': self.steps_to_finish,
                            'total_reward': self.total_reward,
                            'last_action_info': {}}

            self.train_results = np.append(self.train_results, train_result)

            self.update_progress()

            self.keep_running = self.should_keep_learning()

            self.steps_to_finish = 0
            self.total_reward = 0.0

        self.steps_to_finish += 1
        self.total_reward += reward

    def start_learning(self):
        # TODO:
        total_timesteps = (self.episodes + self.seconds) * 1000

        self.keep_running = True

        self.steps_to_finish = 0
        self.total_reward = 0.0

        load_path = self.previous_results_load_path()

        def callback(local_variables, global_variables):
          return self.callback(local_variables, global_variables)

        def step_callback(new_state, reward, done, info):
          self.step_callback(new_state, reward, done, info)

        self.act = deepq.learn(
            self.environment,
            network='mlp',
            lr=1e-3,
            total_timesteps=total_timesteps,
            buffer_size=50000,
            exploration_fraction=0.1,
            exploration_final_eps=0.02,
            print_freq=None,
            load_path=load_path,
            callback=callback,
            step_callback=step_callback
        )

        if load_path:
          remove(load_path)

        self.save_results()

        self.task_on_finish(self)
