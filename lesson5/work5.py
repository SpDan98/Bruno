# import math
# def area(a,b,c):
#     p=(a+b+c)/2
#     return math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(area(3,4,5))


# s='''Было просто пасмурно, дуло с севера,
# А к обеду насчитал сто градаций серого.
# Так всегда первого ноль девятого,
# То ли весь мир сошёл с ума, то ли я - того...
# На столе записка от неё смятая,
# Недопитый виски допиваю с матами.
# Посмотрю в окно, допишу главу,
# Первое сентября, дворник жжёт листву.
# И серым облакам наплевать на нас,
# Если знаешь как жить - живи,
# Ты хотела быть как все - так плыви!'''
# def word_less():
#     s_less=[]
#     words=s.split()
#     for i in range(len(words)):
#         if len(words[i])<5 and words[i]!='-':
#             s_less.append(words[i])
#     s_less=' '.join(s_less)
#     return s_less
# print(word_less())

 

# n_mas=list(map(int,input('Введите числа через пробел ').split()))

# def maks_num_of_n(arr):

#     maks_num=arr[0]

#     for i in range(len(arr)):
#         if arr[i]>maks_num:
#             maks_num+=arr[i]
#     return maks_num

# print(maks_num_of_n(n_mas))
# print(n_mas)


def restore(arr):
    s=len(arr)-1
    num=0
    i=0
    while s!=-1:
        num+=arr[i]*10**s
        s-=1
        i+=1
    return num
def find_max(*args):
    if args:
        arr=[]
        for i in args:
            k=i
            little_arr=[]
            while k!=0:
                j=k%10
                k=k//10
                little_arr.insert(0,j)
            arr.append(little_arr)
        arr=sorted(arr,reverse=True)
        new_arr=[]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                new_arr.append(arr[i][j])
        num=restore(new_arr)
        return num
    else:
        print('no arguments')
# print(find_max(list(map(int,input('Введите числа через пробел ').split()))))
print(find_max(12,23,123,356,689,3446,9876))
