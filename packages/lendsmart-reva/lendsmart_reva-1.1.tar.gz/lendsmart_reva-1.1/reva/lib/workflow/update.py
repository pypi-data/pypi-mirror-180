"""
    update the workflow
"""
from ramda import path_or
from reva.lib.utils.get_namespaces import get_namespace_by_argument_and_path
from reva.lib.graphql_queries.workflow import update_workflow_intent_query
from reva.lib.base.base import RevaBase


class WorkflowUpdate(RevaBase):
    """
    update the workflow
    """

    def __init__(self, arguments):
        super().__init__(arguments)
        self.argument = arguments

    def get_workflow_json_paths_to_update(self):
        """
        THis function will return the json files
        to update
        """
        namespaces_to_update = get_namespace_by_argument_and_path(
            self.argument, self.get_ui_customization_path()
        )
        return self.get_workflow_json_paths(namespaces_to_update)

    def start(self):
        """
        update the workflow
        """
        workflow_json_data = self.get_file_by_paths(
            self.get_workflow_json_paths_to_update()
        )
        query_datas = []
        for json_data in workflow_json_data:
            query_datas.append(update_workflow_intent_query(path_or({},["data",0], json_data)))
        return self.excecute_for_list_of_query_data(query_datas)
