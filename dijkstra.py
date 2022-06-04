import math
from re import S
import pandas as pd
import numpy as np

t = 11

l = pd.read_csv(filepath_or_buffer="link_2.csv", encoding="utf_8", sep=",")
d = [math.inf] * t
#global visited
visited = [False] * t
previous = []
d[0] = 0
visited[0] = True

def S():
    return [x for x in range(t) if d[x] != math.inf]

def adjecent(w):
    global a
    global D
    #create a list of adjecent vertices 
    a = l.values[(l["n1"] == w),2].tolist() + l.values[(l["n2"] == w),1].tolist()
    for i in a:
        if  visited[i] == True:
            a.remove(i)
    D = [d[x] for x in range(t) if visited[x] is False]

c = 0
adjecent(0)

while len(S()) != 0:
    if c == 0:
        w = 0
    else:
        w = d.index(min(D))
    
    if w == t - 1:
        print(d[w])
        path = []
        i = t-1
        while i != 0:
            i = previous[i]
            path.append(i)
        path.reverse()
        print("path : ", path)
        #探索終了
        break

    visited[w] = True
    adjecent(w)
    #print("w ",w)
    #print("a ",a)
    #print("d ",d)

    for i in a:
        distance = l[((l["n1"] == w) & (l["n2"] == i))].index.tolist()
        if len(distance) == 0:
            distance = l[((l["n1"] == i) & (l["n2"] == w))].index.tolist()
        new_dist = int(d[w]) + l.values[distance[0],3]
        if d[i]  > new_dist:
            d[i] = new_dist
    adjecent(w)
    
    c += 1
    if c == t:
        print("faile")
        break
