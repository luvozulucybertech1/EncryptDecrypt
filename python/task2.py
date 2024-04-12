
userinput = int()


userinput = int(input())

def Decrypt(userinput):
    terminalOutput = str()
    while userinput != -1:
        terminalOutput += chr(userinput)
        userinput = int(input())
    return terminalOutput
print(Decrypt(userinput))