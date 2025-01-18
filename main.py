print("Welcome to the Python Programming")

# Tuples   :  Immutable, the items in the tuple cannot be changed   
# tupdemo = (1,2,3)
# strdemo = "Sagar"
# print(tupdemo)
# print(type(tupdemo))
# print(len(tupdemo),'\n', tupdemo[1])
# print (tupdemo[1:3])

# for i in tupdemo:
#     print(i)

#     tup = 'a',
#     str = ''.join(tup)
#     print(str)
#     print(type(tup))

# # f strings in python   from python 3.6 onwards
# print(f"this is {{strdemo}}")

# #docstrings in python use to print the comment in function, class, module  // call it using function.__doc__
# def testfund():
#     """This is a docstring function examples which is used to print the comments"""
#     print("This is a test function")

# testfund()
# print(testfund.__doc__)

#recursive function in python
# n = int(input("Enter the number: "))
# def functionrecur(n):
#     if(n==0 or n==1):
#       return 1
#     else:
#      return n * functionrecur(n-1)

# print("Factorial of the given number is:", functionrecur(n))


#sets in python, these are unordered data items, it cannot be changed and it does not allow duplicate values. {}
# import sys

# setdemo = {1,2,3,4,5,6,7,8,9,10}
# setdemo2 = {4,5,6,78,98,99}
# vardemo = "Sagar"
# emptyset = set()
# print(setdemo)
# print(str(sys.getsizeof(setdemo))+"bytes")
# print(sys.getsizeof(vardemo), type(setdemo), type(emptyset))
# for i in setdemo:
#     print(i)
#set methods
# print(setdemo.union(setdemo2))    #prints the union of two sets excluding the duplicate values.
# print("This method will update the set1 with the values that present in set2", setdemo.update(setdemo2))
# print(setdemo, setdemo2)
# print(setdemo.intersection(setdemo2))  #prints the common values in the two sets
# print(setdemo.intersection_update(setdemo2))  #prints the common values in the two sets 
# print(setdemo)
# print(setdemo.update("1,2,3,4"))
# print(setdemo)
# setdemo.discard('22')   #remove and discard methods to remove one item from the set and discard can be used to ignore the error if the item is not present in the set.
# print(setdemo)
# del setdemo  #deletes the entire set and clear () method is used to clear the set values.
# setdemo = {1,2,3,4,5,6,7,8,9,10}
# print(setdemo)

#dictionary in python, it is unordered, changeable and indexed. {key:value pairs} from python 3.7 onwards the order is maintained.
# dictdemo = {
#     "name": "Sagar",
#     "age": 28,
# }
# print(dictdemo['age'])
# print(dictdemo.keys())
# print(dictdemo.values())
# for key in dictdemo.keys():
#     # print(dictdemo[key])
#     print(f"The value corresponding to {key} is {dictdemo[key]}")

# print(dictdemo.items())
# for key, value in dictdemo.items():
#     print(f"Key is {key} and value is {value}")

#dictionary methods
# ep = {200: 45, 65:79, 45: 89}
# ep2 = {13: 56, 43:79, 76: 89}
# ep.update(ep2)
# print("This is an updated dictionary", ep)
# ep.pop(200)  #pop method is used to remove the key value pair from the dictionary with the key value.
# ep.popitem()  #popitem method is used to remove the last key value pair from the dictionary.
# del ep2
# print(ep)

# for i in range(6):
#   print(i)
#   # if i == 3:
#   #   break   #the else block will not be executed if the break statement is used.
# else:
#   print("This is the end block of the for loop")


#error handling in python
# try:
#   a= int(input("Enter the number: "))
#   c= a/0
#   print(c)
# except ValueError as e:
#   print("Number cannot be divided by zero!!!! Error message:", e)
# except ZeroDivisionError as e:
#   print("Number cannot be divided by zero!!!! Error message:", e)

# finally:        #even if the finally block is inside a function with return statement, the finally block will be executed. It is typically used for cleanup tasks and releasing resources that need to be performed no matter what.
#   print("This finally block will always be executed")

# print("This is the further continuation of the program")

#Raise an error

# a = int(input("Enter the number: \n"))
# if a < 0 or a> 10:
#   print("Number is between 0-10")
#   raise ValueError("Number must be between 0-10")

