class EveryOtherNumber:
    def __init__(self, end, start=0):
        self.number = start
        self.end = end

    def __next__(self):
        if self.number >= self.end:
            raise StopIteration

        returned_number = self.number
        self.number += 2
        return returned_number

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = EveryOtherNumber(100)
    print(list(numbers))

    numbers = EveryOtherNumber(20, 10)
    print(list(numbers))
