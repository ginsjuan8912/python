#This class represents a node
class Node:
    name = ''
    row:int = -1
    column:int = -1
    data:int = 0
    is_visited:bool = False

    adjacent_nodes = []

    def __init__(self, data, row, column) -> None:       
        self.data = data
        self.row = row
        self.column = column
        self.name = str(row)+str(column)

#This class represents a graph
class Graph:
    nodes = {}  
    river_sizes = []

    def _addNode(self,name:str, node: Node):
        self.nodes[name] = node
    
    def __init__(self, matrix) -> None:

        columns = len(matrix)
        rows = len(matrix[0])

        if(columns > 1 and rows > 1):
            for i in range (0,len(matrix),1):
                for j in range(0, len(matrix[0]), 1):
                    name = str(j)+str(i)
                    self._addNode(name, Node(matrix[i][j],j,i))
        elif(columns >= 1 and rows <= 1):
             for i in range (0,len(matrix),1):
                name = str(0)+str(i)
                self._addNode(name, Node(matrix[i][0],0,i))
        elif(columns <= 1 and rows >= 1):
             for i in range (0,len(matrix[0]),1):
                name = str(i)+str(0)
                self._addNode(name, Node(matrix[0][i],i,0))

        self.get_adjacent_nodes()
    
    def get_adjacent_nodes(self):
        for node in self.nodes.values():

            if(node.data == 0):
                continue
            
            closer_nodes = []
            #add top
            top = str(node.row - 1) + str(node.column)
            if top in self.nodes:
                closer_nodes.append(self.nodes[top]) 
            #add rigth
            rigth = str(node.row) + str(node.column - 1)
            if rigth in self.nodes:
                 closer_nodes.append(self.nodes[rigth])
            #add left
            left = str(node.row) + str(node.column + 1)
            if left in self.nodes:
                 closer_nodes.append(self.nodes[left])
            #add bottom
            bottom = str(node.row + 1) + str(node.column)
            if bottom in self.nodes:
                 closer_nodes.append(self.nodes[bottom])
            
            node.adjacent_nodes = closer_nodes
      
    def DFS(self, root: Node) -> int:

        river_size = 0

        if root.is_visited:         
            return 0      
       
        if root.data == 1:
            river_size =+ 1       

        root.is_visited = True 
     
        for neighbour in root.adjacent_nodes:
            if(neighbour.data == 1): #Visit the node if has value
                river_size += self.DFS(neighbour)
        
     
        return river_size
    
    def visit(self):
        for node in self.nodes.values():          
           
            size = self.DFS(self.nodes[node.name])
            if(size > 0):  
                print(f'{node.name} : {size}')            
                self.river_sizes.append(size)
        
        self.river_sizes.sort()


def initialize_graph(matrix) -> Graph:
    graph = Graph(matrix) 
    graph.visit()
    return graph
    #for node in graph.nodes.values():
     #   print(node.name)

def riverSizes(matrix):

    if(len(matrix) <= 0):
        return []   

    if(len(matrix) == 1 and len(matrix[0]) == 1):
        if(matrix[0][0] == 1):
            return [1]
        else:
            return []   

    gp = initialize_graph(matrix)
    print(gp.river_sizes)
    return gp.river_sizes

#declare a matrix of m * n size
m =[
  [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
  [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]
riverSizes(m)