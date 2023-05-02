# # Задание 1
# a=int(input())
# b=int(input())
# c=int(input())
# if a==b==c:
#     print('3')
# elif a==b or b==c or c==a:
#     print('2')
# else:
#     print('0')

# Задание 2
# across_1=int(input())
# down_1=int(input())
# across_2=int(input())
# down_2=int(input())
# if across_1>8 or across_2>8 or down_1>8 or down_2>8:
#     print('ERROR')
# else:
#     if across_1==across_2 or down_1==down_2:
#         print('YES')
#     else:
#         print('NO')

# # Задание 3
# print('Введите пароль более 8 символов, который включает прописные и загавные буквы')
# check=False
# prop=0
# zagl=0
# while True:
#     PASSWORD=input()
#     for i in range(len(PASSWORD)):
#         if PASSWORD[i] in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
#             prop+=1
#         if PASSWORD[i] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             zagl+=1
#     if len(PASSWORD)>8 and prop>0 and zagl>0:
#         print('Пароль допустимый')
#         break
#     else:
#         print('Пароль не соответсвует требованиям')
        

print('Введите пароль более 8 символов, который включает прописные и загавные буквы')
while True:
    PASSWORD=str(input())
    if len(PASSWORD)>8 and not PASSWORD.isupper() and not PASSWORD.islower() and not PASSWORD.isnumeric():
        print('Пароль допустимый')
        break
    else:
        print('Пароль не соответсвует требованиям')



across_1=int(input())
down_1=int(input())
across_2=int(input())
down_2=int(input())
if across_1>8 or across_2>8 or down_1>8 or down_2>8:
    print('ERROR')
else:
    if across_1==across_2 or down_1==down_2 or abs(across_1-across_2) or abs(down_1-down_2) or abs(across_1+across_2) or abs(down_1+down_2):
        print('YES')
    else:
        print('NO')