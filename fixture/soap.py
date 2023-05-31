from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        url = self.app.base_url + "/api/soap/mantisconnect.php?wsdl"
        client = Client(url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        url = self.app.base_url + "/api/soap/mantisconnect.php?wsdl"
        client = Client(url)
        list = client.service.mc_projects_get_user_accessible(self.app.current_username, self.app.current_password)
        project_list = []
        for element in list:
            text = element.name
            project_list.append(Project(name=text))
        return project_list
