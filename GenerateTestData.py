# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:50:21 2019

@author: jared
"""
from collections import namedtuple
import random

Point = namedtuple('Point','X Y Z')

f = open("InteractionRefData.txt",'r')
outfile = open("InteractionTestData.txt",'w')

for i, line in enumerate(f):
    data = line.strip().split()
    p1 = Point(float(data[0]),float(data[1]),float(data[2]))
    p2 = Point(float(data[3]),float(data[4]),float(data[5]))
    interaction = 10*random.random() - 5
    line = "%0.2f %0.2f %0.2f %0.2f %0.2f %0.2f %0.5f \n" % (p1.X,p1.Y,p1.Z,p2.X,p2.Y,p2.Z,interaction)
    outfile.writelines(line)

f.close()
outfile.close()