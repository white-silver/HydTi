%NprocShared=8
%Mem=25712MB
#T B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Opt=(MaxCyc=60,CalcFC,TS,NoEigenTest)
   Integral=(Grid=UltraFine) NoSym
   Pop=Regular Pseudo=Read
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

TiO2 1 TS2-3

0 1
 Ti                 0.28480400    0.00001000   -0.36095000
 O                  0.76721000   -1.37241100    0.40892300
 O                  0.76694900    1.37252900    0.40891200
 O                 -1.44506127    0.45872436   -0.32563294
 H                 -1.50973151    1.29410338    0.15888097
 H                 -0.83972491   -1.07884780    0.55445943

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti
SDDAll





