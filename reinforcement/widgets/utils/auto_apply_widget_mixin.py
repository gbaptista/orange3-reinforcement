from Orange.widgets import gui

from Orange.widgets.widget import OWWidget, Msg
from Orange.widgets.settings import Setting


class AutoApplyWidgetMixin:
    setting_auto_apply = Setting(True)

    def render_auto_apply_layout(self):
        self.apply_button = gui.auto_commit(
            self.controlArea, self, 'setting_auto_apply', '&Apply',
            box=True, commit=self.apply, callback=self.auto_apply_changed)

    def auto_apply_changed(self):
        if self.setting_auto_apply and self.outdated_settings:
            self.apply()

    def settings_changed(self, *_args, **_kwargs):
        self.outdated_settings = True
        self.Warning.outdated_settings(shown=not self.setting_auto_apply)

        if self.setting_auto_apply:
            self.apply()

    def clear_outdated_warning(self):
        self.outdated_settings = False
        self.Warning.outdated_settings.clear()

    class Warning(OWWidget.Warning):
        outdated_settings = Msg("Press Apply to submit changes.")
