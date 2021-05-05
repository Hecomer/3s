import math
from operator import attrgetter

class Vertice:
    def __init__(self, name):
        self.name = name
        self.weight = math.inf
        self.status = True
        self.way = []


graphs = [[None, 10, 30, 50, 10],
          [None, None, None, None, None],
          [None, None, None, None, 10],
          [None, 40, 20, None, None],
          [10, None, 10, 30, None]]

ver_lst = []

for i in range(len(graphs)):
    a = Vertice(i)
    if i == 0:
        a.weight = 0
    ver_lst.append(a)

for j in range(len(ver_lst)):
    for k in range(len(ver_lst)):
        if j == k:
            continue
        else:
            if graphs[ver_lst[j].name][ver_lst[k].name] is None:
                continue
            elif ver_lst[k].weight > (graphs[ver_lst[j].name][ver_lst[k].name] + ver_lst[j].weight):
                ver_lst[k].weight = graphs[ver_lst[j].name][ver_lst[k].name] + ver_lst[j].weight
                a = ver_lst[j].way.copy()
                a.append(ver_lst[j].name)
                ver_lst[k].way = a
    ver_lst[j].status = False
    ver_lst = sorted(ver_lst, key=attrgetter('status', 'weight'))
    print(ver_lst[0].way)

ver_lst = sorted(ver_lst, key=attrgetter('name'))
for v in ver_lst:
    print(v.name, v.weight, v.way)