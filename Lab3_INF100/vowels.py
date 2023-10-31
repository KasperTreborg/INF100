inpuddy = input("Oppgi streng: ").lower()
total = 0

for letter in inpuddy:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        total += 1

if total > 1: print(f'Denne strengen inneholder {total} vokaler.')
if total == 1: print("Denne strengen inneholder 1 vokal.")
if total == 0: print("Denne strengen inneholder ingen vokal.")