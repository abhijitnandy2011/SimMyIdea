# The InPort test class
import unittest
from model.OutPort import OutPort
from model.InPort import InPort


class InPortTestCase(unittest.TestCase):
    """ Test case for input port """

    def setUp(self):
        self.outPort = OutPort.basic()
        self.basicInPort = InPort.basic()
        self.inPort = InPort(self.outPort)

    def tearDown(self):
        self.outPort = None
        self.basicInPort = None
        self.inPort = None

    def testOutportReference(self):        
        self.assertEqual(self.inPort.feederPort, self.outPort)
        self.assertEqual(self.inPort.timeSeriesData, self.outPort.timeSeriesData)
        

    def testInsertInBasicPort(self):
        self.basicInPort.setFeederPort(self.outPort)
        self.assertEqual(self.basicInPort.feederPort, self.outPort)
        self.assertEqual(self.basicInPort.timeSeriesData, self.outPort.timeSeriesData)



if __name__ == '__main__':
    unittest.main()
