%NprocShared=8
%Mem=25712MB
#T B3PW91/GenECP
   SCFCon=7 SCFCyc=250 GFInput GFOldPrint
   Opt=(MaxCyc=60)
   Integral=(Grid=UltraFine)
   Pop=Regular Pseudo=Read
   IOp(1/33=0,2/11=1,3/27=8,6/7=3)

TiO2 1-3

0 1
 Ti                -0.30486194    0.14962777   -0.19039443
 O                 -1.29486194   -1.56510253   -0.19039443
 O                 -1.29486194    1.86435807   -0.19039443
 H                 -0.67139182    2.59434780   -0.19039285
 O                  1.67513806    0.14962777   -0.19039443
 H                  1.99559265   -0.08966005   -1.06312016

Ti 0
SDDAll
****
O H 0
6-31G(d,p)
****

Ti
SDDAll



