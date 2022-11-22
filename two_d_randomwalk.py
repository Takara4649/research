import math
import matplotlib.pyplot as plt
from src.two_d import lx, ly
from src.circle import outside_circle
m = 100
n = 100000
p = 0.5
q = 1-p
r = 0.5
s = 1-r
eps = 1
values_x = [1, -1]
values_y = [1, -1]

#円を描画
fig, ax = plt.subplots()

ax.set_xticks(range(-n//2, (n+1)//2, n//10))
ax.set_yticks(range(-n//2, (n+1)//2, n//10))
ax.grid()

oc = outside_circle(n, eps)
ax.add_patch(oc)





for _ in range(m):
    zs = lx(n,p,q,values_x)
    zs.insert(0,0)
    ws = ly(n,r,s,values_y)
    ws.insert(0,0)
    ax.plot(zs, ws,color="red",lw=0.01)
    #print(zs)
    #print(ws)

ax.set_xticks([-1000,-750,-500,-250,0,250,500,750,1000])
ax.set_yticks([-1000,-750,-500,-250,0,250,500,750,1000])
ax.set_aspect('equal')
fig.savefig("img/2d_randomwalk.png")
plt.show()
