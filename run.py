# python C:\wamp64\www\apps\lilpostloo\Challenge374\run.py


#gets grid of 0's in Array form
def gridArray(w,h):
    grid = [0]*h
    for y in range(0,h):
        grid[y] = [0]*w
    return grid

#converts grid array into display output
def drawGrid(grid):
    out = '\n'
    for y in grid:
        for x in y:
            out += str(x)+' '
        out+= '\n'
    return out 

def fillColumn(grid,col): 
    for i,row in enumerate(grid):
        grid[i][col] = 1
    return grid 

#checks for full rows and cols and fills grid accordingly
def checkForWholeLines(grid,width,height,columns,rows):
    for i,x in enumerate(columns):
        if len(x)==1 and int(x[0]) == int(height):
            grid = fillColumn(grid,i)
            columns[i] = [0]

    for i,x in enumerate(rows):
        if len(x)==1 and int(x[0]) == int(width):
            grid[i] = [1]*width
            rows[i] = [0]

    return grid,columns,rows

 
def deduce(grid,columns,rows):
    for i,col in enumerate(columns):
        colSegsCount = len(col)
        #print(colSegs) 
        for j, colSegValue in enumerate(col):
            #print(colSegValue)
            grid,rows = substractFromRow(grid,rows,colSegValue,i,j)
    return grid








def run(inputs):
    width, height, columns, rows = inputs.split("\n")
    width, height = int(width), int(height)
    columns = [[int(y) for y in x.split(",")] for x in columns[1:-1].split('","')]
    rows = [[int(y) for y in x.split(",")] for x in rows[1:-1].split('","')]
    grid = gridArray(width,height)
    #grid,columns,rows = checkForWholeLines(grid,width,height,columns,rows)
    grid = deduce(grid,columns,rows)
    return drawGrid(grid)
    #return 'done'


print(run('''5
5
"5","2,2","1,1","2,2","5"
"5","2,2","1,1","2,2","5"'''))

print(run('''8
11
"0","9","9","2,2","2,2","4","4","0"
"0","4","6","2,2","2,2","6","4","2","2","2","0"'''))
'''

 ****   
 ****** 
 **  ** 
 **  ** 
 ****** 
 ****   
 **     
 **     
 **   
"0","9","9","2,2","2,2","4","4","0"
"0","4","6","2,2","2,2","6","4","2","2","2","0"

"0","0","9","2,2","2,2","4","4","0"
"0","3","5","1,2","1,2","5","3","1","1","1","0"

"0","0","0","2,2","2,2","4","4","0"
"0","2","4","0,2","0,2","4","2","0","0","0","0"

"0","0","0","0,0","2,2","4","4","0"
"0","1","3","0,2","0,2","3","1","0","0","0","0"

"0","0","0","0,0","0,0","4","4","0"
"0","0","2","0,2","0,2","2","0","0","0","0","0"


loop each columns
    if whole number then
        find matching count in rows
            deduct 1 from each matching row
    if split, find pattern match
        deduct 1 from each row



'''