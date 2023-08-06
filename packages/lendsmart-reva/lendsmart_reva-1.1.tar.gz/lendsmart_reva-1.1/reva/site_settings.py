"""
    handles the site settings
"""
from reva.lib.site_settings.main import SiteSettings

def main(argument):
    """
        calls the action
    """
    return SiteSettings(argument).run()


def site_settings(parser):
    """
        handles the site settings
    """
    parser.add_argument('action', metavar ='U', type = str,
                        help ='update the workflow')
    parser.add_argument('namespace', metavar ='N', type = str,
                        help ='List of namespaces')
    parser.add_argument('env', metavar ='E', type = str,
                        help ='Environment , possible values 1.dev 2. prod')
    parser.set_defaults(
        func=main,
        )
