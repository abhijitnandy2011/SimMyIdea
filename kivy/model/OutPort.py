# The OutPort class


class OutPort(object):
    """ Represents a single output port for a Node"""

    def __init__(self, timeSeriesData: list):
        """ Initialize a Port """
        self.timeSeriesData = timeSeriesData

    @classmethod
    def basic(cls):
        """ Create a Port quickly """
        return cls([ [5, 1], [10, 2] ])  # using [ (x, y) ] makes x & y a tuple and thus immutable

    @classmethod
    def zeros(cls):
        """ Create a OutPort quickly with zeros. This is mostly for tests, to 
            create a basic InPort. """
        return cls([ [0, 0] ])


    def insertTimeRangeValue(self, till: int, value: float):
        """ Inserts time range value and sorts the time series list on time """
        self.timeSeriesData.append([till, value])
        self.timeSeriesData.sort(key=lambda timeValuePair: timeValuePair[0])
