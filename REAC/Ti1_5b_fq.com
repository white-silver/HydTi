%NprocShared=8
%Mem=51488MB
#P B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Pseudo=Read
   Freq
   Integral=(Grid=UltraFine)
   Pop=Regular
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

Frequency

0 1
Ti    0.000206    0.000178   -0.000455
 O   -0.145397    1.473532   -1.026430
 H   -0.743946    2.213418   -0.885380
 O   -1.463037   -0.180668    1.034140
 H   -2.205556   -0.772004    0.877143
 O    0.172107   -1.428255   -1.084264
 H    0.765858   -2.174904   -0.959426
 O    1.436903    0.135587    1.077329
 H    2.182862    0.733116    0.967342

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



