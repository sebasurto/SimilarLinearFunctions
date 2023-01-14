def slope (initial,final):
  x = final [0]-initial[0]
  y = final [1]-initial[1]
  m = y/x 
  slope_var = round (m,5)
  return slope_var
  
def distance (initial, final):
  x = final [0]-initial[0]
  y = final [1]-initial[1]
  d = x**2 + y**2
  d = d**(1/2)
  distance_var = round (d,5)
  return distance_var
  
def slopesGraph (graph):
  slopes_list = []
  for i in range(len(graph)-1):
    slope_var_1 =slope(graph[i],graph[i+1])
    slopes_list.append (slope_var_1)
  return slopes_list

def distancesGraph (graph):
  distances_list = []
  for i in range(len(graph)-1):
    slope_var_1 =distance(graph[i],graph[i+1])
    distances_list.append (slope_var_1)
  return distances_list

def proportionsGraph (graph):
  x = distancesGraph(graph)
  proportion_List=[]
  for i in range (len(graph)-2):
    proportion = x[i]/x[i+1]
    proportion = round(proportion,5)
    proportion_List.append(proportion)
  return proportion_List

def compareGraph (graph_1,graph_2):
  slopes_1 = slopesGraph(graph_1)
  slopes_2 = slopesGraph(graph_2)
  proportion_1 =proportionsGraph(graph_1)
  proportion_2 = proportionsGraph(graph_2)
  if (slopes_1 != slopes_2):
    return False
  if (proportion_1 != proportion_2):
    return False
  return True
