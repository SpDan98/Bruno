import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        q=sum(arr)//len(arr)
        l=[]
        m=[]
        h=[]
        for i in arr:
            if i<q:
                l.append(i)
            elif i>q:
                h.append(i)
            else:
                m.append(i)
        return quicksort(l)+m+quicksort(h)
def binary_search(arr, n):
    low=0
    mid=len(arr)//2
    high=len(arr)-1
    while mid != n:
        if n>mid and low<=high:
            low=mid+1
        elif n<mid:
            high=mid-1
        mid=(low+high)//2
    return mid




a=[random.randint(-1000,1000) for i in range(10)]
a_sort=quicksort(a)
print(a_sort)
