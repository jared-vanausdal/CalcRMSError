# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:12:06 2019

@author: jared
"""


from __future__ import print_function

from collections import namedtuple
from math import sqrt

testFile = open('InteractionTestData.txt','r')
refFile = open('InteractionRefData.txt','r')

Point = namedtuple('Point','X Y Z')
Couple = namedtuple('Couple','Point1 Point2')
Interaction = namedtuple('Interaction','Couple Strength')


TestData = []
RefData = []

for i, line in enumerate(testFile):
    data = line.strip().split()
    point1 = Point(float(data[0]),float(data[1]),float(data[2]))
    point2 = Point(float(data[3]),float(data[4]),float(data[5]))
    couple = Couple(point1,point2)
    Coupling = Interaction(couple,float(data[6]))
    TestData.append(Coupling)
    
for i, line in enumerate(refFile):
    data = line.strip().split()
    point1 = Point(float(data[0]),float(data[1]),float(data[2]))
    point2 = Point(float(data[3]),float(data[4]),float(data[5]))
    couple = Couple(point1,point2)
    Coupling = Interaction(couple,float(data[6]))
    RefData.append(Coupling)

TestPoints = list(map(lambda x: x.Couple, TestData))

RefData = list(filter(lambda x: x.Couple in list(map(lambda x: x.Couple,TestData)),RefData))

# Create Dictionaries for both Test and Reference Data
refDict = {}
testDict = {}

for test,ref in zip(TestData,RefData):
    refDict.update({ref.Couple : ref.Strength})
    testDict.update({test.Couple : test.Strength})

RMSErr = 0.0
numEntries = 0

for key in testDict:
    RMSErr += (testDict[key] - refDict[key])**2
    numEntries += 1

RMSErr = sqrt(RMSErr/float(numEntries))

print("RMS Error: ",RMSErr)