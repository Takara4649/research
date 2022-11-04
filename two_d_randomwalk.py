import math
import matplotlib.pyplot as plt
from src.two_d import lx
from src.two_d import ly
m=100
n=10000
p=0.5
q=1-p
r=0.5
s=1-r
values_x = [1, 0]
values_y = [1, 0]

x = [ i for i in range(n+1)]
for _ in range(m):
    zs = lx(n,p,q,values_x)
    zs.insert(0,0)
    ws = ly(n,r,s,values_y)
    ws.insert(0,0)
    #print(zs)
    #print(ws)
    plt.plot(zs, ws,color="red",lw=0.1) #label="2d_walk", color="red",lw=0.01)
plt.show()
