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
Ti   -1.564845    0.000000    1.351425
Ti    1.564845    0.000000    1.351425
Ti    0.000000    1.597333   -0.981597
Ti    0.000000   -1.597333   -0.981597
 O    0.000000    0.000000    2.287505
 O    1.475720   -1.372257    0.339461
 O    1.475720    1.372257    0.339461
 O   -1.475720   -1.372257    0.339461
 O   -1.475720    1.372257    0.339461
 O    0.000000    0.000000   -1.882417
 O    0.000000    2.927626   -1.898493
 O    0.000000   -2.927626   -1.898493

Ti 0
SDDAll
****
O 0
6-31G(d,p)
****

Ti 0
SDDAll



