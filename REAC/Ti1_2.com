%NprocShared=8
%Mem=25712MB
#T B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Opt=(MaxCyc=60,CalcFC) NoSym
   Integral=(Grid=UltraFine)
   Pop=Regular Pseudo=Read
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

TiO2

0 1
Ti    0.000000    0.185922    0.000000
 O    1.399009    1.053818    0.000000
 O   -1.398778    1.054192    0.000000
 O   -0.000176   -1.983047    0.000000
 H   -0.784138   -2.544927    0.000000
 H    0.783699   -2.545054    0.000000

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti
SDDAll



