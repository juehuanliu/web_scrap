import csv
import json

with open('c:/data/listwithemail.csv','r') as name_file:
    # name_reader = csv.reader(name_file,delimiter = ",")
    with open('c:/data/listwithemail2.csv', 'a', newline='') as new_file:
        test_writer = csv.writer(new_file, delimiter="\t")
        for readlines in name_file:

            if readlines[1] != ']':
                units= readlines.split('\t')[0].replace("[", '').replace("]", '').replace("', '", '\t')
                print(units.split('\t')[0])

