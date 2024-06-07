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

    >>> serial
    <SerialGenerator start=100 next=101>
    """

    def __init__(self, start):
        self.start = start
        self.next_number = start

    def __repr__(self):
        return f"<SerialGenerator> start={self.start} next={self.next_number}"

    def generate(self):
        self.next_number += 1  # Prepares for the next call
        serial_number = self.next_number - 1
        return serial_number

    def reset(self):
        self.next_number = self.start
        return self.next_number


serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial)
# print(serial.generate())

""" NOTE

Create a sequence of incrementing serial numbers.
Each time a new serial number is generated, it increments by one from the last number. 

Initial Serial Number - a starting serial number needs to specified.

Generating Serial Number - a `generate` method should return the next serial number in the sequence

Resetting Serial Number - a `reset` method should set the serial number back to the original starting number. 

 """
