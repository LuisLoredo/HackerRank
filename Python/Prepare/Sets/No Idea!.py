# Enter your code here. Read input from STDIN. Print output to STDOUT

def read_input(makeSet = False):
    userInput = input().strip().split()
    
    if makeSet:
        userInput = set(userInput)
        
    return userInput

n, m = read_input()
l = read_input()
A = read_input(makeSet = True)
B = read_input(makeSet = True)

def happinessMeasure(l, A, B):
    happiness = 0
    for element in l:
        if element in A:
            happiness += 1
        if element in B:
            happiness += -1
    return happiness
    
print(happinessMeasure(l, A, B))
