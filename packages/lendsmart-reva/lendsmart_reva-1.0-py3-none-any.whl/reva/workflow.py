"""
    handles the workflow
"""
from reva.lib.workflow.main import Workflow

def main(argument):
    """
        calls the action
    """
    return Workflow(argument).run()


def workflow(parser):
    """
        handles the workflpw
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