#built in FileNotFoundError
# def openfile(filename):
#   try:
#    file = open(filename, 'r')     #open the file in read mode
#    contents = print(file.read())  #read the contents of the file
#    print("This is the content of the file", contents)  #print the contents of the file
#    file.close()   #close the file to release the resources
#   except FileNotFoundError as e:
#     print("File not found in the directory", e)

# inputfile = input("Enter the file name: ")
# openfile(inputfile)

#reverse a string
# strex = "Sagar" [::-1] 
# print(strex)

#Enumerate function in python

# enudemo =  [1,2,3,45,5,6,8]
# index = 0
# for i in enudemo:
#   print(i)
#   if (index == 3):
#     print("Good work, Sagar")
#   index += 1
# print("This is the end of the program")


# enudemo =  [1,2,3,45,5,6,8]
# index = 0
# for index, i in enumerate(enudemo):      #enumerate function is used to get the index of the elements in the list.
#   print(i)
#   if (index == 3):
#     print("Good work, Sagar")
#     break
# print("This is the end of the program")
  
#virtual environment  :  python -m venv virtualenvname     //to create a virtual environment  
#deactivate the virtual environment : deactivate
#activate the virtual environment : source virtualenvname/bin/activate and then install the packages in the virtual environment.
#install different versions of pandas in the virtual environment : pip install pandas==0.25.0
#install different versions of python in the virtual environment : pyenv install 3.7.4
#find the installed pandas version : pip show pandas


# import math as m
# result = m.sqrt(729)
# print(result)
# import sagar as s
# # s.welcome()
# print(__name__)  #prints the name of the module

import os

# if (not os.path.exists("Data")):      #os.path.exists is used to check if the folder exists or not.
#     os.mkdir("Data")
# i = 0
# while (i<5):
#     os.mkdir("Data/Sagar")
#     i=i+1 
#     os.mkdir("Data/Ankita") 
#     i=i+1
#     os.mkdir("Data/Papa") 
#     i=i+1
#     os.mkdir("Data/Mummy") 
    # os.rename("Data/Mummy", "Data/M")  #os.rename is used to rename the folder

# print("The mentioned folders have been created")
# os.rename("Data/M", "Data/Mom") 
# print(os.listdir("Data/Sagar"))  #os.listdir is used to list the directories in the folder
# print(os.getcwd())  #os.getcwd is used to get the current working directory
# os.makedirs("Data1/Sagar1/Ankita1")  #os.makedirs is used to create the nested directories
# print(os.name)
# print(os.path.abspath('testfile.sr'))


#local and global variables in python
# x = 'This is a global variable'
# def test():
#     global x     #global keyword is used to declare the variable as global which can be accessed outside the function
#     x = "This is a local variable"
#     print(x)
# test()
# print(x)

#file handling in python
# file = open("Data/testfile.txt", "a")  #open the file in read mode and it is a default mode and write mode will create the file if it does not exist.
# file = open("Data/testfile.txt", "r+")  #open the file in read and write mode
# file.write("This statement is inserted after opening the file")
# filevar =  file.read(15)
# print(filevar)
# print(file.readlines())
# file.write("\nThis is the test line after the first statement")
# print(file.tell())
# print(file.seek(10))
# print(file.write("nnnnn"))
# print(file.tell())
# print(file.read(5))
# print(os.path.getsize("Data/testfile.txt"),' bytes')

# for line in file:
#     print(line.strip())

# config = {}
# print(type(config)) 
# print(os.cpu_count())

#lambda function in python  :  lambda arguments: expression single line function
# add = lambda x, y: x+y
# print(add(2,3))

# numbers = [1,2,3,4]
# # square = map(lambda a: a**2, numbers)
# # print(list(square))   

# cube = lambda x: x**3

# def apply(alreadydefinedfunction, value):
#     return print(alreadydefinedfunction(value))
# apply(cube, 3)

# print(cube(4))
# new1=[]
# print(map(cube, numbers))

#map function in python
# l = list(map(cube, numbers)) 
# print(l)   

#filter function in python

# def filter_function(x):
#     if x>2:
#         return True
#     else:
#         return False
# filteredlist = list(filter(filter_function, numbers))
# print(filteredlist)

# sum =  lambda x,y: x+y
# #reduce function in python
# from functools import reduce
# reducedcount = reduce(sum, numbers)
# print(reducedcount)


