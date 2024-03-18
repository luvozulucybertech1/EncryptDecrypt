baseinput = int(input())
userinput = int(input())

def NextBase(Base,Number):
    if Base == 0:
        return "0"
    
    digits = []  

    while Base != 0:
        x = Base % 3
        if x < 0:
            x += 3
        digits.append(str(x))
        Base //= 3
    return "".join(reversed(digits))

print(NextBase(baseinput,userinput))

'''
while(userinput != -1):

    userinput = int(input())'''