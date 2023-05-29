from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if "/manage" not in wd.current_url:
            wd.find_element(By.LINK_TEXT, "Manage").click()

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            self.open_manage_page()
            wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        # init project creation
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        wd.find_element(By.LINK_TEXT, "Proceed").click()

    def select_project(self, project):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "%s" % project).click()

    def count(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        return len(wd.find_elements(By.XPATH, "//a[contains(@href,'manage_proj_edit_page.php?project_id=')]"))

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_project(project)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        project_list = []
        for element in wd.find_elements(By.XPATH, "//a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            project_list.append(Project(name=text.strip()))
        return project_list
