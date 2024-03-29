from string import digits,ascii_uppercase,whitespace

userinput = str(input())

Array = [ord(c) for c in userinput]


StringsArray = []

def index(character):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']
    index = -1
    for i in range(0,len(Array)):
        if character == Array[i]:
            index = i
            break
    return index

def Encrypt(base,Number):
    output = 0
    for i in Number:
        output += index(i) * pow(base, len(Number) - 1 - index(i))
    return output

def tobase(decimal_num, base):
    result = ""

    while decimal_num > 0:
        remainder = decimal_num % base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal_num //= base

    return result

for i in Array:
    print(tobase(i,16))
