baseinput = int(input())
userinput = int(input())

Array = []

def remainder(base,Number):
    wholeNumber = Number/base
    remainder = Number%base
    return (remainder,int(wholeNumber))

def Decrypt(base,Number):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']
    
    output = str()
    number = Number
    while number != 0:
        output += Array[int(remainder(base,number)[0])]
        number = int(remainder(base,number)[1])
    return output



while(userinput != -1):

    reversedoutput = Decrypt(baseinput,userinput)[::-1]
    Array.append(reversedoutput)
    userinput = int(input())

for i in Array:
    print(i)