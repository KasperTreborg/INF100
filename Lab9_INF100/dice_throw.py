import random
import collections

def throw_n_2(n):
    
    list = []

    for i in range(n):

        t1 = random.randint(1,6)
        t2 = random.randint(1,6)

        list.append(t1+t2)

    return list

def print_histo(throws):

    dict = collections.Counter(throws)
    sorted_dict = sorted(dict.keys())
    total = sum(dict.values())

    for i in sorted_dict:
        print(f'{i}\t{"*"*int(round(dict[i]/total*100))}')