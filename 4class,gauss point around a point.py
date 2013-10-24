import rhinoscriptsyntax as rs
import random as r

if seed == None : seed = 1

r.seed(seed)

list = []


if (sdX == None) : sdX = 20
if (sdY == None) : sdY = 20
if (sdZ == None) : sdZ = 20


if centerPoint == None : centerPoint = [0,0,0]
if pointNum == None : pointNum = 20

for p in range(pointNum):
    
    x = r.gauss(centerPoint[0],sdX)
    y = r.gauss(centerPoint[1],sdY) 
    z = r.gauss(centerPoint[2],sdZ)    
    
    point = rs.AddPoint(x,y,z)
    list.append(point)

a = list