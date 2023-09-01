import yaml


class Yaml():
    def __init__(self, path):
        self.path = path
        


    def parse_case_yaml(self):
        with open(self.path, 'r') as file:
            data = yaml.safe_load(file)
        
        conf = {}

        conf["case-tool"] = data['case-tool']
        conf["circle-times"] = data['circle-times']
        conf["case-interval"] = data['case-interval']
        conf["tool-interval"] = data['tool-interval']
        conf["case-path"] = data['path']
        conf["ip"] = data['ip']
        conf["port"] = data['port']
        conf["user"] = data['user']
        conf["pwd"] = data['pwd']

        return conf

