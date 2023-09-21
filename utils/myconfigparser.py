import configparser
from pathlib import Path

cfgfile = 'petsqa.ini'
cfgfiledir = 'config'

config = configparser.ConfigParser()
Base_Dir = Path(__file__).resolve().parent.parent
print(Base_Dir)
Config_File = Base_Dir.joinpath(cfgfiledir).joinpath(cfgfile)

config.read(Config_File)


def getPetAPIURL():
    return config['pet']['url']


def getStoreAPIURL():
    return config['store']['url']


print(getPetAPIURL())
