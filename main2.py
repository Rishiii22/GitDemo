#Qn5.
# class Alpha:
#     def __init__(self):
#         self.calculate(30)
#     def calculate(self,i):
#         self.i=2*i;
# class Beta(Alpha):
#     def __init__(self):
#         super().__init__()
#         print("i from Beta is",self.i)
#     def calculate(self,i):
#         self.i=3*i;
# b=Beta()

# Qn6.
# class Employee:
#     def __init__(self,id):
#         self.id=id
#         id=10
# Res=Employee(789)
# print(Res.id)
# Qn7.
class Puppy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class rayj(Puppy):
    pass
class Maxy(Puppy):
    pass
class  Pug(Puppy):
    pass
# miles=JackRusselTerrier("Miles",4)
buddy=Maxy("Buddy",9)
jack=Pug("Jack",3)
jim=Pug("jim",5)
print(isinstance(jack,Maxy))
print(isinstance(jack,Maxy))
# print("testing Git")
