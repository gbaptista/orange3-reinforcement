import numpy as np

import gym

from Orange.data import Table, Domain, StringVariable, ContinuousVariable

from Orange.widgets.utils.signals import Output

from .bases.reinforcement_widget import ReinforcementWidget


class OWEnvironments(ReinforcementWidget):
    id = "orange.widgets.reinforcement.environments"
    name = "Environments"
    description = "List of all available OpenAI Gym Environments."
    icon = "icons/environments_icon.svg"
    priority = 40
    keywords = ["OpenAI Gym", "Environment"]

    class Outputs:
        environments_table = Output("Environments", Table)

    def __init__(self):
        super().__init__()

        self.environments_table_output()

    def environments_table_output(self):
        domain = Domain(
            [
                ContinuousVariable("TimeStep Limit"),
                ContinuousVariable("Trials"),
                ContinuousVariable("Reward Threshold")
            ],
            None,
            [StringVariable("Environment Id")]
        )

        attributes = []
        metas = []
        for environment in gym.envs.registry.all():
            environment_id = environment.id

            timestep_limit = environment.timestep_limit
            trials = environment.trials
            reward_threshold = environment.reward_threshold

            attributes.append([timestep_limit, trials, reward_threshold])
            metas.append([environment_id])

        attributes = np.array(attributes)
        metas = np.array(metas)

        environments_table = Table(domain, attributes, None, metas)

        self.Outputs.environments_table.send(environments_table)
