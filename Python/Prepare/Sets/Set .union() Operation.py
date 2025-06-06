# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
n_students = input().strip().split()

b = int(input().strip())
b_students = input().strip().split()

total_students = set(n_students).union(set(b_students))
print(len(total_students))
