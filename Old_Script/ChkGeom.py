def ElmList(Crd):
  Elm = []
  for i in range(len(Crd)):
    Elm.append(Crd[i][0]) 
  return list(set(Elm))
 
def GetMetal(Elms):
  Mtl = Elms[:]
  Mtl.remove('O')
  return Mtl

def GetMtlCrd(Crd,Mtl):
  MCrd = []
  for i in range(len(Crd)):
    c = Crd[i][0]
    if (c in Mtl): MCrd.append(Crd[i][:])
  return MCrd

def GetOxyCrd(Crd):
  OCrd = []
  for i in range(len(Crd)):
    c = Crd[i][0]
    if (c == 'O'): OCrd.append(Crd[i][:])
  return OCrd

def GetOxyNCrd(CrdIn,N):
  CrdOut = []
  for i in range(len(CrdIn)):
    ncrd = int(CrdIn[i][0][-1])
    if (ncrd == N): CrdOut.append(CrdIn[i][:])
  return CrdOut

def GetCrdNum(Crd1,Crd2,Thr):
  Thr2 = Thr**2
# Refresh Crd1 and Crd2 if necessary
  for i in range(len(Crd1)):
    if (len(Crd1[i]) > 4):
      del Crd1[i][4:]
    c = Crd1[i][0]
    if (c[-1].isdigit()): Crd1[i][0] = c[:-1]
  for i in range(len(Crd2)):
    if (len(Crd2[i]) > 4):
      del Crd2[i][4:]
    c = Crd2[i][0]
    if (c[-1].isdigit()): Crd2[i][0] = c[:-1]

  for i in range(len(Crd1)):
    x0 = Crd1[i][1]
    y0 = Crd1[i][2]
    z0 = Crd1[i][3]
    for j in range(len(Crd2)):
      x1 = Crd2[j][1]
      y1 = Crd2[j][2]
      z1 = Crd2[j][3]
      r2 = (x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2
      if (r2 <= Thr2):
        Crd1[i].append(j)

  for i in range(len(Crd2)):
    x0 = Crd2[i][1]
    y0 = Crd2[i][2]
    z0 = Crd2[i][3]
    for j in range(len(Crd1)):
      x1 = Crd1[j][1]
      y1 = Crd1[j][2]
      z1 = Crd1[j][3]
      r2 = (x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2
      if (r2 <= Thr2):
        Crd2[i].append(j)

# Check Coordination Number
  for i in range(len(Crd1)):
    ncrd = len(Crd1[i]) - 4
    c = Crd1[i][0] + str(ncrd)
    Crd1[i][0] = c
  for i in range(len(Crd2)):
    ncrd = len(Crd2[i]) - 4
    c = Crd2[i][0] + str(ncrd)
    Crd2[i][0] = c

def GetMaxCrd(Crd):
  NMax = 0
  for i in range(len(Crd)):
    ncrd = int(Crd[i][0][-1])
    if (ncrd > NMax): NMax = ncrd
  return NMax

def RmNotFullCrd(CrdIn,NMxCrd):
  CrdOut = []
  for i in range(len(CrdIn)):
    ncrd = int(CrdIn[i][0][-1])
    if (ncrd == NMxCrd):
      CrdOut.append(CrdIn[i][:])
  return CrdOut

def RmZeroCrd(CrdIn):
  CrdOut = []
  for i in range(len(CrdIn)):
    ncrd = int (CrdIn[i][0][-1])
    if (ncrd > 0):
      CrdOut.append(CrdIn[i][:])
  return CrdOut
