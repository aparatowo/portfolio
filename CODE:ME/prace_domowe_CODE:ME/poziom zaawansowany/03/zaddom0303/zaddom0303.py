# Rafał Nitychoruk

def counter_generator(start=0, digits=2):
    max_num = 10 ** digits
    start_number = start
    while start_number != max_num+1:
        for number in range(start_number, max_num):
            yield str(number).zfill(digits)
            start_number += 1
            if start_number == max_num:
                start_number = start


if __name__ == '__main__':
    numbersy = counter_generator()
    for number in numbersy:
        print(number)
    pass
