# coding: utf-8

import os
import numpy as np
import time

distance_dir=os.path.join(os.getcwd(),'m1.txt')
fee_dir=os.path.join(os.getcwd(),'m2.txt')
print('distance_dir:',distance_dir)
print('fee_dir:',fee_dir)

def readfile(file_dir):
    res=[]
    with open(file_dir,'r') as f:
        for line in f.readlines():
            linelist=[int(i) for i in line.split()]
            res.append(linelist)
    return res

distance_arr=np.array(readfile(distance_dir))
fee_arr=np.array(readfile(fee_dir))
print(distance_arr)
print(fee_arr)

def floyd(D):
    lengthD = len(D)                   
    P =np.array(D)
    
    for k in range(lengthD):
        for i in range(lengthD):
            for j in range(lengthD):
                if(P[i,j] > P[i,k]+P[k,j]):         
                    P[i,j] = P[i,k]+P[k,j]                
    return P

min_distance_arr=floyd(distance_arr)
min_distance_arr[49][49]=0
print(min_distance_arr.tolist())
#print(distance_arr.tolist())
min_fee_arr=floyd(fee_arr)
min_fee_arr[49][49]=0
#print(min_fee_arr.tolist())

stack=[0 for i in range(51)]
visited=[0 for i in range(51)]
depth=0
stack[depth]=0
stack[depth+1]=0
currentDist=0
distBound=9998
currentFee=0
feeBound=1500
bestPath=[]
shortestDist=9999
minimumFee=9999

startTime=time.time()
while(depth>=0):
    cur=stack[depth]
    next_=stack[depth+1]
    nextnode=0
    for i in range(next_+1,50):
        if distance_arr[cur][i]==9999 or visited[i]==1:
            continue 
        if currentDist+distance_arr[cur][i]+min_distance_arr[i][49]>=distBound or currentFee+fee_arr[cur][i]+min_fee_arr[i][49]>feeBound:
            continue 
        nextnode=i
        break
    if(nextnode==0):
        depth=depth-1
        currentDist-=distance_arr[stack[depth]][stack[depth+1]]
        currentFee-=fee_arr[stack[depth]][stack[depth+1]]
        visited[stack[depth+1]]=0
    else:
        #print(nextnode)
        #print(currentDist,' ',distance_arr[cur][i],' ',min_distance_arr[i][49],' ',currentDist+distance_arr[cur][i]+min_distance_arr[i][49])
        currentDist+=distance_arr[cur][nextnode]
        currentFee+=fee_arr[cur][nextnode]
        visited[nextnode]=1
        depth+=1
        stack[depth]=nextnode
        stack[depth+1]=0
        if nextnode==49:
            bestPath.clear()
            for i in range(depth+1):
                bestPath.append(stack[i]+1)
            #print('found a solution:',bestPath,' the dis is:',currentDist)
            shortestDist=currentDist
            minimumFee=currentFee
            distBound=currentDist
            depth-=1
            currentDist-=distance_arr[stack[depth]][stack[depth+1]]
            currentFee-=fee_arr[stack[depth]][stack[depth+1]]
            visited[stack[depth+1]]=0
costTime=time.time()-startTime

print('shortestDist:',shortestDist)
print('minimumFee:',minimumFee)
print('bestPath:',bestPath)
print('costTime:',costTime)

