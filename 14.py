import queue
import math

vis = {}
vis[0] = 0
vis[1] = 1
n = 1000001

def dfs(n: int):
    if vis.get(n) is not None:
        return vis[n]

    if n % 2 == 0:
        vis[n] = dfs(int(n/2)) + 1
    else:
        vis[n] = dfs(n * 3 + 1) + 1
    return vis[n]

res = 0
for i in range(2, 1000000):
    res = max(res, dfs(i))
    if res == dfs(i):
        print(i)

print(res)