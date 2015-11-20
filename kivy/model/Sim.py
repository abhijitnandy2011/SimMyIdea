# Defining the model's layout
# This module is the Sim's namespace

import json
from enum import Enum
import model.Serializer as Serializer

def generateUnits():
    global units
    units = dict(zip(unitsList[:], range(1, len(unitsList)+1)))

def addUnit(unitName: str):
    global units
    units[unitName] = len(units) + 1


def loadModel(fileName: str):
    """ Read the model from disk """
    global model
    model = Serializer.fromJSON(fileName)



def writeModel(fileName: str):
    global model
    # Start creating the JSON directly from runtime model
    strJSON = Serializer.toJSON(model)

    

class SimObjectTypes(Enum):
    NODE= 1
    PORTBANK = 2
    PORT = 3

# The initial list of units
unitsList = [
    'MILILITRE'
    'LITRE',
    'GALLON'
    'KG',
    'GRAM',
    'TON',
    'SECONDS',
    'MINUTES',
    'HOURS',
    'DAYS',
    'MONTHS',
    'YEARS',
    'DECADES',
    'CENTURIES',
    'METERS',
    'KM',
    'MILES'
    'WATT',
    'MEGAWATT',
    'GIGAWATT',
    'TERAWATT'
]

# Runtime model
model = {
    'Sim': 
    {
        'WaterPump':
        {
            'type': SimObjectTypes.NODE,
            'InBank':
            {
                'ref': 'None'
            },
            'OutBank':
            {
                'WaterOut':
                {
                    'type': SimObjectTypes.PORT,
                    'curves' : 
                    {
                        'real':
                        [
                              { 'type': 'lin', 'start':0, 'end':10, 'left':0, 'right':100 },
                              { 'type': 'const', 'start':10, 'end':22, 'value':100}
                        ],
                        'speculation':
                        [
                             { 'type': 'const', 'start':10, 'end':22, 'value':100}
                        ],
                    },
                    'unit':   # There may be more units like for speed m/s, [0] = meters, [1] = seconds
                    [
                        'litre'
                    ]
                }
            },
            'properties':
            {

            },
            'script':
            {

            },
        },
        'Factory':
        {
            'InBank':
            {
                'WaterIn':
                {
                    'ref': 'WaterPump.WaterOut'
                }
            },
        }
    }
}

# Setup references
#model['Sim']['Factory']['InBank']['WaterIn'] = model['Sim']['WaterPump']['OutBank']['WaterOut']
