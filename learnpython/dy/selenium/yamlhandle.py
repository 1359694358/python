import yaml
def readYml(path):
    with open(path,"r") as ymlFile:
        config=yaml.load(ymlFile, yaml.FullLoader)
        return config