class EveryOtherNumber:
    def __init__(self):
        self.number = 0

    def __next__(self):
        self.number += 2

        if self.number > 100:
            raise StopIteration
        return self.number

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = EveryOtherNumber()
    print(list(numbers))
