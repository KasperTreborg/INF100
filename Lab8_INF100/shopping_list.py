
def shopping_list_to_dict(shopping_list):

    dict = {}
    test = shopping_list.split("\n")

    for i in test:
        try:
            key, value = i.split(" ", 1)
            dict[value] = int(key)
        except ValueError:
            continue
    
    return dict

def shopping_list_file_to_dict(path):
    inputFile = open(path, "r")
    streng = ""

    for line in inputFile:
        streng += line + "\n"
    
    value = shopping_list_to_dict(streng)

    inputFile.close

    return value