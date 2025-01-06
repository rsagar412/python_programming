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

#reverse a string
strex = "Sagar" [::-1] 
print(strex)