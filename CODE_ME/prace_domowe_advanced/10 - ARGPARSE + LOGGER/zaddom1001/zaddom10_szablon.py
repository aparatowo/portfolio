# tutaj wpisz swoje imie i nazwisko
import logging
import argparse
from zaddom10_functions import set_logger, wc
from zaddom10_logger import initialize_wc_logger

logger = logging.getLogger('wc_logger')

parser = argparse.ArgumentParser(description='Program pozwala na ustawienie poziomu logowania.')
parser.add_argument('-v', '--log_level', choices=['CRITICAL', 'FATAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'], default='WARNING', help='Poziom logowania, domyślnie jako WARNING')
parser.add_argument('-l', help='Powoduje, że wypisana jest tylko liczba linii')
parser.add_argument('-w', help='Powoduje, że wypisana jest tylko liczba słów')
parser.add_argument('-c', help='Powoduje, że wypisana jest tylko liczba bajtów')
parser.add_argument('filename', help='Obowiązkowa nazwa pliku do analizy.')

args = parser.parse_args()

def main():
    initialize_wc_logger()

    set_logger(args.log_level)

    result = wc(args.filename, template)

    print(result)


if __name__ == '__main__':
    main()
