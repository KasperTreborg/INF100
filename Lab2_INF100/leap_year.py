år = int(input("Angi år: "))

if år % 4 == 0:
    if år % 100 == 0:
        if år % 400 == 0: print("Dette er et skuddår.")
        else: print("Dette er ikke et skuddår.")
    else: print("Dette er et skuddår.")
else: print("Dette er ikke et skuddår.")