import gym
import numpy as np

from Orange.util import Reprable

from .agent_train_mixin import AgentTrainMixin
from .agent_play_mixin import AgentPlayMixin


class Agent(AgentTrainMixin, AgentPlayMixin, Reprable):
    environment_id = None
    environment = None

    memory = None
    initial_memory = None

    ow_widget = None
    ow_widget_on_finish = None

    _executor = None

    def __init__(self, environment_id):
        self.environment_id = environment_id
        self.environment = gym.make(self.environment_id)

        self.train_results = np.empty(0)
        self.initial_train_results = np.empty(0)

        self.memory = {}
        self.initial_memory = {}

    def make_enviroment(self):
        self.environment = gym.make(self.environment_id)

    def prepare_to_pickle(self):
        self.ow_widget = None
        self.environment = None
        self.ow_widget_on_finish = None
        self._executor = None
