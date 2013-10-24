import rhinoscriptsyntax as rs
import random as r

r.seed(seed)

list = []

for c in range(count):
    
    gaussinPoint = r.gauss(mu,sig)
    
    list.append(gaussinPoint)

a = list