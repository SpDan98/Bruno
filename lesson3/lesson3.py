# Вывод n первых эелементов массива двумя способами
# l=['qwerty','lesson','345','123','asd','678','bnm' ]
# n=int(input())
# for i in range(n):
#     print(l[i])

# l=['qwerty','lesson','345','123','asd','678','bnm' ]
# n=int(input())
# print(l[:n:])

# кортеж
# tup=(326,215,769)
# tup.

# словарь
# d={'key1':'valuel1','key2':'valuel2'}
# print(d['key2'])
# d={'имя':'Даня','возраст':'24'}
# print(d['имя'])
# d={'имя':'Даня','возраст':[5,25]}
# print(d['возраст'])
# d={'имя':'Даня','возраст':'24'}
# d['почта']='d@y.ru'
# print(d['почта'])

# d={'название':'Xiomi','год выпуска':'2022','подробные характеристики':{'камера':'64mp','процессор':{'частота':'3,3ghz','ядер':'100'}}}
# print(d['подробные характеристики']['процессор']['ядер'])

# d={'город':'СПб','адрес':{'улица':'садовая','дом':23}}
# print(d['адрес']['дом'])

# функции
# print('hello')       #print - функция 'hello' - аргумент

# def test_foo():
#     print('I am test foo')
# test_foo()

# def test_foo():
#     print('I am test foo')
# print(type(test_foo))

# def test_foo(argument):
#     print(argument)
# test_foo('Hello world')

# def test_foo(arg):
#     print(arg,'forever')
# test_foo('Goodbye world')

# def custom_sum(a,b):
#     return a+b
# def custom_sum1(a,b):
#     print(a+b)
# c=custom_sum(2,3)
# d=custom_sum1(2,3)
# print(c,d)

# def custom_pr(a,b):
#     return a*b
# print(custom_pr(2,3))

l=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
l1=[15,223,651,450,-15,1,26,-15,0,-2356,4]
def find_maximum(arr):
    max_elem=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_elem:
            max_elem=arr[i]
    return max_elem
print(find_maximum(l))
print(find_maximum(l1))

# def sum_from_n_to_k(n,k):
#     if n>=k:
#         return -1
#     while n<k:
#         print(n)
#         n+=1
# sum_from_n_to_k(4,9)
# sum_from_n_to_k(44,99)
# sum_from_n_to_k(444,999)
# sum_from_n_to_k(-4,19)
# sum_from_n_to_k(-34,-9)

# l=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# def in_out(list):
#     last=len(list)-1
#     first=0
#     while first<last:
#         # list[first],l[last]=l[last],list[first]
#         value=list[first]                   #по принципу замены жидкостей в двух стаканах с помощью пустого третьего
#         list[first]=list[last]
#         list[last]=value
#         first+=1
#         last-=1
#     print(list)
# in_out(l)

# l=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# def centr_l(list):
#     k=len(list)//2
#     print(list[k])
# centr_l(l)

# l=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# def centr_l(list):
#     sum=0
#     for i in l:
#         sum+=i
#     average=sum//len(list)
#     return average
# print(centr_l(l))
