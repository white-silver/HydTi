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
Ti   -0.178548   -0.085833    0.228763
 O   -0.399288    1.511078    0.026770
 O    1.563524   -0.637333   -0.046416
 H    1.801686   -1.511318   -0.371971
 O   -1.519992   -1.130752   -0.431768
 H   -2.315433   -0.820005   -0.874340
 O   -0.096894   -0.050448    2.369008
 H    0.777769   -0.324693    2.676574
 H   -0.208479    0.876966    2.621975

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



