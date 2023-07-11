if __name__ == '__main__':
    N = int(input())
    list=[]
    for k in range (0,N):
        comm=input()
        if ("insert" in comm):
            e=int(comm.split(' ')[2])
            i=int(comm.split(' ')[1])
            list.insert(i,e)
        elif(comm=="print"):
            print(list)
        elif("remove" in comm):
            e=int(comm.split(' ')[1])
            if (e in list):
                list.remove(e)
        elif("append" in comm):
            e=int(comm.split(' ')[1])
            list.insert(len(list),e)
        elif(comm=="sort"):
            list.sort()
        elif(comm=="pop"):
            list.pop(-1)
        elif (comm=="reverse"):
            list.reverse()
