if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr,reverse=True)
    maxi=max(arr)
    for i in arr:
        if(i!=maxi):
            print(i)
            quit()
        
