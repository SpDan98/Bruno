# def foo(n):
#     if n==1:
#         return n
#     else:
#         return foo(n-1)
# r=foo(5)
# print(r)

# def factorial(n):
#     if n==1:
#         print(f'n:{n}')
#         return n
#     else:
#         print(f'n:{n}')
#         return n*factorial(n-1)
# f=factorial(15)
# print(f)

# import random
# import time
# l=[random.randint(-100,100) for i in range(1000000)]
# def simple_search(n):
#     k=int(input())
#     for i in range(len(l)):
#         if n[i]==k:
#             return i
#     return None
# time1=time.time()
# print(simple_search(l))
# time2=time.time()
# print(time2-time1)

# import random
# import time
# def binary_search(arr,value):
#     low_index=0
#     high_index=len(arr)-1
#     while low_index<=high_index:
#         mid_index=(low_index+high_index)//2
#         if arr[mid_index]== value:
#             return mid_index
#         if value>arr[mid_index]:
#             low_index=mid_index+1
#         else:
#             high_index=mid_index-1
#     return None
# a=sorted([random.randint(-100,100) for i in range(1000000)])
# k=int(input())
# time1=time.time()
# print(binary_search(a,k))
# time2=time.time()
# print(time2-time1)

# import numpy as np
# import random
# import time
# PATH_100='bruno/lesson6/path/100.txt'
# PATH_1000='bruno/lesson6/path/1000.txt'
# PATH_10000='bruno/lesson6/path/10000.txt'
# PATH_100000='bruno/lesson6/path/100000.txt'
# PATH_1000000='bruno/lesson6/path/1000000.txt'
# PATH_RESULT='bruno/lesson6/path/result.txt'
# def write_arr_to_file(path,size):
#     a=[random.randint(-1000,1000) for i in range(size)]
#     with open(path,'w') as f:
#         for i in a:
#             f.write(str(i)+'\n')
# def read_arr_from_file(path):
#     arr=[]
#     with open(path,'r') as f:
#         for i in f:
#             arr.append(int(i))
#     return arr
# def writeresult(path,data):
#     with open(path, 'a+') as f:
#         f.write(str(data)+'\n')
# def bubblesort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
# def combosort(arr):
#     step=len(arr)
#     swap=True
#     while swap or step > 1:
#         step=int(step/1.247)
#         swap=False
#         for i in range(len(arr)-step):
#             j=i+step
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#                 swap=True
# def quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         q=sum(arr)//len(arr)
#         l=[]
#         m=[]
#         h=[]
#         for i in arr:
#             if i<q:
#                 l.append(i)
#             elif i>q:
#                 h.append(i)
#             else:
#                 m.append(i)
#         return quicksort(l)+m+quicksort(h)
# a=[random.randint(-1000,1000) for i in range(10)]
# temparr=read_arr_from_file(PATH_1000000)
# stime=time.time()
# quicksort(temparr)
# ftime=time.time()
# fftime=ftime-stime
# writeresult(PATH_RESULT,f'quicksort1000000 {fftime}')