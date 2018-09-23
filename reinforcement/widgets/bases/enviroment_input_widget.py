from Orange.widgets.widget import Input

from .reinforcement_widget import ReinforcementWidget


class EnviromentInputWidget(ReinforcementWidget):
    class Inputs:
        enviroment_id = Input("Enviroment", str)

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        pass
