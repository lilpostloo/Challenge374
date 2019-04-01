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



def substractFromRowOld(grid,rows,colSegValue,colNum,segNum):
    rowsClone = rows
    gridClone = grid
    minusCount = 0
    colSegMarker = 0
    colSegCounter = 0
    for l, row in enumerate(rowsClone):
        if sum(row) != 0:
            for j, rowSegValue in enumerate(row):
                if rowSegValue !=0:
                    colSegCounter += 1 if colSegMarker==0 else 0
                    colSegMarker = 1                    
                    rows[l][j] = rowSegValue-1
                    grid[l][colNum] = 1
                    minusCount+=1
        else:
            colSegMarker = 0

            if minusCount>0 and minusCount != colSegValue:
                rows = rowsClone
                grid = gridClone

            if minusCount==colSegValue and colSegCounter ==segNum+1:
                break

        #print(colSegCounter)

    #print(segNum+1,colSegCounter)
    return grid,rows

            #minus 1 from row or child of
            #add 1 to minus count
        #if sum row is 0
            #check if minus count == colSegValue
                #no then reset minus count and rows to rowsClone             



def getSegmentCount(arr):
    count = 0
    marker = 0
    for x in arr:
        if x == 1:
            count += 1 if marker==0 else 0
            marker=1
        else:
            marker=0
    return count if marker==1 else count+1




#clone a copy of rows
#loop through rows, minus one from each, while counting, if match colSeg number continue else reset using clone.]
#columns = "0","0","0","0,0","0,0","4","4","0"
#rows = "0","0","2","0,2","0,2","2","0","0","0","0","0"

def substractFromRow(grid,rows,colSegValue,colNum,colSegNum):
    rowsClone = rows
    gridClone = grid
    minusCount = 0
    colSegMarker = 0
    colSegCounter = 0
    rowSegMarker = 0
    rowSegCounter = 0 
    for l, row in enumerate(rowsClone):
        if sum(row) != 0:
            for j, rowSegValue in enumerate(row):
                if rowSegValue !=0:
                    colSegCounter += 1 if colSegMarker==0 else 0
                    colSegMarker = 1          
                    segCount = getSegmentCount(grid[l])
                    if segCount == j+1:
                        rows[l][j] = rowSegValue-1
                        grid[l][colNum] = 1
                        minusCount+=1
        else:
            colSegMarker = 0

            if minusCount>0 and minusCount != colSegValue:
                rows = rowsClone
                grid = gridClone

            if minusCount==colSegValue and colSegCounter ==colSegNum+1:
                break

        #print(colSegCounter)

    #print(segNum+1,colSegCounter)
    return grid,rows
            #minus 1 from row or child of
            #add 1 to minus count
        #if sum row is 0
            #check if minus count == colSegValue
                #no then reset minus count and rows to rowsClone    


#essentially we are deducing the cols from the rows by matching none-zero elements across the array e.g.:
#columns = "0","0","0","0,0","0,0","4","4","0"
#rows = "0","0","2","0,2","0,2","2","0","0","0","0","0"
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

* x * * * *
* x x * * *
* * * * * *
* * x * * *
* x x x * *
* x * * x *


  2 1 
0 2 2 1 1 0
* / / / / * 1
* / / / / * 2
* * * * * * 0
* / / / / * 1
* / / / / * 3
* / / / / * 1,1


  2 1 
0 2 2 1 1 0
* / * * * * 1
* / / * * * 2
* * * * * * 0
* / * * * * 1
* / / / * * 3
* / * / * * 1,1



    2 1 
  0 2 2 1 1 0
4 * * * * * * 1
2 * * * * * * 2
0 * * * * * * 0
4 * * * * * * 1
2 * * * * * * 3
3 * * * * * * 1,1
  0 3 4 5 5 0 


----------------------
     2 1 
   0 2 2 1 1 0

4  * 1 1 1 1 *  1
3  * 1 2 2 1 *  2
0  * * * * * *  0
4  * 1 1 1 1 *  1
2  * 1 2 2 1 *  3
3  * 2 1 1 2 *  1,1
   
   0 3 4 5 5 0 

--------------------------
     2 1 
   0 2 2 1 1 0

4  * 2 2 2 2 *  1
3  * 2 3 3 2 *  2
0  * * * * * *  0
4  * 2 2 2 2 *  1
2  * 3 3 3 2 *  3
3  * 3 2 2 3 *  1,1
   
   0 3 4 5 5 0 

--------------------------
     2 1 
   0 2 2 1 1 0

4  * 2 2 2 2 *  1
3  * 2 x x 2 *  2
0  * * * * * *  0
4  * 2 2 2 2 *  1
2  * x x x 2 *  3
3  * x 2 2 x *  1,1
   
   0 3 4 5 5 0 

--------------------------
     2 1 
   0 2 2 1 1 0

