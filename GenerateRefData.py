# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:04:04 2019

@author: jared
"""

import random

f = open("InteractionRefData.txt",'w')

nSamples = 100

for i in range(0,nSamples):
    x1 = 2*random.random() - 1
    y1 = 2*random.random() - 1
    z1 = 2*random.random() - 1
    x2 = 2*random.random() - 1
    y2 = 2*random.random() - 1
    z2 = 2*random.random() - 1
    interaction = 10*random.random() - 5
    line = "%0.2f %0.2f %0.2f %0.2f %0.2f %0.2f %0.5f \n" % (x1, y1, z1, x2, y2, z2, interaction)
    f.writelines(line)

f.close()
