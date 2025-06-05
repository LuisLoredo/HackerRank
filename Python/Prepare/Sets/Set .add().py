# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input().strip())
counter = set()

for n in range(N):
    counter.add(input().strip())
    
print(len(counter))
