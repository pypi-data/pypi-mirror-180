"""
    handles the workflow
"""
from reva.lib.workflow.update import WorkflowUpdate


class Workflow:
    """
        handles the workflow
    """
    def __init__(self, arguments):
        self.argument = arguments

    def run(self):
        """
            THis function will separate the actions
        """
        if self.argument.action == "update":
            WorkflowUpdate(self.argument).start()

    def __str__(self) -> str:
        pass
