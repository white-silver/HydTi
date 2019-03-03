def XYZ(Crd):
  NAtm = len(Crd)
  XYZHead(NAtm)
  XYZBody(Crd)

def XYZ2(Crd1,Crd2):
  NAt1 = len(Crd1)
  NAt2 = len(Crd2)
  NAtm = NAt1 + NAt2
  XYZHead(NAtm)
  XYZBody(Crd1)
  XYZBody(Crd2)

def XYZHead(N):
  print (N)
  print ('#')

def XYZBody(Crd):
  for i in range(len(Crd)):
    c = Crd[i][0]
    x = Crd[i][1]
    y = Crd[i][2]
    z = Crd[i][3]
    print ("%4s  %20.8f %20.8f %20.8f" % (c,x,y,z))
