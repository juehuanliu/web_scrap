import csv
import glob
import os

temp = {}
os.chdir("F:/PycharmProjects/web scrape/tech")
count = 0
with open('cleaned_tech.csv','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")
    with open('merged_finance.csv', 'r') as read_file:
        test_read = csv.reader(read_file, delimiter=",")
        for line in test_read:
            try:
                temp[line[0]] = line[1]
            except:
                continue
    with open('merged_tech.csv', 'r') as new_file2:
        test_read2 = csv.reader(new_file2, delimiter=",")
        for line in test_read2:
            try:
                if temp.get(line[0]) is None:
                    test_writer.writerow(line)
                    count += 1
            except:
                continue
    print(count)