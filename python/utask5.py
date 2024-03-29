from string import digits,ascii_uppercase,whitespace

userinput = str()

userinput = str(input())

Array  = [len(userinput)]

Array = [ord(c) for c in userinput]

for i in Array:
    print(i, end=" ")
