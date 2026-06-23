def minimax(depth, node_index, is_maximizing,scores, max_depth):
  if max_depth==depth:
    return scores[node_index]
  if is_maximizing:
    return max(minimax(depth+1,node_index*2,False,scores, max_depth),minimax(depth+1,node_index*2+1,False,scores,max_depth))
  else:
    return min(minimax(depth+1,node_index*2,True,scores, max_depth),minimax(depth+1,node_index*2+1,True,scores,max_depth))

def alpha_beta(depth, node_index, is_maximizing, scores, max_depth, alpha, beta):
  if depth==max_depth:
    return scores[node_index]
  
  if is_maximizing:
    max_eval = float('-inf')
    for i in range(2):
      eval = alpha_beta(depth+1,node_index*2+i,False,scores,max_depth,alpha,beta)
      max_eval=max(max_eval,eval)
      alpha = max(alpha,max_eval)
      if beta<=alpha:
        break
    return max_eval
  else:
    min_eval = float('inf')
    for i in range(2):
      eval = alpha_beta(depth+1,node_index*2+i,True,scores,max_depth,alpha,beta)
      min_eval = min(min_eval,eval)
      beta = min(beta,min_eval)
      if beta<=alpha:
        break
    return min_eval

def get_input():
  max_depth = int(input("Enter the tree depth: "))
  num_leaves = 2**max_depth
  scores = input("Enter the scores for each of the node (comma separated): ")
  scores = list(map(int, scores.strip().split(",")))
  if (num_leaves!=len(scores)):
    print("Invalid Input")
    return
  optimal_value_minmax = minimax(0,0,True,scores,max_depth)
  optimal_value_ab = alpha_beta(0,0,True,scores,max_depth,float('-inf'),float('inf'))
  
  print(f"Optimal value for minimax algorithm: {optimal_value_minmax}")
  print(f"Optimal value for alpha beta algorithm: {optimal_value_ab}")

get_input()