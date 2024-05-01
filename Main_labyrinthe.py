import random

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
                        row += "---"
                else:
                    row += "+++"
            print(row)

g=Graph(10,15)
for i in range(g.L):
  for j in range(g.C):
    g.ajouterNoeud((i, j))



g.ajouterArc((0,0),(0,1),True)
g.ajouterArc((0,0),(1,0),True)
g.ajouterArc((1,0),(1,1),False)
g.ajouterArc((1,0),(2,0),True)
g.ajouterArc((2,0),(2,1),True)
g.ajouterArc((2,0),(3,0),False)
g.ajouterArc((3,0),(3,1),False)
g.ajouterArc((3,0),(4,0),True)
g.ajouterArc((4,0),(4,1),True)
g.ajouterArc((4,0),(5,0),True)
g.ajouterArc((5,0),(5,1),False)
g.ajouterArc((5,0),(6,0),True)
g.ajouterArc((6,0),(6,1),False)
g.ajouterArc((6,0),(7,0),True)
g.ajouterArc((7,0),(7,1),True)
g.ajouterArc((7,0),(8,0),False)
g.ajouterArc((8,0),(8,1),False)
g.ajouterArc((8,0),(9,0),True)
g.ajouterArc((9,0),(9,1),True)
########################
g.ajouterArc((0,1),(0,2),True)
g.ajouterArc((0,1),(1,1),False)
g.ajouterArc((1,1),(1,2),True)
g.ajouterArc((1,1),(2,1),True)
g.ajouterArc((2,1),(2,2),False)
g.ajouterArc((2,1),(3,1),True)
g.ajouterArc((3,1),(3,2),False)
g.ajouterArc((3,1),(4,1),True)
g.ajouterArc((4,1),(4,2),False)
g.ajouterArc((4,1),(5,1),False)
g.ajouterArc((5,1),(5,2),True)
g.ajouterArc((5,1),(6,1),True)
g.ajouterArc((6,1),(6,2),True)
g.ajouterArc((6,1),(7,1),False)
g.ajouterArc((7,1),(7,2),True)
g.ajouterArc((7,1),(8,1),False)
g.ajouterArc((8,1),(8,2),True)
g.ajouterArc((8,1),(9,1),True)
g.ajouterArc((9,1),(9,2),False)
##########
g.ajouterArc((0,2),(0,3),True)
g.ajouterArc((0,2),(1,2),False)
g.ajouterArc((1,2),(1,3),False)
g.ajouterArc((1,2),(2,2),False)
g.ajouterArc((2,2),(2,3),True)
g.ajouterArc((2,2),(3,2),True)
g.ajouterArc((3,2),(3,3),False)
g.ajouterArc((3,2),(4,2),True)
g.ajouterArc((4,2),(4,3),False)
g.ajouterArc((4,2),(5,2),True)
g.ajouterArc((5,2),(5,3),False)
g.ajouterArc((5,2),(6,2),False)
g.ajouterArc((6,2),(6,3),True)
g.ajouterArc((6,2),(7,2),False)
g.ajouterArc((7,2),(7,3),True)
g.ajouterArc((7,2),(8,2),False)
g.ajouterArc((8,2),(8,3),False)
g.ajouterArc((8,2),(9,2),True)
g.ajouterArc((9,2),(9,3),True)
#####
#####
g.ajouterArc((0,3),(0,4),True)
g.ajouterArc((0,3),(1,3),False)
g.ajouterArc((1,3),(1,4),True)
g.ajouterArc((1,3),(2,3),True)
g.ajouterArc((2,3),(2,4),False)
g.ajouterArc((2,3),(3,3),False)
g.ajouterArc((3,3),(3,4),True)
g.ajouterArc((3,3),(4,3),False)
g.ajouterArc((4,3),(4,4),True)
g.ajouterArc((4,3),(5,3),True)
g.ajouterArc((5,3),(5,4),False)
g.ajouterArc((5,3),(6,3),True)
g.ajouterArc((6,3),(6,4),False)
g.ajouterArc((6,3),(7,3),False)
g.ajouterArc((7,3),(7,4),True)
g.ajouterArc((7,3),(8,3),False)
g.ajouterArc((8,3),(8,4),True)
g.ajouterArc((8,3),(9,3),True)
g.ajouterArc((9,3),(9,4),True)
######
g.ajouterArc((0,4),(0,5),True)
g.ajouterArc((0,4),(1,4),False)
g.ajouterArc((1,4),(1,5),True)
g.ajouterArc((1,4),(2,4),False)
g.ajouterArc((2,4),(2,5),True)
g.ajouterArc((2,4),(3,4),True)
g.ajouterArc((3,4),(3,5),False)
g.ajouterArc((3,4),(4,4),False)
g.ajouterArc((4,4),(4,5),True)
g.ajouterArc((4,4),(5,4),False)
g.ajouterArc((5,4),(5,5),True)
g.ajouterArc((5,4),(6,4),False)
g.ajouterArc((6,4),(6,5),True)
g.ajouterArc((6,4),(7,4),True)
g.ajouterArc((7,4),(7,5),False)
g.ajouterArc((7,4),(8,4),True)
g.ajouterArc((8,4),(8,5),False)
g.ajouterArc((8,4),(9,4),False)
g.ajouterArc((9,4),(9,5),False)
##hhere
g.ajouterArc((0,5),(0,6),False)
g.ajouterArc((0,5),(1,5),True)
g.ajouterArc((1,5),(1,6),False)
g.ajouterArc((1,5),(2,5),True)
g.ajouterArc((2,5),(2,6),False)
g.ajouterArc((2,5),(3,5),False)
g.ajouterArc((3,5),(3,6),True)
g.ajouterArc((3,5),(4,5),True)
g.ajouterArc((4,5),(4,6),False)
g.ajouterArc((4,5),(5,5),False)
g.ajouterArc((5,5),(5,6),True)
g.ajouterArc((5,5),(6,5),True)
g.ajouterArc((6,5),(6,6),False)
g.ajouterArc((6,5),(7,5),True)
g.ajouterArc((7,5),(7,6),False)
g.ajouterArc((7,5),(8,5),False)
g.ajouterArc((8,5),(8,6),True)
g.ajouterArc((8,5),(9,5),True)
g.ajouterArc((9,5),(9,6),False)
##
g.ajouterArc((0,6),(0,7),True)
g.ajouterArc((0,6),(1,6),True)
g.ajouterArc((1,6),(1,7),False)
g.ajouterArc((1,6),(2,6),True)
g.ajouterArc((2,6),(2,7),True)
g.ajouterArc((2,6),(3,6),False)
g.ajouterArc((3,6),(3,7),True)
g.ajouterArc((3,6),(4,6),False)
g.ajouterArc((4,6),(4,7),True)
g.ajouterArc((4,6),(5,6),True)
g.ajouterArc((5,6),(5,7),False)
g.ajouterArc((5,6),(6,6),False)
g.ajouterArc((6,6),(6,7),True)
g.ajouterArc((6,6),(7,6),False)
g.ajouterArc((7,6),(7,7),True)
g.ajouterArc((7,6),(8,6),True)
g.ajouterArc((8,6),(8,7),False)
g.ajouterArc((8,6),(9,6),False)
g.ajouterArc((9,6),(9,7),True)
########################"########################"""
g.ajouterArc((0,7),(0,8),True)
g.ajouterArc((0,7),(1,7),True)
g.ajouterArc((1,7),(1,8),True)
g.ajouterArc((1,7),(2,7),False)
g.ajouterArc((2,7),(2,8),False)
g.ajouterArc((2,7),(3,7),True)
g.ajouterArc((3,7),(3,8),True)
g.ajouterArc((3,7),(4,7),False)
g.ajouterArc((4,7),(4,8),False)
g.ajouterArc((4,7),(5,7),True)
g.ajouterArc((5,7),(5,8),False)
g.ajouterArc((5,7),(6,7),True)
g.ajouterArc((6,7),(6,8),True)
g.ajouterArc((6,7),(7,7),False)
g.ajouterArc((7,7),(7,8),False)
g.ajouterArc((7,7),(8,7),True)
g.ajouterArc((8,7),(8,8),False)
g.ajouterArc((8,7),(9,7),True)
g.ajouterArc((9,7),(9,8),True)
##################################################
g.ajouterArc((0,8),(0,9),True)
g.ajouterArc((0,8),(1,8),False)
g.ajouterArc((1,8),(1,9),True)
g.ajouterArc((1,8),(2,8),False)
g.ajouterArc((2,8),(2,9),False)
g.ajouterArc((2,8),(3,8),True)
g.ajouterArc((3,8),(3,9),True)
g.ajouterArc((3,8),(4,8),False)
g.ajouterArc((4,8),(4,9),True)
g.ajouterArc((4,8),(5,8),True)
g.ajouterArc((5,8),(5,9),True)
g.ajouterArc((5,8),(6,8),False)
g.ajouterArc((6,8),(6,9),False)
g.ajouterArc((6,8),(7,8),True)
g.ajouterArc((7,8),(7,9),True)
g.ajouterArc((7,8),(8,8),True)
g.ajouterArc((8,8),(8,9),False)
g.ajouterArc((8,8),(9,8),False)
g.ajouterArc((9,8),(9,9),True)
#############################################
g.ajouterArc((0,9),(0,10),True)
g.ajouterArc((0,9),(1,9),False)
g.ajouterArc((1,9),(1,10),False)
g.ajouterArc((1,9),(2,9),True)
g.ajouterArc((2,9),(2,10),True)
g.ajouterArc((2,9),(3,9),False)
g.ajouterArc((3,9),(3,10),True)
g.ajouterArc((3,9),(4,9),False)
g.ajouterArc((4,9),(4,10),False)
g.ajouterArc((4,9),(5,9),True)
g.ajouterArc((5,9),(5,10),False)
g.ajouterArc((5,9),(6,9),True)
g.ajouterArc((6,9),(6,10),True)
g.ajouterArc((6,9),(7,9),False)
g.ajouterArc((7,9),(7,10),False)
g.ajouterArc((7,9),(8,9),False)
g.ajouterArc((8,9),(8,10),True)
g.ajouterArc((8,9),(9,9),True)
g.ajouterArc((9,9),(9,10),False)
##hereeeeeeeeeeeeeeee
g.ajouterArc((0,10),(0,11),True)
g.ajouterArc((0,10),(1,10),False)
g.ajouterArc((1,10),(1,11),True)
g.ajouterArc((1,10),(2,10),False)
g.ajouterArc((2,10),(2,11),True)
g.ajouterArc((2,10),(3,10),False)
g.ajouterArc((3,10),(3,11),True)
g.ajouterArc((3,10),(4,10),False)
g.ajouterArc((4,10),(4,11),True)
g.ajouterArc((4,10),(5,10),False)
g.ajouterArc((5,10),(5,11),True)
g.ajouterArc((5,10),(6,10),False)
g.ajouterArc((6,10),(6,11),False)
g.ajouterArc((6,10),(7,10),True)
g.ajouterArc((7,10),(7,11),False)
g.ajouterArc((7,10),(8,10),True)
g.ajouterArc((8,10),(8,11),False)
g.ajouterArc((8,10),(9,10),False)
g.ajouterArc((9,10),(9,11),True)
##hereeeeeeeeeeeeee
g.ajouterArc((0,11),(0,12),False)
g.ajouterArc((0,11),(1,11),True)
g.ajouterArc((1,11),(1,12),False)
g.ajouterArc((1,11),(2,11),False)
g.ajouterArc((2,11),(2,12),True)
g.ajouterArc((2,11),(3,11),False)
g.ajouterArc((3,11),(3,12),False)
g.ajouterArc((3,11),(4,11),False)
g.ajouterArc((4,11),(4,12),True)
g.ajouterArc((4,11),(5,11),False)
g.ajouterArc((5,11),(5,12),True)
g.ajouterArc((5,11),(6,11),True)
g.ajouterArc((6,11),(6,12),False)
g.ajouterArc((6,11),(7,11),True)
g.ajouterArc((7,11),(7,12),True)
g.ajouterArc((7,11),(8,11),True)
g.ajouterArc((8,11),(8,12),False)
g.ajouterArc((8,11),(9,11),True)
g.ajouterArc((9,11),(9,12),True)
##### here -1
g.ajouterArc((0,12),(0,13),True)
g.ajouterArc((0,12),(1,12),True)
g.ajouterArc((1,12),(1,13),True)
g.ajouterArc((1,12),(2,12),False)
g.ajouterArc((2,12),(2,13),True)
g.ajouterArc((2,12),(3,12),False)
g.ajouterArc((3,12),(3,13),True)
g.ajouterArc((3,12),(4,12),True)
g.ajouterArc((4,12),(4,13),False)
g.ajouterArc((4,12),(5,12),False)
g.ajouterArc((5,12),(5,13),False)
g.ajouterArc((5,12),(6,12),True)
g.ajouterArc((6,12),(6,13),False)
g.ajouterArc((6,12),(7,12),False)
g.ajouterArc((7,12),(7,13),False)
g.ajouterArc((7,12),(8,12),True)
g.ajouterArc((8,12),(8,13),True)
g.ajouterArc((8,12),(9,12),False)
g.ajouterArc((9,12),(9,13),True)
##Done
g.ajouterArc((0,13),(0,14),True)
g.ajouterArc((0,13),(1,13),False)
g.ajouterArc((1,13),(1,14),False)
g.ajouterArc((1,13),(2,13),True)
g.ajouterArc((2,13),(2,14),False)
g.ajouterArc((2,13),(3,13),False)
g.ajouterArc((3,13),(3,14),True)
g.ajouterArc((3,13),(4,13),False)
g.ajouterArc((4,13),(4,14),True)
g.ajouterArc((4,13),(5,13),True)
g.ajouterArc((5,13),(5,14),True)
g.ajouterArc((5,13),(6,13),False)
g.ajouterArc((6,13),(6,14),True)
g.ajouterArc((6,13),(7,13),True)
g.ajouterArc((7,13),(7,14),True)
g.ajouterArc((7,13),(8,13),False)
g.ajouterArc((8,13),(8,14),True)
g.ajouterArc((8,13),(9,13),False)
g.ajouterArc((9,13),(9,14),True)
##done
g.ajouterArc((0,14),(1,14),True)
g.ajouterArc((1,14),(2,14),True)
g.ajouterArc((2,14),(3,14),True)
g.ajouterArc((3,14),(4,14),True)
g.ajouterArc((4,14),(5,14),False)
g.ajouterArc((5,14),(6,14),True)
g.ajouterArc((6,14),(7,14),False)
g.ajouterArc((7,14),(8,14),True)
g.ajouterArc((8,14),(9,14),False)
g.AfficherLabyrinthe()