#is and ==    object interning is done for the values between -5 to 256. True will be returned. 
# a = 2580
# b = 2580
# c= 'hello12345 this is an example'
# d= 'hello12345 this is an example'
# print (a is b)
# print (c is d)

#OOPs concepts in python
# Classes and objects. everything in python is an object. Everything revolves around an object in python. certain classes will have their entity and their properties. Class is basically the blueprint/template of the object. Object is the instance of the class. Properties is the state of the object. Methods are the behavior of the object. Inheritance is the property of the object to inherit the properties of the parent class. Encapsulation is the property of the object to hide the data. Polymorphism is the property of the object to take multiple forms.

# class Family:
#     mother = "Jayshree"
#     father = "Bhanji"
#     sister = "Ankita"
#     def __init__(self1, n, o):  #self is the reference to the object of the class. It is used to access the variables of the class. __init__ is the constructor of the class. It is used to initialize the object of the class.
#         # self1.mother = n
#         # self1.father = o
#         print(f"My mother's name is {self1.mother} and her husband is {self1.father}")

    # def profession(demoobj):
    #     print(f"Mother's name - {demoobj.mother}, Profession - Housewife")
    #     print(f"Father's name - {demoobj.father}, Profession - Businessman")
    #     print(f"Sister's name - {demoobj.sister}, Profession - Software Engineer")

# a = Family('Sagar', 'Developer')  #creating the object of the family class
# b = Family()
# # profession(a) #passing the object of the class to the function
# a.mother = "Mom"
# print(a.mother)
# a.profession()
# print(id(a))

#constructor in python, it is used to initialize the object of the class. It is called automatically when the object is created. It is used to initialize the instance variables of the class.

#decorator in python,
# it is used to modify the behavior of the function or method. It is used to add extra functionality to the function. It is used to wrap the function and modify its behavior. To add functionality (like logging, validation, or timing) without modifying the original function.

# def dec_function(funobj):
#     def wrapper(*args, **kwargs):  #use to handle positional and keyword arguments. *args is used to handle any number of positional arguments and **kwargs is used to handle any number of the keyword arguments (key-value pair dictionary arguments).
#         print("Good Morning")
#         funobj(*args, **kwargs)  #calling the original function (test_fun())
#         print("Stay tuned")
#     return wrapper  

# @dec_function  # @ is used to call the decorator function. this is the syntactic sugar in python.
# def test_fun():
#     print("This is a test function")

# @dec_function
# def test_fun1(a,b):
#     print(a*b)

# test_fun1(8,9)

#getters and setters in python

# class gettersetterex:
#     def __init__(self, value):
#         self._value = value    #leading underscore is used to make the variable private. It is used to indicate that the variable is private and should not be accessed directly.
#     def showvar(self):      
#         print(f'The value is {self._value}')

#     @property         #property decorator is used to access the value of the variable.converts the method into a variable
#     def ten_value (self):
#         return 10*self._value

#     @ten_value.setter    #propertyname.setter is used to set the value of the variable.
#     def ten_value(self, new_value):
#         self._value = new_value/10   #no return statement is used in the setter method.

# objgetset = gettersetterex(5)
# objgetset.showvar()
# objgetset.ten_value = 100
# objgetset.showvar()
# print(objgetset._value)


#access modifiers in python
#bydefault the variables are public in python. Public variables can be accessed outside the class. Protected variables are accessed within the class and the child class. Private variables are accessed within the class only.
# class Employee:
#     def __init__(self, name, sal):
#         self.__name = name   #double underscore is used to make the variable private. It is used to indicate that the variable is private and should not be accessed directly.
#         self.sal = sal

#     def show(self):
#         print(f"Name is {self.__name} and salary is {self.sal}")

# empobj = Employee('Sagar', 100000)

# # empobj.show()
# # print(empobj.__name)  #this will throw an error as the variable is private and cannot be accessed outside the class.
# print(empobj._Employee__name)  #this is the way to access the private variable outside the class. It is called name mangling.
# print(empobj.__dir__())  #this is used to get the list of the attributes of the object.
# print(empobj.__sizeof__())  #this is used to get the size of the object in bytes.


# class Student:
#     def __init__(self):
#         self._name = "Sagar"  
#     def _funName(self):     
#         return "SagarRathod"

