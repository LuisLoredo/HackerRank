if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    averageScore = list(student_marks.get(query_name))
    averageScore = sum(averageScore) / len(averageScore)
    print("%.2f" %averageScore)
