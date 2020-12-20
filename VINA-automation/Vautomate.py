import os
import subprocess as sp

print("Inserisci il nome dei file: ")
argbase = input()
print("Inserisci il numero di file da generare: ")
N = int(input())

# qui metti il numero di cicli:
#N = QUALCOSA
#argbase= "irinotecan"

for i in range (1, N+1):
    if i < 10:
        strI = str(0) + str(i)
    else:
        strI = str(i)
    argname = argbase + strI
    sp.run(["C:/AUTODOCKworkspace/vina.exe", "--config", "C:/AUTODOCKworkspace/config.txt", "--out", argname + ".pdbqt"])

