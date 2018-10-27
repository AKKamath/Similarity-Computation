#!/usr/bin/env python
from algorithms import *
import csv

class data:
    def __init__(self):
        self.rowSize = 0
        self.binaryType = True
        self.headerRow = []
        self.data = {}
    def addRow(self, row):
        if(self.rowSize == 0):
            self.headerRow = row
        else:
            self.data[row[0]] = [int(x) for x in row[1:-1]]
            for i in row[1:-1]:
                i = int(i)
                if(i != 0 and i != 1):
                    self.binaryType = False
        self.rowSize = self.rowSize + 1
    def outputData(self):
        print("Binary: " + str(self.binaryType))
        print(self.headerRow)
        print(self.data)

inputFile = 'input_example_binary' #raw_input("Enter file name\n")
if(not inputFile.endswith('.csv')):
    inputFile = inputFile + '.csv'

ratioData = data()

with open(inputFile) as csvFile:
    reader = csv.reader(csvFile, delimiter='\t', quotechar='|')
    for row in reader:
        ratioData.addRow(row)

ratioData.outputData()

