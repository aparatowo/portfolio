from functools import reduce
def add_advanced_border(string, char, spacing_h=0, spacing_v=0):
    lines = string.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + spacing_h * 2

    floor = f'{char * width}'
    v_fill = f'{" " * width}'

    new_string = [floor] + \
                 [v_fill] * spacing_v + \
                 [f'{line.center(width)}' for line in lines] + \
                 [v_fill] * spacing_v + \
                 [floor]

    new_string = [f'{char}{line}{char}' for line in new_string]
    new_string = '\n'.join(new_string)
    return new_string


if __name__ == '__main__':
    print("Przykładowe użycie: 'add_advanced_border('tekst', '.', spacing_h=10, spacing_v=3)'")
    print(add_advanced_border('tekst', '.', spacing_h=10, spacing_v=3))

