def average(array):
    # your code goes here
    sarray = set(array)
    return sum(sarray)/len(sarray)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
