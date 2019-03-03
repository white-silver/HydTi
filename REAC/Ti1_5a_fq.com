%NprocShared=8
%Mem=51491MB
#P B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Pseudo=Read
   Freq
   Integral=(Grid=UltraFine)
   Pop=Regular
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

Frequency

0 1
Ti    0.042503    0.097451   -0.061733
 O    0.916219    1.302979    0.956952
 H    0.642751    2.207214    1.138752
 O   -1.685008   -0.008674    0.432782
 H   -2.146028   -0.746401    0.842473
 O    0.842193   -1.500925    0.132702
 H    1.132301   -2.101929   -0.560085
 O    0.051959    0.605939   -1.790820
 H   -0.715137    0.647607   -2.370028

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti 0
SDDAll



