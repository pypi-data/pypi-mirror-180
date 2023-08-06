"""
    handles the namespaces
"""
from reva.lib.utils import get_namespaces
from reva.lib.utils.get_paths import PathGetter

def main(argument):
    """
        calls the action
    """
    if argument.action == "list":
        ui_path = PathGetter().get_ui_customization_path()
        namespace_list = get_namespaces.get_namespace_by_argument_and_path(argument, ui_path)
        print("Namespaces=>", namespace_list)
        return None
    print("Unknown action !!!")
    print("Supported action => list")
    print("Try => reva namespace list all dev")
    return None


def namespaces(parser):
    """
        handles the namespace
    """
    parser.add_argument('action', metavar ='U', type = str,
                        help ='action for namespace')
    parser.add_argument('namespace', metavar ='N', type = str,
                        help ='list namespaces')
    parser.add_argument('env', metavar ='E', type = str,
                        help ='Environment , possible values 1.dev 2. prod 3.qa 4.tao 5.apiprod')
    parser.set_defaults(
        func=main,
        )