from collections import deque


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
                    
   



s1 = SearchLabyrinthe(g, 10, 15)
solution1 = s1.dfs((0, 0), (9, 14))
print(solution1)

s2 = SearchLabyrinthe(g, 10, 15)
solution2 = s2.bfs((0, 0), (9, 14))
print(solution2)


s3 = SearchLabyrinthe(g, 10, 15)
solution3 = s3.dfs_limited((0, 0), (9, 14), 115)
print(solution3)



def generate_maze(width, height):
    maze = [['#'] * (width * 2 + 1) for _ in range(height * 2 + 1)]

    def add_wall(x, y):
        if 0 < x < width * 2 and 0 < y < height * 2:
            walls.append((x, y))

    def mark_cell(x, y):
        maze[y][x] = ' '
        add_wall(x - 1, y)
        add_wall(x + 1, y)
        add_wall(x, y - 1)
        add_wall(x, y + 1)

    start_x, start_y = random.randrange(width) * 2, random.randrange(height) * 2
    mark_cell(start_x, start_y)
    walls = []
    add_wall(start_x - 1, start_y)
    add_wall(start_x + 1, start_y)
    add_wall(start_x, start_y - 1)
    add_wall(start_x, start_y + 1)

    while walls:
        wall_x, wall_y = random.choice(walls)
        walls.remove((wall_x, wall_y))

        opposite_x, opposite_y = wall_x, wall_y
        if wall_x % 2 == 0:
            opposite_y += -1 if maze[wall_y - 1][wall_x] == '#' else 1
        else:
            opposite_x += -1 if maze[wall_y][wall_x - 1] == '#' else 1

        if maze[opposite_y][opposite_x] == '#':
            maze[wall_y][wall_x] = maze[opposite_y][opposite_x] = ' '
            mark_cell(opposite_x, opposite_y)

    return maze

def create_graph_from_maze(maze):
    graph = Graph(len(maze), len(maze[0]))

    def add_edge(x1, y1, x2, y2):
        graph.ajouterArc((x1, y1), (x2, y2), 1)

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == ' ':
                if x > 0 and maze[y][x - 1] == ' ':
                    add_edge(x, y, x - 1, y)
                if x < len(row) - 1 and maze[y][x + 1] == ' ':
                    add_edge(x, y, x + 1, y)
                if y > 0 and maze[y - 1][x] == ' ':
                    add_edge(x, y, x, y - 1)
                if y < len(maze) - 1 and maze[y + 1][x] == ' ':
                    add_edge(x, y, x, y + 1)

    return graph



