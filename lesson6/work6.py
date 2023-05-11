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
a=[random.randint(-1000,1000) for i in range(10)]
# print(quicksort(a))

def bin_search(arr, n):
    low=0
    high=len(arr)-1
    while low <= high:
        mid=(low+high)//2
        if n==arr[mid]:
            return mid
        if n > arr[mid]:
            low=mid+1
        else:
            high=mid-1
    
l=[6, 17, 21, 27, 32, 34, 35, 36, 37, 48, 53]
# print(bin_search(l, 37))


def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
l1=[45,12,57,23,78,34]
print(insertion_sort(a))


