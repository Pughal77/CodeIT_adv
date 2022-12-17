'''
    Filter
        1. Take in a csv file name as a command line argument 
           (signups1.csv, signups2.csv or signups3.csv)
        2. Read from that csv file name using the csv module
        3. Print out the names of signups with age > 18 from the data read
'''
import csv 
import sys

with open(sys.argv[1], "r") as csv_file:
  read_file = csv.reader(csv_file)
  line_num = 0
  for row in read_file:
    if line_num == 0:
      line_num += 1
      pass
    else:
        if int(row[1])>18:
          print(row)
        else:
          pass


