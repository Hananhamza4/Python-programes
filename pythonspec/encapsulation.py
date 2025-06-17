


# class person:
#     def __init__(self,name):
#         self.__name=name
#     def __nameprint(self):
#         print("hello ",self.__name)
#     def public1(self):
#         self.__nameprint()

# obj=person("hanan")
# obj.public1()


# class bankaccount:
#     def __init__(self,bankbalace,bankname):
#         self.__bankbalance=bankbalace
#         self.bankname=bankname
#     def __private1(self):
#         print("your balance",self.__bankbalance)
#         print("your bank name is",self.bankname)
#     def public1(self):
#         self.__private1()
# obj=bankaccount(1000,"canara")
# obj.public1()   
# 
#         

#private which is rep by an single under score


class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _display(self):
        print("name",self._name)
        print("age",self._age)
class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self._roll_number=roll_number
    def display(self):
        self._display()
        print("roll number",self._roll_number) 

s=Student("jhon",20,123)
s.display()           
                   