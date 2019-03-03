%NprocShared=8
%Mem=25712MB
#P B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Pseudo=Read
   Freq
   Integral=(Grid=UltraFine)
   Pop=Regular
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

Frequency

0 1
Ti    0.000045    0.199214   -0.564146
 O    1.372552    0.625093    0.238233
 O   -1.372388    0.625291    0.238253
 O   -0.000179   -1.924223   -0.323407
 H   -0.778041   -2.152143    0.205532
 H    0.777627   -2.152328    0.205535

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



