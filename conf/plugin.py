from pathlib import Path
import yaml 
from config import PLUGIN_BASE_DIR
import glob
import re

class PluginLoader:

    def __init__(self):
        self.plugin_folder = Path(__file__).parent.parent / PLUGIN_BASE_DIR
        self.plugins = [self._process(plugin_file) for plugin_file in glob.glob(f"{self.plugin_folder}/*.yml")]
    
    def _process(self, plugin_file):
        with open(plugin_file, "r") as f:
            try:
                #yaml.SafeLoader.add_constructor(u'tag:yaml.org,2002:python/regexp', lambda l, n: re.compile(l.construct_scalar(n)))
                
                p = yaml.safe_load(f)
            except Exception as e:
                raise(e)
            
            return Plugin(plugin_file, p)

    def __str__(self):
        return ",".join([str(plugin.fname) for plugin in self.plugins])


class Plugin:

    def __init__(self, fname, yaml_data):
        self.fname = Path(fname)
        try:
            self.id = yaml_data["id"]
            self.info = yaml_data["info"]
            self.parameters = yaml_data["parameters"]
            self.languages = self.parameters["languages"]
            self.file_types = self.parameters["file_types"]
            self.regex = re.compile(bytes(f"\n(.*)\n(.*)\n(.*)({self.parameters['matchers']['regex']})", encoding="utf-8"), re.IGNORECASE | re.MULTILINE) if self.parameters["matchers"]["regular_expression"] else None
        
        except TypeError:
            raise Exception("unable to parse YAML plugin")


    def __str__(self):
        return f"{self.id} - {self.info['description']}"

