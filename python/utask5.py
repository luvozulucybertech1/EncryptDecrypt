from string import digits,ascii_uppercase,whitespace

instruction = str(input())
baseinput = int(input())
userinput = str(input())

def remainder(base, Number):
    wholeNumber = Number / base
    remainder = Number % base
    return (remainder, int(wholeNumber))

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

def Encryption(base,userinput):
    EncryptArray = [ord(c) for c in userinput]

    for i in EncryptArray:
        print(tobase(i,baseinput))

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



def Decrypt(base, Number):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

    output = ""
    number = Number
    while number != 0:
        output += Array[int(remainder(base, number)[0])]
        number = int(remainder(base, number)[1])
    return output[::-1]

def fromBase(input_str, base):
    value = 0
    for digit in input_str:
        value = base * value + int(digit, base=base)
    return value

def Decryption(baseinput,userinput):
   Array = []
   for input_str in userinput:
       if input_str == '-1':
           break
       decrypted_str = ""

       for i in range(0, len(input_str), 2):
           decrypted_str += chr(fromBase(input_str[i:i+2], baseinput))
       Array.append(decrypted_str)

   output_str = ""

   for i in Array:
        output_str += i
   print(output_str)




if instruction == "encrypt":
    Encryption(baseinput,userinput)
else:
    Decryption(baseinput,userinput)
