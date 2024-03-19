baseinput = int(input())
userinput = int(input())

def NextBase(Base, Number):
    if Base == 0:
        return "0"
    
    digits = []  

    while Number != 0:
        x = Number % Base  # Fixed: Calculate modulo with Base, not Base % Base
        if x < 0:
            x += Base
        digits.append(str(x))
        Number //= Base  # Fixed: Divide by Base, not Base //= Base
    return "".join(reversed(digits))

Array = []


while(userinput != -1):

    Array.append(NextBase(baseinput, userinput))
    userinput = int(input())

for i in Array:
    print(i)