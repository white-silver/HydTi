import sys
import math
import numpy as np
from hydti import *

#O[0] = name, [1][2][3] = xyz,[4]=closest Ti.[5]=O->Ti vector

args = sys.argv

O_H = 0.9584

f = open(args[1],'r')
data = f.read()
f.close() #args[1] is xyz file

k = data.count('Ti')
m = data.count('O')
n = -4*k + 2*m #4k + n - 2m = 0, n is number of H

x = 2*m - n #x+y=6,x+2y=8 
y = n - m #x is number of OH, y is H2O

xyzList = data.split()
num_nameList = xyzList[:2]
numOfElements = num_nameList[0]; #number of elements
del xyzList[:2]  #cut NofElements & Name

TiList = xyzList[:k*4]
OList = xyzList[-m*4:]
HList = []

for i in xrange(len(TiList)): #convert to float
    try:
        TiList[i] = float(TiList[i])
    except ValueError:
        pass
for j in xrange(len(OList)):
    try:
        OList[j] = float(OList[j])
    except ValueError:
        pass

TiList = [TiList[i:i+4] for i in range(0,len(TiList),4)] #split to each Ti
OList = [OList[i:i+4] for i in range(0,len(OList),4)] #split to each O

#Append closest Ti data
for O in OList:
    num = float('inf')
    index = 0
    for i,Ti in enumerate(TiList):
        dist = xyzDist(O[1],O[2],O[3],Ti[1],Ti[2],Ti[3])
        if dist < num:
            num = dist  
            index = i
    O.append(index)
          
#Append O->Ti vector
#O[4] is closest Ti index
for O in OList:
    O.append(O_T_vector(O,TiList[O[4]]))

#addH or H2(now H only)
for O in OList:
    addH(O,HList)

writexyz(TiList,OList,HList)

print TiList #debug print
print OList
print HList
