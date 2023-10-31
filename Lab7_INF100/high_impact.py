
def get_impact(line):
    yep = line.split(';')
    try:
        float(yep[2])
        return float(yep[2])
    except ValueError:
        return None

def filter_earthquakes(earthquake_csv_string, threshold):

    test = earthquake_csv_string.splitlines()
    returnStr = f'{test[0]}\n'

    for line in test:

        if get_impact(line) == None:
            continue

        if get_impact(line) >= threshold:
            returnStr += f'{line}\n'
    
    return returnStr

def filter_earthquakes_file(source_filename, target_filename, threshold):
    inputFile = open(source_filename, "r")
    outputFile = open(target_filename, "w")

    outputFile.writelines(inputFile.readline())

    for line in inputFile:

        if get_impact(line) == None:
            continue

        if get_impact(line) >= threshold:
            outputFile.writelines(line)
    
    inputFile.close
    outputFile.close