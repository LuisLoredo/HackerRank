if __name__ == '__main__':
    masterList = []
    N = int(input())

    for n in range(N):
        command = input().strip().split(' ')
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            masterList.insert(i, e)
        elif command[0] == "print":
            print(masterList)
        elif command[0] == "remove":
            e = int(command[1])
            masterList.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            masterList.append(e)
        elif command[0] == "sort":
            masterList.sort()
        elif command[0] == "pop":
            masterList.pop()           
        elif command[0] == "reverse":
            masterList.reverse()              
            
