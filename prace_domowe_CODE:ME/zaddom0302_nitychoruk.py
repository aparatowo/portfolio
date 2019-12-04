# Rafał Nitychoruk

zespoly = ["Led Zeppelin", "The Beatles", "Pink Floyd", "Queen",
           "Metallica", "AC/DC", "The Rolling Stones", "Nirvana",
           "Guns'n Roses", "The Who", "Black Sabbath", "Rush",
           "Green Day", "Iron Maiden", "Red Hot Chilli Peppers",
           "Aerosmith", "Linkin Park", "The Jimi Hendrix Experience",
           "Radiohead", "The Doors"]

zespoly_z_the = []
zespoly_dlugie = []
zespoly_na_r = []

# tutaj wpisz swój kod
for zespol in zespoly:
    if len(zespol) > 16:
        zespoly_dlugie.append(zespol)
    if 'The' in zespol:
        zespoly_z_the.append(zespol)
    if 'R' in zespol[0]:
        zespoly_na_r.append(zespol)

print("Zespoły z 'The' w nazwie:", zespoly_z_the)
print("Zespoły z długą nazwą:", zespoly_dlugie)
print("Zespoły na 'R':", zespoly_na_r)
