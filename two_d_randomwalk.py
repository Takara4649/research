import math
import matplotlib.pyplot as plt
from src.two_d import lx, ly
from src.circle import inside_circle,outside_circle
m = 10000
n = 1000
p = 0.5
q = 1-p
r = 0.5
s = 1-r
eps = 0.5
values_x = [1, 0]
values_y = [1, 0]

#円を描画
fig, ax = plt.subplots()

ax.set_xticks(range(-n//2, (n+1)//2, n//10))
ax.set_yticks(range(-n//2, (n+1)//2, n//10))
ax.grid()

ic = inside_circle(n, eps)
oc = outside_circle(n, eps)
ax.add_patch(oc)
ax.add_patch(ic)




for _ in range(m):
    zs = lx(n,p,q,values_x)
    zs.insert(0,0)
    ws = ly(n,r,s,values_y)
    ws.insert(0,0)
    ax.plot(zs, ws,color="red",lw=0.1)
    #print(zs)
    #print(ws)


fig.savefig("img/2d_randomwalk.png")
plt.show()
