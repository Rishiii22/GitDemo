
# Qn2.
# import array as arr
# My_Array=arr.array('i',[1,2,3,4])
# My_list=[1,'abc',1.20]
# print(My_Array)
# print(My_list)

# Qn3.
# class Puppy:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
# class Rayj():
#     def speak(self):
#         return "Arff!"
# bobo=Rayj()
# print(bobo.speak())

# Qn4.
class Employee:
    Department='CIS'
    def __init__(self,id):
        self.id=id
    def setAddress(self,address):
        self.address=address
    def getAddress(self):
        return self.address
a=Employee(101)
a.setAddress("Bangalore,Karnataka")
print(a.getAddress())
print("Saptarsijnfe")

