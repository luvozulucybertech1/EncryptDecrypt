import math

def spliting(Message):
    return Message.split()

def Ascii(decimal_number):
    return chr(decimal_number)

def decode(Number):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
    output =  0

    for i in Number:
        for j in range(0, len(Array)):
            if i == Array[j]:
                output = output * len(Array) + j
    return output

def remainder(base, Number):
    numerical = decode(str(Number))  # Corrected to ensure decode receives a string
    wholeNumber = numerical // base
    remainder = numerical % base
    return (remainder, wholeNumber)

def index(character):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
    index = -1
    for i in range(0, len(Array)):
        if character == Array[i]:
            index = i
            break
    return index

def Decrypt(base, Number):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

    output = ""
    number = Number
    while number != 0:
        output = Array[remainder(base, number)[0]] + output
        number = int(remainder(base, number)[1])
    return output

def Encryption(base, Number):
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

    output = ""
    number = Number
    while number != 0:
        output = Array[int(remainder(base, number)[0])] + output
        number = int(remainder(base, number)[1])
    return output

def Decryption(base, Cipher_Text):
    Array = spliting(Cipher_Text)
    output = ""
    for i in Array:
        output += Ascii(int(Decrypt(base, i)))  # Corrected to convert result to integer
    return output

message = str(input())
baseinput = int(input())
userinput = str(input())

if message == "decrypt":
    print(Decryption(baseinput, userinput))
else:
    print(Encryption(baseinput, userinput))