# class Subject(Student):
#     pass

# objstudent = Student()
# objsubject = Subject()

# print(objstudent._name)
# print(objsubject._funName())


#static method in python
#it is used to define the method that does not take the self or cls parameter. It is used to define the method that does not depend on the object or class. It is used to define the utility methods that do not depend on the object or class.

# class Staticmethoddemo :
#     @staticmethod
#     def add(a,b):
#         return a+b

# print(Staticmethoddemo.add(2,3)) 

#instance and class variables in python
# class Employee:
#     classvardemo = 'Sagar is amazing in learning python'   #class variable is used to define the variable that is common to all the objects of the class.
#     def __init__(self, name, sal, company):
#         self.name = name
#         self.sal = sal
#         self.company = company
#     def showdetails(self):
#         print(f"Name is {self.classvardemo}, Salary is {self.sal} and company is {self.company}")
#     print(f"{classvardemo}")
# E1 = Employee('Sagar', 100000, 'TCS')
# E1.classvardemo = 'Sagar is amazing in learning python and he is a good learner'
# E1.showdetails()

#class method in python
# class Employee:   
#     def __init__(self, name, sal, id):
#         self.name = name
#         self.sal = sal
#         self.id = id

#     @classmethod   #can be used as alternative constructor.
#     def splitname(cls, stringvar):
#         return cls(stringvar.split('-')[0], stringvar.split('-')[1], stringvar.split('-')[2])   #parameters must be passed in the same order as the __init__ method.
#     # company = "MasterCard"
#     # def show(self):
#     #     print(f"I work in {self.company}")
#     # @classmethod     #classmethod decorator is used to define the class method. It is used to define the method that takes the cls parameter. It is used to define the method that operates on the class variables.
#     # def changeCompany(cls, newCompany):
#     #     cls.company = newCompany
# e1 = Employee('Sagar', 100000, 123)
# stringvari = "Rakesh-Airoli-sec2-400708"
# empname = Employee.splitname(stringvari)
# print(empname.name)
# emp1 = e1.splitname(stringvar)
# print(emp1)
# print(e1.name)
# print(e1.sal)
# print(e1.id)
# e1.changeCompany("Wipro")
# e1.show()
# print(Employee.company)

# x = 'Sagar'
# print(dir(x))  #dir method is used to get the list of the attributes/methods of the object.
# # print(dir(e1))
# print(x.count('a'))

# class Person:
#     def __init__(self, name, age):
#         self.pname = name
#         self.page = age

# p = Person('Sagar', 28)
# print (p.__dict__)  #__dict__ is used to get the dictionary of the object.

# print(help(p))

#super method in python

# class Parent:
#     def parentmethoddemo(self):
#         print("This is the parent class method called from the child class using the super method")
    
# class Child(Parent):

#     def parentmethoddemo(self):
#         print("This is the child class method")
#     def childmethoddemo(self):
#         print("This is the child class method")
#         super().parentmethoddemo()  #super method is used to call the parent class method.

# c = Child()
# c.childmethoddemo()

# class Employee:
#     count = 0
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):    #repr is for the developers representational purpose & __str__ is for the user readable
        # return f"this method is called from the employee class with variable {self.name}" These are the dunder (double underscore)/magic methods.

    # def __len__(self):    
    #     i = 0 
    #     for c in self.name:
    #         i = i+1
    #     return i

#     def __call__(self):    #makes the object callable and performs the task in it. 
#         self.count += 1
#         return self.count

# objemp = Employee('Sagar')
# print(repr(objemp))
# print(objemp())

#method overriding in python
# class Animal:
#     def speak(self):
#         print("This is the parent class animal method")

# class Dog (Animal):
#     def speak (self):
#         super().speak()
#         return ('Woof woof!')
    
# class Cat (Animal):
#     def speak (self):
#        return ('Meowww')

# dog = Dog()
# cat = Cat()
# print('How the dog sounds', dog.speak())
# print(cat.speak())

#operator overloading in python
class Vector:
    def __init__(self, i , j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return Vector(self.i + x.i,self.j + x.j,self.k + x.k)

v = Vector(1,2,3)
v2 = Vector(6,8,5)
print(v)
print(v2)
print(v + v2)
print(type(v + v2))
