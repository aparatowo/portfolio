#Rafał Nitychoruk


class MyTime:
    def __init__(self, _minutes, _seconds):
        self._minutes = _minutes
        self._seconds = _seconds

        if self._minutes >= 0:
            pass
        else:
            raise ValueError

        if self._seconds in range(60):
            pass
        else:
            raise ValueError

    def __repr__(self):
        return f'MyTime(min={self._minutes}, sec={self._seconds})'

    def __lt__(self, other):
        if self._minutes < other._minutes:
            return True
        elif self._minutes == other._minutes:
            if self._seconds < other._seconds:
                return True
        return False

    def __eq__(self, other):
        if self._minutes == other._minutes and self._seconds == other._seconds:
            return True
        return False

    def __add__(self, other):
        add_a_minute = self._minutes + other._minutes
        add_a_second = self._seconds + other._seconds
        if add_a_second > 59:
            add_a_minute += 1
            add_a_second -= 60
        return MyTime(add_a_minute, add_a_second)

    def __sub__(self, other):
        sub_a_minute = self._minutes - other._minutes
        sub_a_second = self._seconds - other._seconds
        if sub_a_second < 0:
            sub_a_minute -= 1
            sub_a_second = 60 - other._seconds
            sub_a_second += self._seconds
        if sub_a_minute < 0:
            raise ValueError
        return MyTime(sub_a_minute, sub_a_second)


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    m = MyTime(10, 1)
    n = MyTime(0, 59)
    p = m - n
    print(p)
    pass
