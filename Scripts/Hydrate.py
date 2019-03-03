import Elements
import random
import math

def Init():
  HCrd = []
  return HCrd

def CalcNumHydrgn(Crd):
  NCh = 0
  for i in range(len(Crd)):
    c = Crd[i][0]
    if (c[-1].isdigit()): c = c[:-1]
    NCh += Elements.RtrnFrmlChrg(c)
  if (NCh > 0):
    print (" ERROR! Positively charged cluster is weired.")
    print (" Please check the geometry again.")
    quit()
  print (" Number of Hydrogen atom = %d" % -NCh)
  return -NCh

def ChooseSite(O1Crd,O2Crd,NHyd):
  NO1 = len(O1Crd)
  NO2 = len(O2Crd)
# Make number list of O1 and O2 for random choose
  LO1 = []
  for i in range(NO1):
    LO1.append(i)
  LO2 = []
  for i in range(NO2):
    LO2.append(i)
# Initialize O1Site and O2Site
  O1Site = []
  for i in range(NO1):
    O1Site.append(0)
  O2Site = []
  for i in range(NO2):
    O2Site.append(0)
#
  if (NO1 > NHyd): # Randomly select positions 
    HPos = random.sample(LO1,NHyd)
    for i in HPos:
      O1Site[i] += 1
    return O1Site,O2Site
  elif (NO1 == NHyd):
    for i in range(NO1):
      O1Site[i] += 1
    return O1Site,O2Site
  elif (NO1 < NHyd):
    for i in range(NO1):
      O1Site[i] += 1
    NRes = NHyd - NO1
    if (NO2 > NRes):
      HPos = random.sample(LO2,NHyd)
      for i in HPos:
        O2Site[i] += 1
      return O1Site,O2Site
    elif (NO2 == NRes):
      for i in range(NO2):
        O2Site[i] += 1
      return O1Site,O2Site
    elif (NO2 < NRes):
      for i in range(NO2):
        O2Site[i] += 1
      NRes2 = NRes - NO2
      if (NO1 < NRes2):
        print ("ERROR! Too few O site") 
        quit()
      elif (NO1 == NRes2):
        for i in range(NO1):
          O1List[i]  += 1
          return O1List,O2List
      elif (NO1 > NRes2):
        HPos = random.sample(LO1,NRes2)
        for i in HPos:
          O1Site[i] += 1
        return O1Site,O2Site
  
def O1Hyd1(MtlCrd,O1Crd,O1Site,HCrd):
  for i in range(len(O1Site)):
    if (O1Site[i] == 2): continue
    MPos = O1Crd[i][4]
    xm = MtlCrd[MPos][1]
    ym = MtlCrd[MPos][2]
    zm = MtlCrd[MPos][3]
    xo = O1Crd[i][1]
    yo = O1Crd[i][2]
    zo = O1Crd[i][3]
    rx = xo - xm
    ry = yo - ym
    rz = zo - zm
    rnorm = math.sqrt(rx**2 + ry**2 + rz**2)
    theta = (180.0-104.0)/180.0
    xh = xo + rx/rnorm*math.cos(theta*math.pi) - ry/rnorm*math.sin(theta*math.pi)
    yh = yo + rx/rnorm*math.sin(theta*math.pi) + ry/rnorm*math.cos(theta*math.pi)
    zh = zo + rz/rnorm
    HCrd.append(["H",xh,yh,zh])

