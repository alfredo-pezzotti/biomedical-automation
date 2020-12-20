#!/usr/bin/python3

import os
import collections
import xlwt


# lista dei numeri da cercare
lista_numeri = collections.defaultdict(list)
# lista dei valori trovati nei file
lista_valori = collections.defaultdict(list)


def parseFiles(fileName, index):
    # apro il file in lettura
    fo = open(fileName, "r")
    # assegno un array di linee:
    line = fo.readlines()
    # cerco la linea giusta:
    i=0
    pippo = 1
    while ( (pippo) and (i < len(line)) ):
        tokenized_line = line[i].split()
        if (tokenized_line[0] == "REMARK") and \
           (tokenized_line[1] == "VINA")   and \
           (tokenized_line[2] == "RESULT:"):
            pippo=0
            break
        i = i + 1
    
    result = tokenized_line[3]
    lista_valori[index].append(result)

    fo.close()

    return


def searchFiles(path):
    # itera su tutti i file nella cartella corrente:
    for files in os.scandir(path):
        # per ogni numero specificato...
        for j in range (len(lista_numeri)):
            # se il numero coincide con il file sotto il cursore "files"...
            if ( ( lista_numeri[j][0] + ".pdbqt") == 
                    files.name[len(files.name)-8:]):
                # aggiungilo alla lista di file da scrivere
                lista_files[i].append(files.name)
    return



""" 
    MAIN
"""

print("\nImmetti i numeri dei file da scrivere \n(esempio: scrivi \
01 per il file file01.pdbqt). \n\
Inserisci una linea vuota quando hai finito. \nQuesto software \
non funge se provi a iterare su piu' di 100 file \n(e in quel \
caso secondo me stai fuori)\n")

# piglia la directory di lavoro corrente:
path = os.getcwd()

pippo = 1
while pippo:
    print("immettere il file " + str(pippo) + " da scrivere: ")
    temp = input()
    if (len(temp) == 0):
        pippo = 0
        break
    lista_numeri[pippo-1].append(temp)
    pippo = pippo + 1

# crea una lista vuota:
lista_files = collections.defaultdict(list)
# indice:
i = 0

# costruisce una lista di file compatibili:
searchFiles(path)

# per ogni file che matcha l'input dell'utonto...
for filename in range (len(lista_files)):
    parseFiles(lista_files[filename][0], filename)

# adesso butta tutto in un file excel:
wb = xlwt.Workbook()
foglio01 = wb.add_sheet('Foglio 1')
i = 1
for element in range(len(lista_valori)):
    foglio01.write(i, 0, lista_files[i-1][0])
    foglio01.write(i, 1, lista_valori[i-1][0])
    i = i + 1

wb.save("Risultati.xls")

# EOF
