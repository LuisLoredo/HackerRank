# Enter your code here. Read input from STDIN. Print output to STDOUT

def readInput(makeSet = False):
    s = input().strip().split()
    s = map(int, s)
    s = list(s) 
    
    if makeSet:
        s = set(s)
        
    return s

def symmetricDifference(set1, set2):
    setUnion = set1.union(set2)
    setIntersection = set1.intersection(set2) 
    
    symmetricDiff = setUnion.difference(setIntersection)
    symmetricDiff = list(symmetricDiff)
    symmetricDiff.sort()
        
    return symmetricDiff
    
    
M = readInput()
set1 = readInput(makeSet=True)
N = readInput()
set2 = readInput(makeSet=True)
[print(element) for element in symmetricDifference(set1, set2)]
