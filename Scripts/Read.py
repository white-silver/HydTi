def XYZ(f):
  Crd = []
  NAtm = int(f.readline())
  f.readline()
  while 1:
    line = f.readline()
    if not line: break
    Crd.append(line.split())
  if (len(Crd) != NAtm):
    print (" Error: Illegal XYZ file")
    quit()
  for i in range(NAtm):
    Crd[i][1] = float(Crd[i][1])
    Crd[i][2] = float(Crd[i][2])
    Crd[i][3] = float(Crd[i][3])
  return Crd