4  * X 0 0 2 *  1
3  * X x x 2 *  2
0  * * * * * *  0
4  * 0 2 0 2 *  1
2  * x x x 2 *  3
3  * x 2 0 x *  1,1
   
   0 3 4 5 5 0 
cancel acrosss
--------------------------
     2 1 
   0 2 2 1 1 0

4  * X 0 0 0 *  1
3  * X x x 0 *  2
0  * * * * * *  0
4  * 0 2 0 2 *  1
2  * x x x 0 *  3
3  * x 0 0 x *  1,1
   
   0 3 4 5 5 0

cancel down   
--------------------------
     2 1 
   0 2 2 1 1 0

4  * X 0 0 0 *  1
3  * X x x 0 *  2
0  * * * * * *  0
4  * 0 X 0 0 *  1
2  * x x x 0 *  3
3  * x 0 0 x *  1,1
   
   0 3 4 5 5 0

--------------------------
     2 1 
   0 2 2 1 1 0

4  * X 0 0 0 *  1
3  * X x 0 0 *  2
0  * * * * * *  0
4  * 0 X 0 0 *  1
2  * x x x 0 *  3
3  * x 0 0 x *  1,1
   
   0 3 4 5 5 0

--------------------------
pos:"0","2","4",""
col:"0","2,2","1,2","1","1","0"
row:"1","2","0","1","3","1,1"

1) find statistical chance of each square being on
2) cancel down and across




--------------------------
     2 1 
   0 2 2 1 1 0

4  * x x x x *  1
3  * x x x x *  2
0  * * * * * *  0
4  * x x x x *  1
2  * x x x x *  3
3  * x x x x *  1,1
   
   0 3 4 5 5 0 

1)Turn squares on
2)




----------
ANS

* x * * * *
* x x * * *
* * * * * *
* * x * * *
* x x x * *
* x * * x *
-------------

"5","2,2","1,1","2,2","5"
"5","2,2","1,1","2,2","5"


--------------
     2 1 2 
   5 2 1 2 5

1  * * * * *  5
1  * * * * *  2,2
6  3 2 2 2 3  1,1
1  * * * * *  2,2
1  * * * * *  5

   1 1 5 1 1


1) for each row calculate number of permutations possible, if = 1 then fill squares
2) for each col calculate number of permutations possible, if = 1 then fill squares
3) create a statistical grid, fill squares with chance of being ON
-4) assume highest chance is on, 
4)
5) foreach row, does match row hint?, 
    yes- change chance of others to 0
6) foreach col,does match col hint?,
    yes- change chance of others to 0
    no - can be deduced from colHint pattern match?  
        yes - change others to 0
        no - can be deduced from double hint pattern match? ie(row & col pattern match)
            yes - change others to 0

7) repeat 5 & 6 until no more changes
-------------------


Start with a grid of 0's where 0=unknown, 1=off, 2=on
For each row of hints, generate all possible permutations of that row 
    (skipping the permutations where a possible on value overlaps with a given off value to speed things up).
    If a column is off for every possible permutation 
        then set the row's cell to off. 
    If a column is on for every possible permutation 
        then set the row's cell to on. 
    Otherwise it is still unknown.

Do the same for every column of hints.
Repeat 2-4 until no more changes are possible.

-------------------

    2 1 
  0 2 2 1 1 0

4 - 2 - - - - 1
2 - 2 2 - - - 2
0 - - - - - - 0
4 - * * - - - 1
2 - 2 2 2 - - 3
3 - * * - 2 - 1,1

  0 3 4 5 5 0 
-------------------
 (3)
     2 1 
   0 2 2 1 1 0

4  * x * * * *  1
2  * x x * * *  2
0  * * * * * *  0
4  * x * * * *  1
2  * x x x * *  3
3  * * x * x *  1,1
  
  0 3 4 5 5 0 
-------------------
(3)
     2 1 
   0 2 2 1 1 0

4  * 2 2 2 2 *  1
2  * 2 3 3 2 *  2
0  * * * * * *  0
4  * 2 2 2 2 *  1
2  * 3 4 3 2 *  3
3  * 2 3 3 2 *  1,1
  
  0 3 4 5 5 0 
-------------------
(3)
     2 1 
   0 2 2 1 1 0

4  * 1 1 1 1 *  1
2  * 1 2 2 1 *  2
0  * * * * * *  0
4  * 1 1 1 1 *  1
2  * 1 2 2 1 *  3
3  * 1 2 2 1 *  1,1
  
  0 3 4 5 5 0 

-------------------
    2 1 
  0 2 2 1 1 0
4 * * * * * * 1
2 * * * * * * 2
0 * * * * * * 0
4 * * * * * * 1
2 * * * * * * 3
3 * * * * * * 1,1
  0 3 4 5 5 0 


=================
ANS =

* x * * * *
* x x * * *
* * * * * *
* * x * * *
* x x x * *
* x * * x *




=============================



cols=0,1,1,1,0
rows=0,'1,1',0,1,0

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *


loop through columns
    not zero:
        scan row for count match




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