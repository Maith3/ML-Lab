import heapq

class Node:
  def __init__(self, name, heuristics,parent=None):
    self.name=name
    self.heuristics=heuristics
    self.parent=parent
  def __lt__(self,other):
    return self.heuristics<other.heuristics
  
  
def best_first_search(graph, start, heuristics, goal):
  open_list=[]
  closed_list=set()
  heapq.heappush(open_list,Node(start,heuristics[start]))
  
  while open_list:
    current_node = heapq.heappop(open_list)
    if current_node.name == goal:
      path=[]
      while current_node:
        path.append(current_node.name)
        current_node=current_node.parent
      return path[::-1]
    
    if current_node.name in closed_list:
      continue
    
    closed_list.add(current_node.name)
    
    for neighbor in graph.get(current_node.name,[]):
      if neighbor not in closed_list:
        heapq.heappush(open_list,Node(neighbor, heuristics[neighbor],current_node))
  return None

def get_input():
  graph={}
  heuristics={}
  
  n = int(input("Enter the number of nodes: "))
  for _ in range(n):
    node = input("Enter name of node: ")
    neighbors = input("Enter the neighbors in comma separated manner: ").strip()
    if neighbors:
      graph[node] = [neighbor.strip() for neighbor in neighbors.split(",")]
    else:
      graph[node]=[]
  print("\nEnter the heuristics: ")
  for _ in range(n):
    node = input("Enter the node to enter heuristics for: ")
    heuristics[node] = int(input("Enter the heuristic value: "))
    
  start = input("Enter the start node: ")
  goal = input("Enter the goal node: ")
  
  path = best_first_search(graph, start, heuristics, goal)
  
  if path:
    print(f"Path from {start} to {goal} = ", path)
  else:
    print(f"No path exists from {start} to {goal}")

get_input()