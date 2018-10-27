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
            self.data[row[0]] = [float(x) for x in row[1:]]
            for i in row[1:]:
                i = float(i)
                if(i != 0 and i != 1):
                    self.binaryType = False
        self.rowSize = self.rowSize + 1

    def outputData(self):
        print("Binary: " + str(self.binaryType))
        print(self.headerRow)
        print(self.data)

    def compare(self, key1, key2):
        print(self.data[key1])
        print(self.data[key2])
        if(self.binaryType):
            print("\nBinary data detected")
            print("Simple Matching: " + str(simple_matching_coefficient(self.data[key1], self.data[key2])))
            print("Jaccard Coefficient: " + str(jaccard_coefficient(self.data[key1], self.data[key2])))
            print("Cosine Similarity: " + str(cosine_similarity(self.data[key1], self.data[key2])))
        else:
            print("\nNon-binary data detected")
            print("Manhattan Distance: " + str(manhattan_distance(self.data[key1], self.data[key2])))
            print("Euclidean Distance: " + str(euclidean_distance(self.data[key1], self.data[key2])))
            print("Minkowski Distance (p = 3): " + str(minkowski_distance(self.data[key1], self.data[key2], 3)))
            print("Chebyshev Distance: " + str(chebyshev_distance(self.data[key1], self.data[key2])))
            print("Pearson Correlation Distance: " + str(pearson_correlation_distance(self.data[key1], self.data[key2])))
            print("Tanimoto Coefficient: " + str(tanimoto_coefficient(self.data[key1], self.data[key2])))
            print("Cosine Similarity: " + str(cosine_similarity(self.data[key1], self.data[key2])))
        print("")
    def keyname(self):
        return self.headerRow[0]
                    

inputFile = raw_input("Enter file name\n")
if(not inputFile.endswith('.csv')):
    inputFile = inputFile + '.csv'

ratioData = data()

with open(inputFile) as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in reader:
        ratioData.addRow(row)

opt = 0
while(opt != 3):
    opt = int(raw_input("1. Output Data\n2. Similarity Comparison\n3. Exit\n"))
    if(opt == 1):
        ratioData.outputData()
    if(opt == 2):
        key1 = raw_input("Enter " + str(ratioData.keyname()) + " for 1st object: ")
        key2 = raw_input("Enter " + str(ratioData.keyname()) + " for 2nd object: ")
        ratioData.compare(key1, key2)
