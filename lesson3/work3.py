# x=float(input('Размер вклада '))
# y=float(input('Желаемая сумма '))
# p=float(input('процент '))
# years=0
# while x<y:
#     x+=x*p/100
#     years+=1
# print(years)


# n=int(input())
# n1=0
# while n1!=n:
#     print('for - частный случай while')
#     n1+=1


n=int(input())
sum=0
while n!=0:
    last=n%10
    sum+=last
    n=n//10
print(sum)
