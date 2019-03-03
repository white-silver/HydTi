def Sphere(Crd):
  crad = raw_input(' Sphere Cutting Radius (angstrom) = ')
  radsq = float(crad)**2

  NAtm = len(Crd)
  SCrd = []
  for i in range(NAtm):
    x = Crd[i][1]
    y = Crd[i][2]
    z = Crd[i][3]
    rsq = x**2 + y**2 + z**2 
    if (rsq <= radsq):
      SCrd.append(Crd[i][:])

  return SCrd

