first = input("Første raden: ")
second = input("Andre raden: ")
third = input("Tredje raden: ")

longest = max(len(first), len(second), len(third))

print()

print("@" * longest + "@@@@")
print("@ " + (" " * (longest - len(first))) + first + " @")
print("@ " + (" " * (longest - len(second))) + second + " @")
print("@ " + (" " * (longest - len(third))) + third + " @")
print("@" * longest + "@@@@")