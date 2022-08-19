import math 
from re import S
import pandas as pd
import numpy as np

f1 = 112
b1 = 207
t = f1 + b1
#number of nodes

# start and end setting
s = int(input("Enter the start node number >> "))
e = int(input("Enter the end node number >> "))

def tocon(x):
    #連続に直す。B1と1Fのみなのであとで訂正
    if 1000 < x:
        return x - 1001 + b1
    else:
        return x-1

def fromcon(x):
    if b1 <= x:
        return x - b1 + 1001
    else:
        return x + 1

s = tocon(s)


l = pd.read_csv(filepath_or_buffer="LinkList_sapporo.csv", encoding="utf_8", sep=",")
d = [math.inf] * t
visited = [False] * t
previous = [0] * t

#初期化
d[s] = 0
visited[s] = True


def S():
    return [x for x in range(t) if d[x] != math.inf]

def adjecent(w):
    global a
    global stop
    #create a list of adjecent vertices 
    a = l.values[(l["n1"] == w),2].tolist() + l.values[(l["n2"] == w),1].tolist()
    if len(a) == 0:
        stop = True
    else:
        stop = False
        for i in a:
            print("tocon(i) ",tocon(i))
            print("a ",a)
            if visited[tocon(i)] == True:
                a.remove(i)

def shortest():
    ind = []
    dis = []
    for i in range(t):
        if not visited[i]:
            ind.append(i)
            dis.append(d[i])
    return fromcon(ind[dis.index(min(dis))])

c = 0
adjecent(s)
stop = False

while len(S()) != 0:
    #本当はSの定義違う
    if c == 0:
        w = fromcon(s)
    else:
        w = shortest()
        visited[tocon(w)] = True
    #print(w)
    #w is an actual value now
    if w == e or visited[tocon(e)]:
        print("cost = ", d[tocon(e)])
        path = []
        i = tocon(e)
        
        while i != s:
            i = previous[i]
            path.append(fromcon(i))
        path.reverse()
        print("path : ", path)
        #探索終了
        break

    else:
        adjecent(w)
        #print(visited)
        if stop:
            visited[tocon(w)] = True
            a1 = l.values[(l["n1"] == w),2].tolist() + l.values[(l["n2"] == w),1].tolist()
            for i in a1:
                distance = l[((l["n1"] == w) & (l["n2"] == i))].index.tolist() + l[((l["n1"] == i) & (l["n2"] == w))].index.tolist()
                new_dist = int(d[tocon(w)]) + l.values[distance[0],3]
                #w is continuous now
                j = tocon(i)
                if d[j]  > new_dist:
                    d[j] = new_dist
                    previous[w] = j
        else:
            for i in a:
                print("w", w)
                print("i", i)
                distance = l[((l["n1"] == w) & (l["n2"] == i))].index.tolist() + l[((l["n1"] == i) & (l["n2"] == w))].index.tolist()
                print(distance)
                w = tocon(w)
                #w is continuous now
                if d[w] == math.inf:
                    new_dist = l.values[distance[0],3]
                else:
                    new_dist = int(d[w]) + l.values[distance[0],3]
                j = tocon(i)
                if d[j] > new_dist:
                    d[j] = new_dist
                    previous[j] = w
                w = fromcon(w)
    
    c += 1
    if c >= 491:
        print("faile")
        break