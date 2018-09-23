import gym

from Orange.widgets import gui

from Orange.widgets.widget import Input

from .bases.reinforcement_widget import ReinforcementWidget


class OWInfo(ReinforcementWidget):
    id = "orange.widgets.reinforcement.info"
    name = "Enviroment Info"
    description = """Display basic information about the enviroment, such
    as the number and type of observation space and action space."""
    icon = "icons/info.png"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Info", "Details"]

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    def __init__(self):
        super().__init__()

        self.set_enviroment_id(None)

        for box in ("Enviroment Id",
                    "Observation Space", "Action Space",
                    "Reward Range", "TimeStep Limit",
                    "Trials", "Reward Threshold"):
            name = box.lower().replace(" ", "_")
            v_box = gui.vBox(
                self.controlArea, box,
                addSpace=False and box != "Meta Attributes"
            )
            gui.label(v_box, self, "%%(%s)s" % name)

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        self.enviroment_id = '?'

        self.observation_space = '?'
        self.action_space = '?'
        self.reward_range = '?'

        self.timestep_limit = '?'
        self.trials = '?'
        self.reward_threshold = '?'

        if enviroment_id is not None:
            for enviroment in gym.envs.registry.all():
                if enviroment.id == enviroment_id:
                    maked_enviroment = enviroment.make()

                    self.enviroment_id = enviroment.id

                    self.observation_space = maked_enviroment.observation_space
                    self.action_space = maked_enviroment.action_space
                    self.reward_range = maked_enviroment.reward_range

                    self.timestep_limit = enviroment.timestep_limit
                    self.trials = enviroment.trials
                    self.reward_threshold = enviroment.reward_threshold

                    break
