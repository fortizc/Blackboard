class blackboard_plugin:
    def __init__(self, name, author, sdesc, ldesc, keywords=[]):
        self.name = name
        self.author = author
        self.short_desc = sdesc
        self.long_desc = ldesc
        self.keywords = keywords

    def help(self):
        msg = "Error, help() method must be implemented in child class"
        raise NotImplemented(msg)

    def process(self, line):
        msg = "Error, process() method must be implemented in child class"
        raise NotImplemented(msg)
