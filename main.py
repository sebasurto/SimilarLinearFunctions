import funtions as ft
a = [0,0]
b = [3,2]
c = [4,4]
d = [7,3]
m = ft.slope(a,d)
dist = ft.distance(a,b)
print (m,dist)
x =[a,b,c]
y =[a,b,c]
z =[a,c,d]
graphs = [x,y,z]
print (x,y)
print (ft.compareGraph(x,y))
lista_slope = ft.slopesGraph(x)
lista_dist = ft.distancesGraph(x)
lista_dist2 = ft.distancesGraph(y)
lista_propor = ft.proportionsGraph(x)
print (lista_slope,lista_dist, lista_dist2, lista_propor)
print (graphs)