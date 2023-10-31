def no_duplicates(a):

    return_value = list(dict.fromkeys(a))

    return return_value

def set_difference(setA, setB):

    return_value = []

    for i in setA:
        if i not in setB:
            return_value.append(i)
        else: continue
    
    return return_value

def set_union(setA, setB):
    
    return_value = []

    for i in setA:
        if i in return_value: continue
        else: return_value.append(i)
    
    for i in setB:
        if i in return_value: continue
        else: return_value.append(i)

    return return_value

def set_intersection(setA, setB):

    return_value = []

    for i in setA:
        if i in setB:
            return_value.append(i)
        else: continue

    return return_value


print("Tester no_duplicates... ", end="")
assert([1] == no_duplicates([1, 1]))
assert([1, 3, 5, 4, 8] == no_duplicates([1, 1, 3, 5, 4, 3, 8]))
assert([1, 3, 5, 4, 8] == no_duplicates([1, 3, 5, 4, 8]))
print("OK")

print("Tester set_difference... ", end="")
assert sorted([1, 5, 8]) == sorted(set_difference([1, 3, 5, 4, 8], [2, 3, 4, 7, 6])) 
assert sorted([2 , 7, 6]) == sorted(set_difference([2, 3, 4, 7, 6], [1, 3, 5, 4, 8])) 
print("OK")

print("Tester set_union... ", end="")
assert sorted([1, 3, 5, 4, 8, 2, 7, 6]) == sorted(set_union([1, 3, 5, 4, 8], [2, 3, 4, 7, 6]))
assert sorted([2, 7, 6]) == sorted(set_union([2, 7, 6], [2, 6]))
print("OK")

print("Tester set_intersection... ", end="")
assert sorted([3 , 4]) == sorted(set_intersection([1, 3, 5, 4, 8] , [2, 3, 4, 7, 6]))
assert sorted([3]) == sorted(set_intersection([3, 4], [2, 3, 5]))
assert sorted([]) == sorted(set_intersection([3, 4], [5, 6]))
print("OK")