import math
import random
import numpy as np

O_H = 0.9584
#decide accuracy in this function
def my_round(n):
    return round(n,7)

#O -> Ti
def O_T_vector(O,Ti):
    vector = [Ti[1]-O[1],Ti[2]-O[2],Ti[3]-O[3]]
    return map(my_round,vector)

def makeO_H(vector,angle):
    norm = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector = map(lambda x:(-1.0)*x*O_H/norm,vector) 
    #normalize for O-H distance
    
    m_vector = np.matrix([[vector[0]],[vector[1]],[vector[2]]])

    theta = math.radians(angle)  
    rad76 = math.radians(76)
    inv_rad76 = math.radians(284) #inverse_rotate
    
    #rotate matrix
    #rot 76 is main rotation
    rot76 =  np.matrix([[math.cos(theta),(-1)*math.sin(theta),0],\
            [math.sin(theta),math.cos(theta),0],[0,0,1]])
    rotyz =   np.matrix([[1,0,0],[0,math.cos(rad76),(-1)*math.sin(rad76)],\
            [0,math.sin(rad76),math.cos(rad76)]])
    inv_rotyz =   np.matrix([[1,0,0],[0,math.cos(inv_rad76),(-1)*math.sin(inv_rad76)],\
            [0,math.sin(inv_rad76),math.cos(inv_rad76)]])
    rotxz = np.matrix([[math.cos(rad76),0,math.sin(rad76)],[0,1,0]\
            ,[(-1)*math.sin(rad76),0,math.cos(rad76)]])
    inv_rotxz = np.matrix([[math.cos(inv_rad76),0,math.sin(inv_rad76)],[0,1,0]\
            ,[(-1)*math.sin(inv_rad76),0,math.cos(inv_rad76)]])
    
    #xz rotate
    p0 = np.dot(rotxz,m_vector)
    #yz rotate
    p1 = np.dot(rotyz,p0)
    #main rotate
    p2 = np.dot(rot76,p1)
    #inv yz rotate
    p3 = np.dot(inv_rotyz,p2)
    #inv xz rotate
    p4 = np.dot(inv_rotxz,p3)
    p4 = p4.tolist()
    n_vector = [p4[0][0],p4[1][0],p4[2][0]]
    return map(my_round,n_vector)

def countElem(Tis,Os,Hs):
    return len(Tis)+len(Os)+len(Hs)            

def addH(TiList,OList,HList,n):
    counter = 0
    while counter < n: 
        print counter
        for i,O in enumerate(OList):
            rand = random.choice([0,1,2])
            O_HList = makeO_H_numberList(OList,HList)
            
            if O[0] == 'O2' and rand == 0: #Probability = 1/3 
                if O_HList[i] >= 2:
                    pass #limit of H = 2
                else:
                    v1 = O_T_vector(O,TiList[O[4]])
                    v2 = O_T_vector(O,TiList[O[5]]) #O[4],O[5] is closest Ti 
                    v = [v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]
                    
                    norm = math.sqrt(v[0]**2 + v[1]**2 + v[2] **2)
                    
                    v = map(lambda x : -(1.0)*x*O_H/norm,v)
                    
                    H = setH(v,O,i)
                    HList.append(H)
                    counter = counter + 1
                    if counter == n:
                        break
            
            if O[0] == 'O1':
                if O_HList[i] >= 2:
                    pass #limit of H = 2
                else:
                    if rand == 0: #case O-H
                        v = O_T_vector(O,TiList[O[4]])
                        v= makeO_H(v,76)
                        H = setH(v,O,i)
                        HList.append(H)
                        counter = counter + 1
                        if counter == n:
                            break
                    elif rand == 1:#case H-O-H
                        if O_HList[i] >= 1:
                            pass
                        else:
                            if counter + 2 > n:
                                pass
                            v  = O_T_vector(O,TiList[O[4]])
                            v1 = makeO_H(v,76)
                            H1 = setH(v1,O,i)
                            HList.append(H1)

                            v2 = makeO_H(v,-76)
                            H2 = setH(v2,O,i)
                            HList.append(H2)
                            counter = counter +2
                            if counter == n:
                                break

#H adjust true coordination
def setH(v,O,i):
    H = ['H',v[0]+O[1],v[1]+O[2],v[2]+O[3],i]
    return H


def makeO_H_numberList(OList,HList):
    O_HList = [0]*len(OList)
    for H in HList:
        O_HList[H[4]] += 1
    return O_HList    
        
def writexyz(Tis,Os,Hs,O_HList):
    f = open("out.xyz",'w')
    f.write(str(countElem(Tis,Os,Hs))+'\n')
    for i in O_HList:
        f.write(str(i))
    f.write('\n') #line for comment
    for Ti in Tis:
        f.write(str('Ti')+'\t\t')
        f.write(str(Ti[1])+'\t\t')
        f.write(str(Ti[2])+'\t\t') 
        f.write(str(Ti[3])+'\t\t')
        f.write('\n')
    for O in Os:
        f.write(str('O')+'\t\t')
        f.write(str(O[1])+'\t\t')
        f.write(str(O[2])+'\t\t') 
        f.write(str(O[3])+'\t\t')
        f.write('\n')
    for H in Hs:
        f.write(str('H')+'\t\t')
        f.write(str(H[1])+'\t\t')
        f.write(str(H[2])+'\t\t') 
        f.write(str(H[3])+'\t\t')
        f.write('\n') 
    f.close()
