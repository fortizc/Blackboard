class plugin_base:
    def __init__(self,
                 name,
                 keywords,
                 author,
                 description,
                 long_desc, help, instance):
        self.name = name
        self.keywords = keywords
        self.author = author
        self.description = description
        self.long_desc = long_desc
        self.help = help
        self.instance = instance
