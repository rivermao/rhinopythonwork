import rhinoscriptsyntax as rs

#randomness

import random as r

r.seed(seed)

#class
class walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def point(self):
        shape = rs.AddPoint(self.x,self.y,0)
        return shape
        
    
    def step(self):
        choice = r.randint(0,3)
        if (choice == 0):
            self.x = self.x + 1

        elif (choice == 1):
            self.x = self.x - 1

        elif (choice == 2):
            self.y = self.y + 1
        else:
            self.y = self.y -1



#time
w = walker()


pList = []
for t in range(time):
    
    w.step()
    pList.append(w.point())
    
    
    
a = pList
print pList