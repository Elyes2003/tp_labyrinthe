class Graph:
  def __init__(self,L,C):
      self.graph = {} #ou self.graph = dict()
      self.L= L
      self.C= C

  def ajouterNoeud(self, node):
      if node not in self.graph:
          self.graph[node] = []

  def ajouterArc(self, node1, node2,p):
      if node1 in self.graph.keys() and node2 in self.graph.keys():
          self.graph[node1].append((node2,p))
          self.graph[node2].append((node1,p))
      else:
        print("One or both nodes does not belong to the graph")

  def listerNoeuds(self):
      return list(self.graph.keys())

  # liste de toutes les arrêtes du graphe
  def listerArcs(self):
      edges = []
      for node,arcs in self.graph:
              edges.append(arcs)
      return edges

  # liste des arrêtes dont node est une extrémité
  def listerArcs(self, node):
      if node in self.graph:
        return self.graph.get(node,[])

  def adjacenceNoeud(self, node1, node2):
      return (node1,_) in self.graph[node2]

  def AfficherGraphe(self):
      for node in self.graph:
          print(f"{node} -> {self.graph[node]}")


  def AfficherLabyrinthe(self):
    for i in range(self.L):
        row = ""
        for j in range(self.C):
            if (i, j) in self.graph:
                if not self.graph[(i, j)]:
                    row += "+++"
                else:
                    row += "  "
            else:
                row += "+++"
        print(row)
g = Graph(5, 5)
for i in range(g.L):
    for j in range(g.C):
        g.ajouterNoeud((i, j))

g.ajouterArc((0, 0), (0, 1), True)
g.ajouterArc((0, 1), (0, 2), True)
g.ajouterArc((0, 2), (0, 3), True)
g.ajouterArc((0, 3), (0, 4), True)
g.ajouterArc((1, 0), (1, 1), True)
g.ajouterArc((1, 1), (1, 2), True)
g.ajouterArc((1, 2), (1, 3), True)
g.ajouterArc((1, 3), (1, 4), True)
g.ajouterArc((2, 0), (2, 1), True)
g.ajouterArc((2, 1), (2, 2), True)
g.ajouterArc((2, 2), (2, 3), True)
g.ajouterArc((2, 3), (2, 4), True)
g.ajouterArc((3, 0), (3, 1), True)
g.ajouterArc((3, 1), (3, 2), True)
g.ajouterArc((3, 2), (3, 3), True)
g.ajouterArc((3, 3), (3, 4), True)
g.ajouterArc((4, 0), (4, 1), True)
g.ajouterArc((4, 1), (4, 2), True)
g.ajouterArc((4, 2), (4, 3), True)
g.ajouterArc((4, 3), (4, 4), True)

g.ajouterArc((0, 0), (1, 0), True)
g.ajouterArc((1, 0), (2, 0), True)
g.ajouterArc((2, 0), (3, 0), True)
g.ajouterArc((3, 0), (4, 0), True)
g.ajouterArc((0, 1), (1, 1), True)
g.ajouterArc((1, 1), (2, 1), True)
g.ajouterArc((2, 1), (3, 1), True)
g.ajouterArc((3, 1), (4, 1), True)
g.ajouterArc((0, 2), (1, 2), True)
g.ajouterArc((1, 2), (2, 2), True)
g.ajouterArc((2, 2), (3, 2), True)
g.ajouterArc((3, 2), (4, 2), True)
g.ajouterArc((0, 3), (1, 3), True)
g.ajouterArc((1, 3), (2, 3), True)
g.ajouterArc((2, 3), (3, 3), True)
g.ajouterArc((3, 3), (4, 3), True)
g.ajouterArc((0, 4), (1, 4), True)
g.ajouterArc((1, 4), (2, 4), True)
g.ajouterArc((2, 4), (3, 4), True)
g.ajouterArc((3, 4), (4, 4), True)

g.ajouterArc((0, 0), (0, 1), False)
g.ajouterArc((0, 1), (0, 2), False)
g.ajouterArc((0, 2), (0, 3), False)
g.ajouterArc((0, 3), (0, 4), False)
g.ajouterArc((1, 0), (1, 1), False)
g.ajouterArc((1, 1), (1, 2), False)
g.ajouterArc((1, 2), (1, 3), False)
g.ajouterArc((1, 3), (1, 4), False)
g.ajouterArc((2, 0), (2, 1), False)
g.ajouterArc((2, 1), (2, 2), False)
g.ajouterArc((2, 2), (2, 3), False)
g.ajouterArc((2, 3), (2, 4), False)
g.ajouterArc((3, 0), (3, 1), False)
g.ajouterArc((3, 1), (3, 2), False)
g.ajouterArc((3, 2), (3, 3), False)
g.ajouterArc((3, 3), (3, 4), False)
g.ajouterArc((4, 0), (4, 1), False)
g.ajouterArc((4, 1), (4, 2), False)
g.ajouterArc((4, 2), (4, 3), False)
g.ajouterArc((4, 3), (4, 4), False)

