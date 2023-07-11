if __name__ == '__main__':
    stud=[]
    stu=[]
    for _ in range(int(input())):
        name = input()
        stu.append(name)
        score = float(input())
        stu.append(score)
        stud.append(stu)
        stu=[]
    for i in stud:
        stu.append(i[1])
    stu=sorted(stu)
    low=min(stu)
    for i in stu:
        if (i>low):
            low=i
            break
    stu=[]
    for i in stud:
        if (i[1]==low):
            stu.append(i[0])
    for i in sorted(stu):
        print(i)
