
if __name__=='__main__':
    arr=list(map(int,input().split()))
    xiaomi,dami=0,0
    lena=len(arr)
    dp=[[0]*lena for i in range(lena)]
    for i in range(lena):
        dp[i][i]=arr[i]
    for i in range(lena-1,-1,-1):
        summ=arr[i]
        for j in range(i+1,lena):
            summ+=arr[j]
            dp[i][j]=summ-min(dp[i+1][j],dp[i][j-1])
    xiaomi=dp[0][lena-1]
    dami=sum(arr)-xiaomi

    if xiaomi>=dami: print('Yes')
    else: print('No')
