# l=[1, 4, 1, 6, 'hello', 'a', 5, 'hello']
# l_1=[]
# l_2=[]
# l_new=[]
# ex_l=0
# for i in range(len(l)):
#     if type(l[i])==int:
#         l_1.append(l[i])
#     else:
#         l_2.append(l[i])
# l_sort1=sorted(l_1)
# l_sort2=sorted(l_2)
# for i in range(len(l_sort1)):
#     if l_sort1[i]==ex_l:
#         l_new.append(l_sort1[i])
#     ex_l=l_sort1[i]
# for i in range(len(l_sort2)):
#     if l_sort2[i]==ex_l:
#         l_new.append(l_sort2[i])
#     ex_l=l_sort2[i]
# print(l_new)



from random import randint
n=5
m=[[randint(0,100) for i in range(n)] for j in range(n)]
j=0
maks=m[0][j]
for i in range(n):  
    for j in range(n):
        if m[i][j]>maks:
            maks=m[i][j]  
print(m)
print(maks)





# d={'name1':'id1','name2':'id2','name3':'id3'}
# d_new={v: k for k, v in d.items()}
# print(d)
# print(d_new) 
