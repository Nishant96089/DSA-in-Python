def space():
    return print("\n")

# -- PATTERNS -- #

def rectangularStar(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
    space()    
         

def rightAngleStarPyramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
    space()    

def numPyramid1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()  
    space()      

def numPyramid2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
    space()    

def invertedStarPyramid(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print()
    space()

def invertedNumPyramid(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(n-j,end=" ")
        print()
    space()    

def starPyramid(n):
    pass    
                             

num = int(input("Enter a number: ")) 
rectangularStar(num)
rightAngleStarPyramid(num)
numPyramid1(num)
numPyramid2(num)
invertedStarPyramid(num)
invertedNumPyramid(num)