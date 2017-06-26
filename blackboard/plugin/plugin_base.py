MAX_PRIORITY = 0
MOD_PRIORITY = 1
POW_PRIORITY = 2
DIV_PRIORITY = 3
ADD_PRIORITY = 4
SHF_PRIORITY = 5
BIT_AND_PRIORITY = 6
BIT_XOR_PRIORITY = 7
BIT_OR_PRIORITY = 8
LOWEST_PRIORITY = 9


class plugin_base:
    def __init__(self,
                 name,
                 keywords,
                 priority,
                 author,
                 description,
                 long_desc,
                 help,
                 instance):
        self.name = name
        self.keywords = keywords
        self.priority = priority
        self.author = author
        self.description = description
        self.long_desc = long_desc
        self.help = help
        self.instance = instance
