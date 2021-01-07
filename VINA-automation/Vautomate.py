import os
import subprocess as sp

print("Insert the files' base name: ")
argbase = input()

inputError = True
while inputError:
    try:
        print("How many times you want to run the simuation? ")
        N = int(input())
        inputError=False
    except ValueError:
        print("Please insert a valid number.")
        continue

startValue = 1
inputError = True
while inputError:
    try:
        print("Which simulation number do you want to start from?\n\
Press RETURN for defalt (1)")
        startValue = int(input())
        inputError = False
    except ValueError:
        print("Please insert a valid number.")
        continue

# qui metti il numero di cicli:
#N = QUALCOSA
#argbase= "irinotecan"

for i in range (startValue, startValue + N + 1):
    if i < 10:
        strI = str(0) + str(i)
    else:
        strI = str(i)
    argname = argbase + strI
    sp.run(["C:/AUTODOCKworkspace/vina.exe", "--config", "C:/AUTODOCKworkspace/config.txt", "--out", argname + ".pdbqt"])

