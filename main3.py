#Qn.9
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def cal_salary(self,sal):
#       pass
# class Developer(Employee):
#     def cal_salary(self,sal):
#         Tsalary=sal*1.10
#         return Tsalary
# emp_1=Developer()
# print(emp_1.cal_salary(10000))

#Qn10.
# class Test():
#     pass
# print(Test.__name__)

#Qn16.
# def f(x,I=[]):
#     for i in range(x):
#         I.append(i*i)
#     print(I)
# f(2)

#Qn17.
# f=None
# for i in range(5):
#     with open("data.txt","w") as f:
#         if i>2:
#             break
# print(f.closed)

#Qn18.
with open("data.txt") as fh:
    count=0
    text=fh.read()
    for character in text:
        if character.isupper():
            count+=2
print(count)

#Qn20.
# def f(value,values):
#     v=1
#     values[0]=44
# t=3
# v=[1,2,3]
# f(t,v)
# print(t,v[0])

# Qn21
# s1={1,2,3}
# s2={3,4,5}
# print(s1.union(s2))
# print(s1 |{3,4,5})

# Qn22.
# item={n:n*2 for n in range(10)}
# print(item)

# Qn23.
# def multiplexers():
#     return [lambda n:index*n for index in range(4)]
# print([m(2) for m in multiplexers()])

# Qn24.
# a=input("enter seq")
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not a palindrome")

# Qn.25
# item=[n*2 for n in range(10)]
# print(item)

# Qn26
# import numpy as np
# duplicates=['a','b','c','d','d','d','e','f','g','g','h']
# unique=list(np.unique(duplicates))
# print(sorted(unique))

# Qn27
# try:
#     if '1'!=1:
#         raise "someError"
#     else:
#         print("someError has not occured")
# except "someError":
#     print("someError has occured")

# Qn28
# f=open("data1.txt",'w')
# f1=open("data2.txt",'r')

# Qn29.
# import re
# sentence='Learn Python Programming'
# test=re.match(r'(.*)(.*?)(.*)',sentence)
# print(test.group())

# Qn3 new

# my_list=[1,5,4,6,8,11,3,12]
# new_list=list(filter(lambda x:(x%2==0),my_list))
# print(new_list)
print("testing the git again")
