from interface import utworz_czytaj, powitanie
from notatnik import Notatnik


print()
powitanie()
print()

while __name__ == '__main__':
    notatnik_podstawowy = Notatnik()
    utworz_czytaj(notatnik_podstawowy)
    print()