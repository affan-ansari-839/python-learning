def plane_sweep(n, p):
    p.sort(key=lambda point: point[0])
    s = []
    for i in range(n):
        while (s != [] and s[-1][1]<=p[i][1]):
            s.pop()
        s.append(p[i])
        
    return s    
p = [(3,13),(12,12),(4,11),(9,10),(14,10),(15,7),(7,7),(2,5),(10,5),(13,3),(5,1)]
n = len(p)

s = plane_sweep(n, p)

print(s)