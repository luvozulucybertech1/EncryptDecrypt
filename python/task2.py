
userinput = int()
terminalOutput = str()

userinput = int(input())
while userinput != -1:
    terminalOutput += chr(userinput)
    userinput = int(input())
print(terminalOutput)