def CntOfCrd(Crd):
  NAtm = len(Crd)
  # Calculate Center-Of-Coordinate
  cx = 0.0
  cy = 0.0
  cz = 0.0
  for i in range(NAtm):
    cx += Crd[i][1]
    cy += Crd[i][2]
    cz += Crd[i][3]
  cx /= float(NAtm)
  cy /= float(NAtm)
  cz /= float(NAtm)

  # Parallel shift
  for i in range(NAtm):
    Crd[i][1] -= cx
    Crd[i][2] -= cy
    Crd[i][3] -= cz
