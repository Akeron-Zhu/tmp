
def partsort(arr,left,right):
    if left>=right: return
    key=right
    while left<right:
        while left<right and arr[left]<=arr[key]: left+=1
        while left<right and arr[right]>=arr[key]: right-=1
        arr[left],arr[right]=arr[right],arr[left]
    arr[key],arr[right]=arr[right],arr[key]
    return right


def qsort(arr,left,right):
    if left>=right:
        return 
    mid=partsort(arr,left,right)
    qsort(arr,left,mid-1)
    qsort(arr,mid+1,right)


if __name__=='__main__':
    arr=[82,90,4,70,2,9,1,4]
    lena=len(arr)
    qsort(arr,0,lena-1)
    print(arr)