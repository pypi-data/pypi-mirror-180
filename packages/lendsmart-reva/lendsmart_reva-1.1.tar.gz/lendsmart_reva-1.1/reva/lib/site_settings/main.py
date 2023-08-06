"""
    handles the site settings
"""
from reva.lib.site_settings.update import SiteSettingsUpdate


class SiteSettings:
    """
        handles the site settings
    """
    def __init__(self, arguments):
        self.argument = arguments

    def run(self):
        """
            THis function will separate the actions
        """
        if self.argument.action == "update":
            SiteSettingsUpdate(self.argument).start()

    def __str__(self) -> str:
        pass
