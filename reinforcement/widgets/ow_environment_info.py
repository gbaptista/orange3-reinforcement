import gym

from Orange.widgets import gui

from .bases.environment_input_widget import EnvironmentInputWidget


class OWEnvironmentInfo(EnvironmentInputWidget):
    id = "orange.widgets.reinforcement.environment_info"
    name = "Environment Info"
    description = """Display basic information about the environment, such
    as the number and type of observation space and action space."""
    icon = "icons/environment_info_icon.svg"
    priority = 60
    keywords = ["OpenAI Gym", "Environment", "Info", "Details"]

    environment_id = None

    observation_space = None
    action_space = None
    reward_range = None

    timestep_limit = None
    trials = None
    reward_threshold = None

    def __init__(self):
        super().__init__()

        self.set_initial_values()

        for box in ("Environment Id",
                    "Observation Space", "Action Space",
                    "Reward Range", "TimeStep Limit",
                    "Trials", "Reward Threshold"):
            name = box.lower().replace(" ", "_")
            v_box = gui.vBox(
                self.controlArea, box,
                addSpace=False and box != "Meta Attributes"
            )
            gui.label(v_box, self, "%%(%s)s" % name)

    def set_initial_values(self):
        self.environment_id = '?'

        self.observation_space = '?'
        self.action_space = '?'
        self.reward_range = '?'

        self.timestep_limit = '?'
        self.trials = '?'
        self.reward_threshold = '?'

    def set_environment_id(self, environment_id):
        if environment_id is not None:
            registry = self.gym_registry_by_id(environment_id)
            environment = registry.make()

            self.build_environment_info(registry, environment)

    @staticmethod
    def gym_registry_by_id(environment_id):
        gym_registry = None

        for registry in gym.envs.registry.all():
            if registry.id == environment_id:
                gym_registry = registry
                break

        return gym_registry

    def build_environment_info(self, registry, environment):
        self.environment_id = registry.id

        self.observation_space = environment.observation_space
        self.action_space = environment.action_space
        self.reward_range = environment.reward_range

        self.timestep_limit = registry.timestep_limit
        self.trials = registry.trials
        self.reward_threshold = registry.reward_threshold
