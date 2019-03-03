from sys import *
import ChkGeom
import Cut
import Dump
import Edit
import Elements
import Hydrate
import Read
import ShfRot

if __name__ == '__main__':
# Open Base XYZ file
# This should be replaced with cif file in future. [ToDo]
  f = open(argv[1],'r')
# Read Coordinate
  Crd = Read.XYZ(f)
  f.close() 
  
# Shift XYZ so that the center-of-coordinate becomes origin
  ShfRot.CntOfCrd(Crd)

# Sphere cut of Crd.
# SCrd is the newest Crd.
  SCrd = Cut.Sphere(Crd)

# Get Elements in SCrd.
  Elms = ChkGeom.ElmList(SCrd)

# Get Metals in Elms.
  Mtls = ChkGeom.GetMetal(Elms)
# Get coordinates of metals and oxygen.
  MtlCrd = ChkGeom.GetMtlCrd(SCrd,Mtls)
  OxyCrd = ChkGeom.GetOxyCrd(SCrd)

# Calculate the coordination number
# 2.7 is threashold of bond length.
  ChkGeom.GetCrdNum(MtlCrd,OxyCrd,2.7)
  NCrMxMt = ChkGeom.GetMaxCrd(MtlCrd)
  print (OxyCrd) 
# Remove metals, whose coordination number is less than NCrMxMt.
  MtlCrd2 = ChkGeom.RmNotFullCrd(MtlCrd,NCrMxMt)

# Check the coordination number again
  ChkGeom.GetCrdNum(MtlCrd2,OxyCrd,2.7)

# Remove zero coordinated oxygen.
  OxyCrd2 = ChkGeom.RmZeroCrd(OxyCrd)

  Crd2 = Edit.CombineCrd2(MtlCrd2,OxyCrd2)
#!  Dump.XYZ(Crd2)

  O1Crd = ChkGeom.GetOxyNCrd(OxyCrd2,1)
  O2Crd = ChkGeom.GetOxyNCrd(OxyCrd2,2)

#!  Dump.XYZ(O1Crd)
#!  Dump.XYZ(O2Crd)
### Geometry check and removal of oxygen have finished.
### Hydration start.
# Calculate the number of hydrogen
  NHyd = Hydrate.CalcNumHydrgn(Crd2)
# Choose the site and number of hydrogen 
  O1Site,O2Site = Hydrate.ChooseSite(O1Crd,O2Crd,NHyd)

  HCrd = Hydrate.Init()
  Hydrate.O1Hyd1(MtlCrd2,O1Crd,O1Site,HCrd)
#  Dump.XYZ2(Crd2,HCrd)

