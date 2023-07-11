if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg,sum,c=0,0,0
    find=student_marks[query_name]
    for i in find:
        sum+=i
        c+=1
    avg=sum/c
    print("%.2f" % avg)
