#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file

  for line in inFile:
    info = line.split(" ")

    firstName = info[0]
    lastName = info[1]

    while len(lastName) < 5:
      lastName += "x"

    id = info[3]
    major = info[6][0:3].upper()

    grade = info[5]
    if grade == "Freshman":
      grade = "FR"
    elif grade == "Sophomore":
      grade = "SO"
    elif grade == "Junior":
      grade = "JR"
    else:
      grade = "SR"

    f = firstName[0:1].lower()
    id = id[8:11]

    userID = f + lastName.lower() + id
    majorYear = major + "-" + grade

    outFile.write(lastName + ", " + firstName + ", " + userID + ", " + majorYear + "\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
