%NprocShared=8
%Mem=51491MB
#T B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Opt=(MaxCyc=60,CalcFC) NoSym
   Integral=(Grid=UltraFine)
   Pop=Regular Pseudo=Read
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

TiO2 1-5a

0 1
 Ti                 0.01873970   -0.01027053    0.02610211
 O                  1.05194263    1.44362538    0.88579880
 H                  0.60397838    2.28109772    0.74591276
 O                 -1.79329280   -0.09088409    0.82010441
 H                 -2.28147100   -0.82024953    0.43112099
 O                  0.94338486   -1.73708829    0.31512074
 H                  1.22804171   -2.09348562   -0.52959899
 O                 -0.12707555    0.34326413   -1.91661536
 H                 -0.56249555    1.18725208   -2.05694982

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti
SDDAll






