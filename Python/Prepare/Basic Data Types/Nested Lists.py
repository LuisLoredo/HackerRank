if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    secondLowestScore = set([record[1] for record in records])
    secondLowestScore = list(secondLowestScore)
    secondLowestScore = sorted(secondLowestScore)
    secondLowestScore = secondLowestScore[1]
    
    orderedNames = [x[0] 
        for x in records 
        if x[1] == secondLowestScore]
    orderedNames = sorted(orderedNames)
    
    for name in orderedNames:
        print(name)
