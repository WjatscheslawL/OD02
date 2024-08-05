class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))
