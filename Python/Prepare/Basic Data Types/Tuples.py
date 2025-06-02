if __name__ == '__main__':
    n = int(input())
    l = input().strip().split()
    l = map(int, l)
    t = tuple(l)
    print(hash(t))
        
