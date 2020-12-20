#!/usr/bin/python3

import os
import collections
import xlwt


# list of the file numbers to be searched
number_list = collections.defaultdict(list)
# list of the values found in the matching files
value_list = collections.defaultdict(list)


def parseFiles(fileName, index):
    # open the input file (read-only):
    fo = open(fileName, "r")
    # assign an array containing the file lines:
    line = fo.readlines()
    # search the correct line:
    i=0
    pippo = 1
    while ( (pippo) and (i < len(line)) ):
        # splits the line in tokens (separated by spaces):
        tokenized_line = line[i].split()
        # if the line matches:
        if (tokenized_line[0] == "REMARK") and \
           (tokenized_line[1] == "VINA")   and \
           (tokenized_line[2] == "RESULT:"):
            pippo=0
            break
        # else, go on:
        i = i + 1
    if pippo == 0:
        result = tokenized_line[3]
        value_list[index].append(result)

    fo.close()

    return


def searchFiles(path):
    # itera su tutti i file nella cartella corrente:
    for files in os.scandir(path):
        # per ogni numero specificato...
        for j in range (len(number_list)):
            # se il numero coincide con il file sotto il cursore "files"...
            if ( ( number_list[j][0] + ".pdbqt") == 
                    files.name[len(files.name)-8:]):
                # aggiungilo alla lista di file da scrivere
                file_list[i].append(files.name)
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
    number_list[pippo-1].append(temp)
    pippo = pippo + 1

# crea una lista vuota:
file_list = collections.defaultdict(list)
# indice:
i = 0

# costruisce una lista di file compatibili:
searchFiles(path)

# per ogni file che matcha l'input dell'utonto...
for filename in range (len(file_list)):
    parseFiles(file_list[filename][0], filename)

# adesso butta tutto in un file excel:
wb = xlwt.Workbook()
sheet01 = wb.add_sheet('Sheet 1')
i = 1
for element in range(len(value_list)):
    sheet01.write(i, 0, file_list[i-1][0])
    sheet01.write(i, 1, value_list[i-1][0])
    i = i + 1

wb.save("Risultati.xls")

# EOF
