class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.values = [0] * size
        self.pos = 0
        self.acu = 0
        self.n = 0

    def next(self, val: int) -> float:
        if self.n < self.size:
            self.acu += val
            self.values[self.pos] = val
            self.n += 1
        else:
            self.acu -= self.values[self.pos]
            self.acu += val
            self.values[self.pos] = val
        self.pos = self.pos + 1 if self.pos + 1 < self.size else 0

        return self.acu / self.n

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


obj = MovingAverage(5)
test = [12009, 1965, -940, -8516, -16446, 7870 , 25545 , -21028 , 18430, -23464]

for i in test:
    print(obj.next(i))