g.ajouterArc((0, 0), (1, 0), False)
g.ajouterArc((1, 0), (2, 0), False)
g.ajouterArc((2, 0), (3, 0), False)
g.ajouterArc((3, 0), (4, 0), False)
g.ajouterArc((0, 1), (1, 1), False)
g.ajouterArc((1, 1), (2, 1), False)
g.ajouterArc((2, 1), (3, 1), False)
g.ajouterArc((3, 1), (4, 1), False)
g.ajouterArc((0, 2), (1, 2), False)
g.ajouterArc((1, 2), (2, 2), False)
g.ajouterArc((2, 2), (3, 2), False)
g.ajouterArc((3, 2), (4, 2), False)
g.ajouterArc((0, 3), (1, 3), False)
g.ajouterArc((1, 3), (2, 3), False)
g.ajouterArc((2, 3), (3, 3), False)
g.ajouterArc((3, 3), (4, 3), False)
g.ajouterArc((0, 4), (1, 4), False)
g.ajouterArc((1, 4), (2, 4), False)
g.ajouterArc((2, 4), (3, 4), False)
g.ajouterArc((3, 4), (4, 4), False)
from collections import deque
import heapq

class Pile:
  def __init__(self):
    self.elements = deque()
  def pile_vide(self):
    return len(self.elements) == 0
  def empiler(self, element):
    self.elements.append(element)
  def depiler(self):
    if not self.pile_vide():
      return self.elements.pop()
    else:
      print("La pile est vide.")
  def taille_pile(self):
    return len(self.elements)

from collections import deque

class File:
  def __init__(self):
    self.elements = deque()
  def file_vide(self):
    return len(self.elements) == 0
  def enfiler(self, element):
    self.elements.append(element)
  def defiler(self):
    if not self.file_vide():
      return self.elements.popleft()
    else:
      print("La file est vide.")
  def taille_file(self):
    return len(self.elements)
    

class SearchLabyrinthe:
    def __init__(self,g,L,C):
        self.graph =g
        self.explored = {}
        self.accessible = {}

    def successeurs(self, current_state):
        return [x[0] for x in self.graph.listerArcs(current_state) if x[1]]

    def VerifEtat(self, state):
        return not (state in self.explored.keys()  or state in self.accessible.keys())

    def succValide(self, current_state):
        return [x[0] for x in self.graph.listerArcs(current_state) if x[1] and self.VerifEtat(x[0])]


    def dfs(self,etatinit,etatobj):
        pile1 = Pile()
        pile1.empiler(etatinit)
        pred = None
        
        while not (pile1.pile_vide()):
            x = pile1.depiler()
            if(x == etatobj):
                 return self.solutionOptimal(etatinit, etatobj)
            else:
                for s in self.succValide(x):
                    self.accessible[s] = x    
                    pile1.empiler(s)
                    self.explored[x] = pred
                    pred = x
  

    def dfs_limited(self, etatinit, etatobj, limit):
       
        pile1 = Pile()
        pile1.empiler(etatinit)
        pred = None
        exploredlimit = set()

        while not pile1.pile_vide():
            x = pile1.depiler()
            if x in exploredlimit:
                continue
            exploredlimit.add(x)
            if x == etatobj:
                return self.solutionOptimal(etatinit, etatobj)
            else:
                for s in self.succValide(x):
                    if s in exploredlimit:
                        continue
                    self.accessible[s] = x
                    pile1.empiler(s)
                    self.explored[x] = pred
                    pred = x
                    if len(exploredlimit) > limit:
                        return None
        return None

    def solutionOptimal(self, start, goal):
        path = []
        current = goal
        while current!= start:
            path.append(current)
            current = self.accessible[current]
        path.append(start)
        path.reverse()
        return path    
    
    def bfs(self, etatinit, etatobj):
        file1 = File()
        file1.enfiler(etatinit)
        pred = None

        while not file1.file_vide():
            x = file1.defiler()
            if x == etatobj:
                return self.solutionOptimal(etatinit, etatobj)
            else:
                for s in self.succValide(x):
                    self.accessible[s] = x
                    file1.enfiler(s)
                    self.explored[x] = pred
                    pred = x                
                    
   

g.AfficherLabyrinthe()
s = SearchLabyrinthe(g, 5, 5)
solution = s.dfs((0, 0), (4, 4))
print(solution)
s = SearchLabyrinthe(g, 5, 5)
solution = s.bfs((0, 0), (4, 4))
print(solution)
s = SearchLabyrinthe(g, 5, 5)
solution = s.dfs_limited((0, 0), (4, 4),15)
print(solution)