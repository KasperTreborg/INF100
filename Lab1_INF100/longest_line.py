print("Hva er ditt navn?")
navn = input()
print("Hva er din adresse?")
adresse = input()
print("Hva er ditt postnummer og poststed?")
postnummerOgPoststed = input()

print(max(len(navn), len(adresse), len(postnummerOgPoststed)))