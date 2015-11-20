# Defining the model's layout
# This module is the Sim's namespace

import json
from pprint import pprint

def toJSON(model):
    """ Convert model to JSON string & return it """



def fromJSON(fileName: str):
    """ Read model from JSON file & expand it into the runtime model """
    with open ('model.json', 'r') as data_file:
        #data = data_file.read()
        #print(data)
        fileModel = json.load(data_file)
        pprint(fileModel)
        return fileModel

    # Expand the loaded file model into runtime model

