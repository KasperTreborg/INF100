menneske = int(input("Angi menneskeår: "))

if menneske == 1: print("Dette tilsvarer 15 katteår.")
if menneske == 2: print("Dette tilsvarer 24 katteår.")
if menneske > 2:
    print(f'Dette tilsvarer {24 + ((menneske-2)*4)} katteår.')