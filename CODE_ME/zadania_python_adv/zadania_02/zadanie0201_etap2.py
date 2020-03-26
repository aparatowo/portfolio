class RangeNumbers:
    def __init__(self, end, start=0, step=1):
        self.number = start
        self.end = end

        if step <= 0:
            raise ValueError('Parametr "step" musi być dodatni')
        self.step = step

    def __next__(self):
        if self.number >= self.end:
            raise StopIteration

        returned_number = self.number
        self.number += self.step
        return returned_number

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = RangeNumbers(10)
    print(list(numbers))

    numbers = RangeNumbers(20, 10)
    print(list(numbers))

    numbers = RangeNumbers(30, 10, 3)
    print(list(numbers))
