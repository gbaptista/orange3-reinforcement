import numpy as np

import gym

from Orange.data import Table, Domain, StringVariable, ContinuousVariable

from Orange.widgets.utils.signals import Output

from .reinforcement_widget import ReinforcementWidget


class OWEnvs(ReinforcementWidget):
    id = "orange.widgets.reinforcement.envs"
    name = "Enviroments"
    description = "List of all available OpenAI Gym Enviroments."
    icon = "icons/list.svg"
    priority = 60
    category = "Reinforcement"
    keywords = ["OpenAI Gym", "Enviroment"]

    class Outputs:
        enviroments_table = Output("Enviroments", Table)

    def __init__(self):
        super().__init__()

        self.enviroments_table_output()

    def enviroments_table_output(self):
        domain = Domain(
            [
                ContinuousVariable("TimeStep Limit"),
                ContinuousVariable("Trials"),
                ContinuousVariable("Reward Threshold")
            ],
            None,
            [StringVariable("Enviroment Id")]
        )

        attributes = []
        metas = []
        for enviroment in gym.envs.registry.all():
            enviroment_id = enviroment.id

            timestep_limit = enviroment.timestep_limit
            trials = enviroment.trials
            reward_threshold = enviroment.reward_threshold

            attributes.append([timestep_limit, trials, reward_threshold])
            metas.append([enviroment_id])

        attributes = np.array(attributes)
        metas = np.array(metas)

        enviroments_table = Table(domain, attributes, None, metas)

        self.Outputs.enviroments_table.send(enviroments_table)
