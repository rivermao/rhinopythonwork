import rhinoscriptsyntax as rs

import random as r

r.seed(seed)


class walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    
    def point(self):
        shape = rs.AddPoint(self.x,self.y,self.z)
        return shape
        
    
    def step(self):
        
        self.X = r.uniform(-1,1)    #use r.randint() is interger,and r.uniform()can be float
        self.Y = r.uniform(-1,1)
        self.Z = r.uniform(-1,1)
        
        self.x += self.X
        self.y += self.Y
        self.z += self.Z


#time

w = walker()
pList = []

for t in range(time):
    
    w.step()
    pList.append(w.point())
    

a = pList