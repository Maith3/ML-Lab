import heapq

class Node:
  def __init__(self, name, g, h,parent=None):
    self.name = name
    self.g = g
    self.h = h
    self.f = g+h
    self.parent = parent
    
  def __lt__(self,other):
    return self.f<other.f

def astar(graph,start,goal,heuristics):
  open_list=[]
  closed_list=set()
  
  heapq.heappush(open_list,Node(start,0,heuristics[start]))
  
  while open_list:
    current_node = heapq.heappop(open_list)
    
    if current_node.name==goal:
      path=[]
      while current_node:
        path.append(current_node.name)
        current_node=current_node.parent
      return path[::-1]
    
    if current_node.name in closed_list:
      continue
    
    closed_list.add(current_node.name)
    
    for neighbor,cost in graph.get(current_node.name,[]):
      if neighbor not in closed_list:
        g = current_node.g+cost
        heapq.heappush(open_list,Node(neighbor,g,heuristics[neighbor],current_node))
  return None

def get_input():
  graph={}
  heuristics={}
  
  n = int(input("Enter the number of nodes: "))
  
  for i in range(n):
    node = input("Enter the node name: ")
    neighbors = input("Enter the neighbor node along with the cost (Ex, B 1, C 2): ")
    neighbors.strip()
    graph[node]=[]
    
    if neighbors:
      for item in neighbors.split(","):
        neighbor,cost = item.strip().split()
        graph[node].append((neighbor,int(cost)))
  for i in range(n):
    node = input("Enter the node name: ")
    h=int(input("Enter the heuristic value: "))
    heuristics[node]=h
  start = input("Enter the start node: ")
  goal = input("Enter the goal node: ")
  
  path = astar(graph,start,goal,heuristics)
  
  if path:
    print(f"The path from {start} to {goal}: ",path)
  else:
    print(f"No path exists from {start} to {goal}")
get_input()