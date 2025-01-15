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

class Family:
    mother = "Jayshree"
    father = "Bhanji"
    sister = "Ankita"
    def __init__(self1, n, o):  #self is the reference to the object of the class. It is used to access the variables of the class. __init__ is the constructor of the class. It is used to initialize the object of the class.
        # self1.mother = n
        # self1.father = o
        print(f"My mother's name is {self1.mother} and her husband is {self1.father}")

    # def profession(demoobj):
    #     print(f"Mother's name - {demoobj.mother}, Profession - Housewife")
    #     print(f"Father's name - {demoobj.father}, Profession - Businessman")
    #     print(f"Sister's name - {demoobj.sister}, Profession - Software Engineer")

a = Family('Sagar', 'Developer')  #creating the object of the family class
# b = Family()
# # profession(a) #passing the object of the class to the function
# a.mother = "Mom"
# print(a.mother)
# a.profession()
# print(id(a))

#constructor in python, it is used to initialize the object of the class. It is called automatically when the object is created. It is used to initialize the instance variables of the class.

#decorator in python,
# it is used to modify the behavior of the function or method. It is used to add extra functionality to the function. It is used to wrap the function and modify its behavior

def dec_function(funobj):
    def wrapper():
        print("Good Morning")
        funobj()
        print("Stay tuned")

    return wrapper

@dec_function
def test_fun():
    print("This is a test function")

test_fun()



