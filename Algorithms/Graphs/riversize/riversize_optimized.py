def riverSizes(matrix):
    columns = len(matrix)
    rows = len(matrix[0])

    river_size = []

    for i in range(rows):
        for j in range(columns):
            size = DFS(matrix,i,j)
            #if the size is greater than zero then add it
            if size > 0:
                river_size.append(size)
    
    print(matrix)
    return river_size

def DFS(matrix, row, column) -> int:
    size = 0  
    #print(f'{column}:{row}')
    #we only want execute if the column and row are under the bounds of the matrix
    if(column > -1 and row > -1 and column < len(matrix) and row < len(matrix[0])):
        
        #print('#')
         #if the value print(row)
        if matrix[column][row] <= 0:
            return 0

        #increase the size if the node has value equal to 1
        if matrix[column][row] == 1:
            size =+ 1
       
        #mark this node as visited
        matrix[column][row] = -1

        #iterate through the sides of each node, top, bottom, left, rigth
        sides = [(column, row + 1),(column, row - 1),(column + 1, row),(column - 1, row)]
        for side in sides:
            size += DFS(matrix, side[1], side[0])
    
    return size

#declare a matrix of m * n size
m = [
  [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
  [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]

print(riverSizes(m))