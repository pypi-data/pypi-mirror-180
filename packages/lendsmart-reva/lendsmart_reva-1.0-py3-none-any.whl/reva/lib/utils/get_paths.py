"""
    This module will provide the paths
"""
import os
from reva.exception import EnvPathNotConfigured


class PathGetter:
    """
    This class will hold the functions to get paths
    """

    def __init__(self):
        self.root_path = self.get_root_path()

    def get_root_path(self):
        """
        This function returns the root path
        """
        try:
            home_path = os.environ["LENDSMART_REVA_HOME"]
            print("=====HOME PATH ==>", home_path)
        except KeyError as err:
            home_path = ""
            print("error on accessing home path", err)
        if not home_path:
            raise EnvPathNotConfigured(
                "Root home path is not configured in LENDSMART_REVA_HOME"
            )
        return home_path

    def get_reva_ui_home_path(self):
        """
        Returns the ui home path
        """
        try:
            ui_home_path = os.environ["LENDSMART_REVA_UI_HOME"]
        except KeyError as err:
            print("error on accessing ui home path", err)
            ui_home_path = ""
        print("====UI HOME PATH===>", ui_home_path)
        if not ui_home_path:
            raise EnvPathNotConfigured(
                "UI home path is not configured in LENDSMART_REVA_UI_HOME"
            )
        return ui_home_path

    def get_reva_worklet_home_path(self):
        """
        Returns the worklet home path
        """
        try:
            worklet_home_path = os.environ["LENDSMART_REVA_WORKLET_HOME"]
        except KeyError as err:
            print("error on accessing worklet home path", err)
            worklet_home_path = ""
        print("====UI HOME PATH===>", worklet_home_path)
        if not worklet_home_path:
            raise EnvPathNotConfigured(
                "Worklet home path is not configured in LENDSMART_REVA_WORKLET_HOME"
            )
        return worklet_home_path

    def get_config_path(self):
        """
        Returns the config path
        """
        return self.get_root_path() + "/config.json"

    def get_ui_customization_path(self):
        """
        This function will return the ui customization path
        """
        return self.get_reva_ui_home_path() + "/packages/lendsmart_ui/customization/"

    def get_ui_config_path(self, namespace: str):
        """
        This function will return the ui config path
        """
        return (
            self.get_ui_customization_path()
            + namespace
            + "/config"
        )

    def get_workflow_files(self, folder_path):
        """
        THis function will return the workflow json files path
        """
        workflow_file_path = []
        all_files = os.listdir(folder_path)
        wanted_files = ["WI_"]
        filtered_workflow = [wf for wf in all_files if wf[0:3] in wanted_files]
        for wff in filtered_workflow:
            workflow_file_path.append(folder_path + "/" + wff)
        return workflow_file_path

    def get_site_settings_files(self, folder_path):
        """
            This function will return the site setting json path
        """
        sitesettings_file_path = []
        all_files = os.listdir(folder_path)
        wanted_files = ["siteSettings"]
        filtered_workflow = [wf for wf in all_files if wf[0:12] in wanted_files]
        for wff in filtered_workflow:
            sitesettings_file_path.append(folder_path + "/" + wff)
        return sitesettings_file_path

    def get_workflow_json_paths(self, namespaces: list):
        """
        THis function will return the json files
        to update
        """
        files_to_update = []
        for namespace in namespaces:
            files_to_update.extend(
                self.get_workflow_files(
                    self.get_ui_config_path(namespace)
                )
            )
        return files_to_update

    def get_site_settings_json_path(self, namespaces : list):
        """
            Returns the file paths of site settings
        """
        files_to_update = []
        for namespace in namespaces:
            files_to_update.extend(
                self.get_site_settings_files(
                    self.get_ui_config_path(namespace)
                )
            )
        return files_to_update
