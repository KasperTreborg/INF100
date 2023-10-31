first = input("Skriv et ord: ")
second = input("Skriv et annet ord: ")
third = input("Skriv et siste ord: ")

if len(first) >= len(second) and len(first) >= len(third):
    print(first)

elif len(second) > len(first) and len(second) >= len(third):
    print(second)

elif len(third) > len(first) and len(third) > len(second):
    print(third)