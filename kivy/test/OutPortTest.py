# The OutPort test class

import unittest
from model.OutPort import OutPort


class OutPortTestCase(unittest.TestCase):
    """ Test case for output port """

    def setUp(self):
        self.port = OutPort([ [1,5] ])
        self.basicPort = OutPort.basic()

    def tearDown(self):
        self.port = None
        self.basicPort = None

    def testInsertTimeRangeValue(self):
        self.port.insertTimeRangeValue(0,1)
        expected = [ [0, 1] , [1,5]]
        self.assertEqual(self.port.timeSeriesData, expected)

    def testInsertInBasicPort(self):
        self.basicPort.insertTimeRangeValue(0,1)
        expected = [ [0, 1] , [5, 1], [10, 2]]
        self.assertEqual(self.basicPort.timeSeriesData, expected)



if __name__ == '__main__':
    unittest.main()
