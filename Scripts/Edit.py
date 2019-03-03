def CombineCrd2(CrdIn1,CrdIn2):
  CrdOut = []
  for i in range(len(CrdIn1)):
    CrdOut.append(CrdIn1[i][:])
  for i in range(len(CrdIn2)):
    CrdOut.append(CrdIn2[i][:])
  return CrdOut
