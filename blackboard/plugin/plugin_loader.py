import os
import importlib.util as imp
from .plugin_base import plugin_base


class _plugin_loader:
    def __init__(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.__core_path = "{here}/core_plugins".format(here=here)
        try:
            self.__user_path = os.environ["BLACKBOARD_PLUGIN_DIR"]
        except KeyError:
            self.__user_path = None

        self.__plugins = {}
        self.__load_plugins(self.__core_path)
        self.__load_plugins(self.__user_path)
        self.__kwords = list(self.__plugins.keys())

    def get_plugin(self, identifier):
        return self.__plugins.get(identifier, None)

    def get_keywords(self):
        return self.__kwords

    def __load_plugins(self, path):
        if not path:
            return

        for f in os.listdir(path):
            if os.path.splitext(f)[-1] != ".py" or f == "__init__.py":
                continue
            plg = self.__load_plugin_from_file(os.path.join(path, f))
            if not plg:
                continue

            if not plg.name:
                print ("Error, no name set, cannot be loaded")
                continue

            self.__plugins[plg.name] = plg

            if not plg.keywords:
                print ("Error, no keywords found, cannot be loaded")
                del self.__plugins[plg.name]
                continue

            for kw in plg.keywords:
                self.__plugins[kw] = plg

    def __load_plugin_from_file(self, path):
        spec = imp.spec_from_file_location("loaded_module", path)
        module = imp.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not issubclass(module.plugin.instance, plugin_base):
            return None

        return module.plugin
