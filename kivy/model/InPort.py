# The InPort class

from model.OutPort import OutPort

class InPort(object):
    """ Represents a single input port for a Node. Internally maintains a reference
        to the port which feeds this port. Does not create a new port of its own.
    """

    def __init__(self, feederPort: OutPort):
        """ Initialize an InputPort """
        self.feederPort = feederPort
        self.timeSeriesData = feederPort.timeSeriesData

    @classmethod
    def basic(cls):
        """ Create basic InputPort """
        return cls(OutPort.zeros())

    def setFeederPort(self, feederPort: OutPort):
        """ Sets a new feederPort """
        self.feederPort = feederPort
        self.timeSeriesData = feederPort.timeSeriesData



