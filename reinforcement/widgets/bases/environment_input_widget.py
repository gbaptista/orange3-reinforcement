from Orange.widgets.widget import Input

from .reinforcement_widget import ReinforcementWidget


class EnvironmentInputWidget(ReinforcementWidget):
    class Inputs:
        environment_id = Input("Environment", str)

    @Inputs.environment_id
    def set_environment_id(self, environment_id):
        pass
