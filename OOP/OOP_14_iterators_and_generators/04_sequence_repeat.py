class sequence_repeat:
    def __init__(self, sequence, length):
        self.sequence = sequence
        self.length = length
        self.index = 0
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated >= self.length:
            raise StopIteration
        value = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.generated += 1
        return value
