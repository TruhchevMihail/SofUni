class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.times_yielded = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times_yielded >= self.count:
            raise StopIteration
        value = self.current
        self.current += self.step
        self.times_yielded += 1
        return value
