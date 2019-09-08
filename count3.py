

def Count3Out2(n):
    arr=list(range(1,n+1))
    cnter=0
    inx=0
    while len(arr)>1:
        cnter+=1
        if cnter==3:
            arr.pop(inx)
            inx-=1
            cnter=0
        inx+=1
        if inx==len(arr): inx=0
    print(arr[0])




def Count3Out(n):
    arr=list(range(1,n+1))
    delCnt=0
    cnter=0
    while delCnt<n-1:
        for i in range(n):
            if arr[i]!=0:
                cnter+=1
                if cnter==3:
                    arr[i]=0
                    cnter=0
                    delCnt+=1
    for i in arr:
        if i!=0: print(i)

if __name__=='__main__':
    n=int(input())
    Count3Out(n)
    # Delete people who count 3