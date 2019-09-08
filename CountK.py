
def digitCount(val,k):
    base=1
    res=0
    while base<=val:
        highPart=val//(base*10)
        lowPart=val%base
        cur=(val//base)%10
        if cur<k:
            res+=highPart*base
        elif cur>k:
            res+=(highPart+1)*base
        else:
            res+=highPart*base+lowPart+1
        if 0==k:
            res-=base
        base*=10
    return res


if __name__=='__main__':
    val,k=list(map(int,input().split()))
    print(digitCount(val,k))