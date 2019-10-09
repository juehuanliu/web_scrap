import csv
import glob
import os

temp = {}
os.chdir("F:/PycharmProjects/web scrape/finance")
count = 0
with open('merged_finance.csv','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")
    for file in glob.glob("*.csv"):
        with open(file, 'r') as read_file:
            test_read = csv.reader(read_file, delimiter=",")
            for line in test_read:
                try:
                    temp[line[0]] = line[1]
                except:
                    continue
    for name,web in temp.items():
        test_writer.writerow([name, web])
        count +=1
    print(count)