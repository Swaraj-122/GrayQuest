class Rectangle:
    def __init__(self, length, breadth):
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and breadth must be positive integers.")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def is_square(self):
        return self.length == self.breadth

