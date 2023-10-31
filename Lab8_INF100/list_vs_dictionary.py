
def key_value_getter(d):
    
    print("Dictionary keys:")
    for i in d:
        if(i == list(d)[-1]):
            print(f"{i}\n")
        else:
            print(i)
    
    print("Dictionary values:")
    for i in d:
        if(i == list(d)[-1]):
            print(f"{d[i]}\n")
        else:
            print(d[i])
    
    print("Dictionary keys/value:")
    for i in d:
        print(f"{i} {d[i]}")

def index_value_getter(a):
    
    print("List indices:")
    for i in range(len(a)):
        print(i)
        if(i == len(a)-1):
            print("")
    
    print("List values:")
    for i in range(len(a)):
        print(a[i])
        if(i == len(a)-1):
            print("")
    
    print("List indices/value:")
    for i in range(len(a)):
        print(f'{i} {a[i]}')

key_value_getter({
  "monday": 0,
  "tuesday": 0.7,
  "wednesday": 0,
  "thursday": 4.7,
  "friday": 10
})