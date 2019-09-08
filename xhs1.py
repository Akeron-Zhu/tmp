import functools


def binSearch(val,res,left,right):
    while left<=right:
        mid=(left+right)>>1
        if res[mid]<val: left=mid+1
        elif res[mid]>val: right=mid-1
        else: return mid
    return right

def cmp(a,b):
    if a[0]<b[0]: return -1
    elif a[0]>b[0]: return 1
    else:
        if a[1]<b[1]: return -1
        else: return 1

def binarySearch(number,a,left,right):
        if left==right:
            return left
        while left<right:
            mid=(left+right)>>1
            if mid==left or mid==right:
                if number>a[left]:
                    return right
                else:
                    return left
            if number<a[mid]:
                return binarySearch(a,number,left,mid)
            else:
                return binarySearch(a,number,mid,right)

if __name__=='__main__':
    num=int(input())
    arr=[]
    for i in range(num):
        val=tuple(map(int,input().split()))
        arr.append(val)
    arr=sorted(arr,key=functools.cmp_to_key(cmp))
    #print(arr)

    res=[arr[0][1]]
    for i in range(1,num):
        if arr[i][1]>=res[-1]:
            res.append(arr[i][1])
        else:
            if arr[i][1]<res[0]:
                res[0]=arr[i][1]
            else:
                pos=binarySearch(arr[i][1],res,0,len(res)-1)
                res[pos]=arr[i][1]
        #print(res)
    print(len(res))




'''
    dp=[0 for i in range(num)]
    for i in range(num):
        maxm=0
        for j in range(i):
            if arr[i][1]>=arr[j][1]:
                maxm=max(maxm,dp[j])
        dp[i]=maxm+1
    #print(dp)
    print(max(dp))
'''


