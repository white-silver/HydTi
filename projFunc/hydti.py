import math
import numpy as np

O_H = 0.9584

#decide accuracy in this function
def my_round(n):
    return round(n,7)

def O_T_vector(OList,TiList):
    vector = [TiList[1]-OList[1],TiList[2]-OList[2],TiList[3]-OList[3]]
    return map(my_round,vector)

def O_H_vector(vector):
    mag = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    n_vector = map(lambda x:x*O_H/mag,vector) #normalize for O-H distance
    inv_vector = map(lambda x:-x,n_vector)
    return map(my_round,inv_vector)

def addH(O,HList):
    Hxyz = O_H_vector(O[5])
    H = ['H',Hxyz[0]+O[1],Hxyz[1]+O[2],Hxyz[2]+O[3]]
    theta = math.radians(76)
    rot76 = np.matrix([[math.cos(theta),(-1)*math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    xy = np.matrix([[Hxyz[0]],[Hxyz[1]]])
    afterRot = np.dot(rot76,xy)
    Point = afterRot.tolist()
    H[1] = my_round(Point[0][0]) + O[1] #x,i don't know but result of tolist() is list in list
    H[2] = my_round(Point[1][0]) + O[2] #y
    HList.append(H)

#rotate O-H (104 degrees)
#O is imaginary Origin
#at last, add O coordinate
def my_round(n):
    return round(n,7)

def xyzDist(a,b,c,x,y,z):
    return float(math.sqrt((a-x)**2+(b-y)**2+(c-z)**2))

def countElem(Tis,Os,Hs):
    return len(Tis)+len(Os)+len(Hs)

def writexyz(Tis,Os,Hs):
    f = open("out.xyz",'w')
    f.write(str(countElem(Tis,Os,Hs))+'\n')
    f.write('#\n') #line for comment
    for Ti in Tis:
        f.write(str(Ti[0])+'\t\t')
        f.write(str(Ti[1])+'\t\t')
        f.write(str(Ti[2])+'\t\t') 
        f.write(str(Ti[3])+'\t\t')
        f.write('\n')
    for O in Os:
        f.write(str(O[0])+'\t\t')
        f.write(str(O[1])+'\t\t')
        f.write(str(O[2])+'\t\t') 
        f.write(str(O[3])+'\t\t')
        f.write('\n')
    for H in Hs:
        f.write(str(H[0])+'\t\t')
        f.write(str(H[1])+'\t\t')
        f.write(str(H[2])+'\t\t') 
        f.write(str(H[3])+'\t\t')
        f.write('\n') 
    f.close()
