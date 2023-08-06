"""
    update the workflow
"""
from reva.lib.utils.get_namespaces import get_namespace_by_argument_and_path
from reva.lib.base.base import RevaBase
from reva.lib.graphql_queries.site_settings import update_site_settings_query

class SiteSettingsUpdate(RevaBase):
    """
    update the site settings
    """

    def __init__(self, arguments):
        super().__init__(arguments)
        self.argument = arguments

    def get_site_settings_json_paths_to_update(self):
        """
        THis function will return the json files
        to update
        """
        namespaces_to_update = get_namespace_by_argument_and_path(
            self.argument, self.get_ui_customization_path()
        )
        return self.get_site_settings_json_path(namespaces_to_update)

    def start(self):
        """
        update the workflow
        """
        site_settings_json_data = self.get_file_by_paths(
            self.get_site_settings_json_paths_to_update()
        )
        query_datas = []
        for json_data in site_settings_json_data:
            query_datas.append(update_site_settings_query(json_data))
        return self.excecute_for_list_of_query_data(query_datas)
