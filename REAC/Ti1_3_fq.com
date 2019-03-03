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
Ti   -0.001242    0.049708    0.000259
 O    0.153363    1.653741   -0.000247
 O   -1.718794   -0.581233   -0.000197
 H   -2.065509   -1.478257   -0.000380
 O    1.522076   -0.942802   -0.000153
 H    2.439679   -0.652962   -0.000544

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



