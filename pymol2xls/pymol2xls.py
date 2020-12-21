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
    # iterate over each file in current directory:
    for files in os.scandir(path):
        # for each file...
        for j in range (len(number_list)):
            # if current file matches the "files" identifier...
            if ( ( number_list[j][0] + ".pdbqt") == 
                    files.name[len(files.name)-8:]):
                # add the file to the list of files whose 
                # values areto be exported
                file_list[i].append(files.name)
    return



""" 
    MAIN
"""

print("\nInsert the numbers identifying the files \nto be written \
(e.g.: write 01 for file file01.pdbqt). \n\
Insert an empty line to start the computation. \n\
Don't use this software over more than 100 files. \n\n")

# piglia la directory di lavoro corrente:
path = os.getcwd()

pippo = 1
while pippo:
    print("Insert the file " + str(pippo) + " to be parsed: ")
    temp = input()
    if (len(temp) == 0):
        pippo = 0
        break
    number_list[pippo-1].append(temp)
    pippo = pippo + 1

# create an empty list:
file_list = collections.defaultdict(list)
# index:
i = 0

# builds a list of matching files:
searchFiles(path)

# for each file matching the user's input...
for filename in range (len(file_list)):
    parseFiles(file_list[filename][0], filename)

# now write the results to a spreadsheet:
wb = xlwt.Workbook()
sheet01 = wb.add_sheet('Sheet 1')
i = 1
for element in range(len(value_list)):
    sheet01.write(i, 0, file_list[i-1][0])
    sheet01.write(i, 1, value_list[i-1][0])
    i = i + 1

wb.save("Results.xls")

# EOF
