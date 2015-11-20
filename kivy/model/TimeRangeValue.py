# The TimeRangeValue class

class TimeRangeValue(object):
    """Contains a value in a time range. 1 TimeRangeValue stores only 1 value which holds 
       throughout the time represented by this object. If the value changes, a new 
       TimeRangeValue object is needed to store it for the next time range. 
       
       Note: The unit of time is seconds expressed as an integer. All user supplied time 
       units need to be converted to min & max in secs for this object. Millisec/nanosec 
       resolution will simply require support for larger numbers."""

    def __init__(self, till: int, value: float):
        """Initialize a TimeRangeValue"""
        self.till = till
        self.increment = increment
        self.valueInRange = value

    @classmethod
    def basic(cls):
        """Create a basic TimeRangeValue quickly"""
        return cls(0, 10, 1, 1)


 

