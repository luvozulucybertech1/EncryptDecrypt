import math

instruction = str()
baseinput = int()
Message = str(input()).split()


def isnum(Insert): #check for -1 when using
    Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    isThere = False
    index = -1
    for i in range(0,len(Array)):
        if Insert == Array[i]:
            isThere = True
            index = i
            break
    return (isThere,index)

def check(Message):
    word = str()
    for i in Message:
        for j in i:
            if isnum(j)[0] == True:
               #Decrypt index
                word += chr(isnum(j)[1])
            else:
                #change to ascii
                word += chr(ord(j))
    return word

print(check(Message))
#print(num == '2')