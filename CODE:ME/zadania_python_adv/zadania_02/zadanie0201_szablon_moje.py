class EveryOtherNumber:
    def __init__(self, max_number, start_number=0, step=1):
        self.number = start_number
        self.max = max_number
        self.step = step

    def __next__(self):

        if self.step <= 0:
            raise ValueError('Wartość musi być większa od 0!')
        else:
            pass

        number_to_print = self.number
        self.number += self.step

        if number_to_print >= self.max:
            raise StopIteration
        return number_to_print

    def __iter__(self):
        return self


if __name__ == '__main__':
    numbers = EveryOtherNumber(100, 21, 0)
    print(list(numbers))

    pass  # tutaj możesz testować działanie funkcji
