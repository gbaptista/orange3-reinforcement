import gym
import numpy as np

from Orange.util import Reprable

from .agent_train_mixin import AgentTrainMixin
from .agent_play_mixin import AgentPlayMixin


class Agent(AgentTrainMixin, AgentPlayMixin, Reprable):
    enviroment_id = None
    enviroment = None

    ow_widget = None
    ow_widget_on_finish = None

    _executor = None

    def __init__(self, enviroment_id):
        self.enviroment_id = enviroment_id
        self.enviroment = gym.make(self.enviroment_id)
        self.train_results = np.empty(0)
        self.initial_train_results = np.empty(0)

    def prepare_to_pickle(self):
        self.ow_widget = None
        self.ow_widget_on_finish = None
        self._executor = None
