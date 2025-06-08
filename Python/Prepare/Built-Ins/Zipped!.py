# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().strip().split())
data = [list(map(float, input().strip().split())) for _ in range(X)]
data_zipped = zip(*data)
[print(sum(subdata)/len(subdata)) for subdata in data_zipped]
