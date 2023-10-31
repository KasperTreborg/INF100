first = input("Skriv et ord: ")
second = input("Skriv et annet ord: ")
third = input("Skriv et siste ord: ")

words = []
words.append(first)

if len(second) == len(first):
    words.append(second)
    if len(second) == len(third):
        words.append(third)

if len(second) < len(first):

    words.remove(first)
    
    if len(third) == len(second):
        words.append(second)
        words.append(third)
    elif len(third) < len(second):
        words.append(third)

if len(third) == len(first) and len(first) < len(second):
    words.append(third)

for x in words:
    print(x)