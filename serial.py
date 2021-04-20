class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """set starting serial number"""
        self.start = start-1
        self.counter = 0

    def __repr__(self):
        return f"<SerialGenerator, starting serial number = {self.start}>"

    def generate(self):
        """increment starting serial number by 1 on each call"""
        self.counter += 1
        return self.start + self.counter

    def reset(self):
        """reset the serial number to the starting value"""
        self.counter = 0
        
