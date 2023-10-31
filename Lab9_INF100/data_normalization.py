

def norm_0_1(x):
    minste = min(x)
    storste = max(x)
    ny_liste = []

    for i in x:
        ny_liste.append((i - minste)/(storste - minste))

    return ny_liste

def norm_neg1_1(x):
    minste = min(x)
    storste = max(x)
    ny_liste = []

    for i in x:
        ny_liste.append((2*(i - minste)/(storste - minste))-1)

    return ny_liste

if __name__ == '__main__':
    print("Normaliser data.")
    intput_data = input("Oppgi data du vil normalisere, separert av mellomrom:\n")
    input_list = [float(x) for x in intput_data.split()]

    result_0_1 = norm_0_1(input_list)
    result_neg1_1 = norm_neg1_1(input_list)

    print("norm_0_1:", result_0_1)
    print("norm_neg1_1:", result_neg1_1)