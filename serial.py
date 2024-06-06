"""Python serial number generator."""


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
        self.start = start
        self.current_num = start

    def generate(self):
        serial_number = self.current_num
        self.current_num += 1  # Prepares for the next call
        return serial_number

    def reset(self):
        self.current_num = self.start


serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())

""" NOTE

Create a sequence of incrementing serial numbers.
Each time a new serial number is generated, it increments by one from the last number. 

Initial Serial Number - a starting serial number needs to specified.

Generating Serial Number - a `generate` method should return the next serial number in the sequence

Resetting Serial Number - a `reset` method should set the serial number back to the original starting number. 

 """
