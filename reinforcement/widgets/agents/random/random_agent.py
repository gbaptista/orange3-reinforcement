from ..agent import Agent


class RandomAgent(Agent):
    name = 'Random Agent'

    def train_action(self, state):
        return (self.play_action(state), {})

    def play_action(self, _state):
        return self.enviroment.action_space.sample()
