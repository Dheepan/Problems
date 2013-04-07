import sys,fileinput

class RobotWalk:

    def __init__(self,array):
        self.array=array
        self.grid=None
        self.m=None
        self.n=None

    def walk(self):
        self.generateVerticesCodeforGrid()
        self.printAllValidPaths(self.m-1,self.n-1,self.grid,"")

    def generateVerticesCodeforGrid(self):
        if not self.ifRectangularArray():
            print "Not an rectangular Grid"
            raw_input()
            sys.exit()
        row_len=len(self.array)
        col_len=len(self.array[0])
        #row length for the vertices grid (r+1)
        self.m=row_len+1
        #column length for the vertices grid (c+1)
        self.n=col_len+1
        #create grid vertices array initialized with all zeros
        self.grid=[[0]*self.n for x in xrange(self.m)]
        #iterate through the array and update grid vertices value 0-movable vertex 1-not movable vertex
        for i in range(row_len):
            for j in range(col_len):
                if self.array[i][j]=='1':
                    self.grid[i][j]=1
                    self.grid[i][j+1]=1
                    self.grid[i+1][j]=1
                    self.grid[i+1][j+1]=1
  
    def ifRectangularArray(self):
        col_length=len(self.array[0])
        for i in range(len(self.array)):
            if len(self.array[i])!=col_length:
                return False
        return True
        
    def printAllValidPaths(self,m,n,grid,path):
        #if its a invalid vertex and just return
        if grid[m][n]==1:
            return;
        #check if we reached to the top left corner of Grid and print the path
        elif m==0 and n==0:
            print path
        else:
            #recursively move up marking "D" till we reach top
            if m-1>=0:
                self.printAllValidPaths(m-1,n,grid,"D"+path)
            #recursively move left marking "R" till we reach top
            if n-1>=0:
                self.printAllValidPaths(m,n-1,grid,"R"+path)

if __name__=="__main__":
    #Rectangular Grid containing obstacles - dimension MxN - 0 - walkable grid cell and 1- not walkable grid cell
    grid=[]
    for line in fileinput.input("Robot_Input.txt"):
        temp=list(line.strip("\n"))
        if len(temp)!=0:
            grid.append(temp)
    r=RobotWalk(grid)
    r.walk()
