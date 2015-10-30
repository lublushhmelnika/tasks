from math import sqrt

class Point:
    radius = 0    
    def __init__(self, x, y):
      self.neighbour = []
      self.x = x
      self.y = y
    def __eq__(self, other):
      return (self.x==other.x) and (self.y==other.y)

points_arr = []

with open('points.txt') as points:
    for idx, point in enumerate(points):
        point = point.split()
        point = [int(i) for i in point]
        points_arr.append(Point(point[0], point[1]))

N = len(points_arr)

for j in points_arr:
    if (points_arr.count(j)!=1):
        points_arr.remove(j)
        N=N-1
 
for i in xrange(0,N):
    if (i==0):
        min=sqrt((points_arr[0].x-points_arr[N-1].x)**2+(points_arr[0].y-points_arr[N-1].y)**2)
    else:
        min=sqrt((points_arr[i].x-points_arr[0].x)**2+(points_arr[i].y-points_arr[0].y)**2)    
    for j in xrange(0,N):
        if (j!=i):
            distant=sqrt((points_arr[i].x-points_arr[j].x)**2+(points_arr[i].y-points_arr[j].y)**2)
            if (distant<min):
                min=distant
        points_arr[i].radius=min
        
for i in xrange(0,N):
    for j in xrange(0,N):
        if (j!=i):
            distant=(sqrt((points_arr[i].x-points_arr[j].x)**2+(points_arr[i].y-points_arr[j].y)**2))/2
            if (distant<=points_arr[i].radius):               
              points_arr[i].neighbour.append(j)
              
for i in xrange (0,N):
    print ('Point number',i+1)
    print(points_arr[i].x,points_arr[i].y)
    print("Radius=",points_arr[i].radius)
    print('Neighbours:')
    for j in points_arr[i].neighbour:
        print(points_arr[j].x,points_arr[j].y)
    print ('\n')
