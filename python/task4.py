import math

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
    for i in range(0,len(Number)):
        output += index(Number[i]) *pow(base,i)
    return output

baseinput = int(input())
userinput = str(input())
Array = []

while userinput != "-1":
    Array.append(Encrypt(baseinput,userinput[::-1]))
    userinput = str(input())

for i in Array:
    print(i)