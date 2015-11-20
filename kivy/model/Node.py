# The InPort class

from model.OutPort import OutPort
from model.InPort import InPort

class Node(object):
    """ The Node class. This contains 2 banks of ports and the lua code to execute for this node.
        It also contains any local properties of the Node.
    """

    def __init__(self, nodeName: str):
        """ Initialize a Port """
        self.nodeName = nodeName
        self.inBank = { 'input1': InPort.basic()}
        self.outBank = { 'output1': OutPort.basic()}
        self.scriptCode = ""


    def addInPort(self, inPort: InPort, portName: str):
        """ Add new inPort to inBank """

    def addInPortReference(self, inPortName: str, feederPort: OutPort):
        """ Add a reference feeder port for an existing inPort """


            def addOutPort(self, inPortName: str, feederPort: OutPort):
        """ Add a reference feeder port for an existing inPort """


    def insertTimeRangeValue(self, till: int, value: float):
        """ Inserts time range value and sorts the time series list on time """
        self.timeSeriesData.append([till, value])
        self.timeSeriesData.sort(key=lambda timeValuePair: timeValuePair[0])
