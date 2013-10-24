import rhinoscriptsyntax as rs
import perlin 


sn = perlin.SimplexNoise()

pList = []

for i in range(x):
    for j in range(y):
        
        perVal = sn.noise2(i*scaleX,j*scaleY)
        
        
        point = rs.AddPoint(i,j,perVal)
        pList.append(point)

a = pList