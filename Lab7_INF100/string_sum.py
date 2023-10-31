
def add_together(s):
    inp = s.split()
    final = 0

    for i in inp:
        if((i.strip('-')).isnumeric()):
            final += int(i)
        else:
            continue
    
    return final