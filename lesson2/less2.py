# PASSWORD='password'
# check=False
# count_of_input=0
# while True:
#     prepassword=input()
#     if prepassword==PASSWORD:
#         check=True
#         print('пароль верный')
#         break
#     else:
#         check=False
#         print('пароль неверный')
#         count_of_input+=1
#         if count_of_input>=2:
#             print('превышено количество попыток')
#             break

# a=0
# while a<10:
#     print(a)
#     a+=1

# k=int(input())
# n=int(input())
# while k!=n:
#     print(k)
#     k+=1

# k=int(input())
# n=int(input())
# while k!=n:
#     print((n-1)**2)
#     n-=1

# word='simpleword'
# for i in word:
#     print(i)

# for i in 'word','hello','baza':
#     for j in i:
#         print(j)

# n=int(input())
# k=int(input())
# sum=0
# while n>=k:
#     sum+=n
#     n+=1
# print(sum)

# n=int(input())
# k=int(input())
# sum=1
# while n>=k:
#     sum*=n
#     n+=1
# print(sum)

# l=[1,4,'hello']
# print(l[2])

# l=[1,4,'hello']
# print(l[2][1])

l=[1,4,'hello',[6,7,11],[326,[1,2,[7,'baza']]]]
print(l[4][1][2][1])

# l=[]
# l.append(1)
# l.append(2)
# l.append(3)
# index=0
# for i in l:
#     l[index]=i**2
#     index+=1
# print(l)

# l=[1,2,3]
# r=list(range(5))
# for i in range(len(l)):
#     l[i]=l[i]**2
# print(l)

# l1=[1,2,3]
# l2=l1.copy
# l3[1]=10
# print(id(l1),id(l2))

# l=[15,-1,15151,-1515,0,0,1,2,6,-14]
# max_elem=l[0]
# for i in range(len(l)):
#     if l[i]>max_elem:
#         max_elem=l[i]
# print(max_elem)

# l=[15,-1,15151,-1515,0,0,1,2,6,-14]
# print(l[1:4:])

    # Есть массив элементов. Раскидать эелементы меньше и больше опорного по разным массивам.
# l_start=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# sum=0
# for i in range(len(l_start)):
#     sum+=l_start[i]
# k=sum//len(l_start)
# l_less=[]
# l_more=[]
# for i in range(len(l_start)):
#     if l_start[i]>=k:
#         l_more.append(l_start[i])
#     else:
#         l_less.append(l_start[i])
# print(k,l_less,l_more)

    # Есть массив элементов. Раскидать эелементы меньше и больше опорного по разным массивам. Сделать опорным элементом значение из середины индекса.
# l_start=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# k=l_start[len(l_start)//2]
# l_less=[]
# l_more=[]
# for i in range(len(l_start)):
#     if l_start[i]>=k:
#         l_more.append(l_start[i])
#     else:
#         l_less.append(l_start[i])
# print(k,l_less,l_more)

    # Задача: создать новый массив из элементов под четным индексом.
# l_start=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# l_new=[]
# for i in range(len(l_start)):
#     if i%2==0:
#         l_new.append(l_start[i])
# print(l_new)