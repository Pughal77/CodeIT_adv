'''
    Signup
        1. Ask the user for three signups
            - Each signup should consist of a name and age
        2. Write the signups to a file called signups4.csv
        3. The first row of the csv file should be the name of the columns (Name,Age)
'''
import csv

with open("signups4.csv","w") as write_file:
  writing = csv.writer(write_file)
  writing.writerow(["name","age"])
  for i in range(3):
    name = input("name: ")
    age = input("age: ")
    one_row = writing.writerow([name,age])
    
  
