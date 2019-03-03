%NprocShared=8
%Mem=25712MB
%chk=Ti1_TS23_IRC.chk
#P B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Pseudo=Read
   IRC=(RCFC,MaxPoints=30) Guess=Read
   Integral=(Grid=UltraFine)
   Pop=Regular
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

Frequency

0 1
Ti    0.568541    0.233602   -0.417504
 O    0.334919   -1.159371    0.544438
 O    1.438397    1.395634    0.307534
 O   -1.457922    0.165198   -0.250383
 H   -1.951762    0.738580    0.346792
 H   -0.907727   -0.699536    0.313716

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



