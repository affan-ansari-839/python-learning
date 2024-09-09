# -*- coding: utf-8 -*-

p = [(7,13),(4,11),(9,10),(12,12),(14,10),(7,7),(11,5),(15,7),(2,5),(4,4),(13,3),(5,1)]
n = len(p)

    
def maxima(n, p):
    for i in range(n):
        maximal=True
        for j in range(n):
            if (i!=j) and (p[i][0]<=p[j][0]) and (p[i][1]<=p[j][1]):
                maximal=False
                break
        if maximal:
            return p[i]
                    
maxima(n, p)         