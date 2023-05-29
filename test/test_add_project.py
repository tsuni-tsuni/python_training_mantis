from model.project import Project
import random
import string


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project_exists = True
    while project_exists:
        project_exists = False
        project = Project(name=random_string("project", 15))
        for p in old_projects:
            if p.name == project.name:
                project_exists = True
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda x: x.name) == sorted(new_projects, key=lambda x: x.name)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
