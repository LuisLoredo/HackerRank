# Enter your code here. Read input from STDIN. Print output to STDOUT
N = map(int, input().strip().split())
Nlist = list(map(int, input().strip().split()))

condition1 = all([n > 0 for n in Nlist])
condition2 = any([str(n) == str(n)[::-1] for n in Nlist])


if condition1 and condition2:
    print('True')
else:
    print('False')
