
userinput = int()
terminalOutput = str()

userinput = int(input())

def Decrypt(userinput):
    while userinput != -1:
        terminalOutput += chr(userinput)
        userinput = int(input())
print(terminalOutput)