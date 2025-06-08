# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input().strip())
Nlist = input().split()
Nlist = list(map(int, Nlist))

condition1 = all([x > 0 for x in Nlist])
condition2 = any([str(x)==str(x)[::-1] for x in Nlist])

if condition1 and condition2:
        print("True")
else:
    print("False")
