
def filter_high_temperatures(path_input, path_output, threshold_temp):
    
    inputFile = open(path_input, "r")
    outputFile = open(path_output, "w")

    for line in inputFile:
        alle = line.split()
        if((alle[2].strip('-')).isnumeric()):
            if(int(alle[2]) >= threshold_temp):
                outputFile.writelines(line)

    inputFile.close
    outputFile.close