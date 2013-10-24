import rhinoscriptsyntax as rs


x = 50
y = 50

xSpeed = 1
ySpeed = 3

upperBounds = 90


for t in range(time):
    
    x += xSpeed
    y += ySpeed
    
    if x < 0 or x > upperBounds:
        
        xSpeed *= -1
    
    if y < 0 or y > upperBounds:
        ySpeed *= -1


a = rs.AddSphere([x,y,0],5)