import random
            # Task 1

# text=input("Task 1 - Input ")
# if str.isdigit(text): 
#     print('Your input is a Number')
# elif str.isalpha(text):
#     print('Your input is a Text')
# else:
#     print(text)

            # Task 2

# year=int(input("Task 2 - Input year "))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print('This is leap-year')
# else: 
#     print('This is usual year')

            # Task 3

# ruble=int(input("Task 3 - Input rubles "))
# coin=int(input("Task 3 - Input coins "))
# if ruble%10==1:
#     rub='ь'
# elif ruble%10 in (2, 3, 4):
#     rub='я'
# else:
#     rub='ей'

# if coin%10==1:
#     co='йка'
# elif coin%10 in (2, 3, 4):
#     co='йки'
# else:
#     co='ек'
# print("{} рубл{}, {} копе{}".format(ruble, rub, coin, co))

            # Task 4

#print("Look, Task 4")
# stroka=str('abcdefghijklmnopqrstuvwxyz')
# l=list(stroka)
# for item in l:
#     if item in ('a', 'e', 'i','o', 'u', 'y'):
#         continue
#     print(item)
     
            # Task 5

#print("Look, Task 5")
# keys=list([1,2,3,4,5])
# values=list(['a', 'b', 'c', 'd', 'e'])
# d=dict((k, v) for k, v in zip(keys, values))
# print(d)

            # Task 7 - not completed

# r=0
# s=0
# t=0
# while r not in (0, 10):
#     r=random.randint(0,10)
#     s=s+r
#     t=t+1
#     print("number {}, sum= {}, try № {}".format(r, s, t))
#     continue   

sum = 0
count = 0
while True:
    x = random.randint(0, 10)
    sum+=x
    count+=1
    print(x, sum, count)
    if x == 0 or x == 10:
        break
    
            # Task 8
# password=input("Task 8 - Input password ")

# for pass_try in range(0, 3):
#     pass_try=input("Check you password ")
#     if pass_try==password:
#         print('Correct')
#         break
#     else:
#         print("Try again")
