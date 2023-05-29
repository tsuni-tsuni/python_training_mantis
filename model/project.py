class Project:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name == other.name
