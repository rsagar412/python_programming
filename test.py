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
import sys

setdemo = {1,2,3,4,5,6,7,8,9,10}
setdemo2 = {4,5,6,78,98,99}
# vardemo = "Sagar"
# emptyset = set()
# print(setdemo)
# print(str(sys.getsizeof(setdemo))+"bytes")
# print(sys.getsizeof(vardemo), type(setdemo), type(emptyset))
# for i in setdemo:
#     print(i)
#set methods
print(setdemo.union(setdemo2))    #prints the union of two sets excluding the duplicate values.
print("This method will update the set1 with the values that present in set2", setdemo.update(setdemo2))
print(setdemo, setdemo2)
print(setdemo.intersection(setdemo2))  #prints the common values in the two sets
print(setdemo.intersection_update(setdemo2))  #prints the common values in the two sets 
print(setdemo)
print(setdemo.update("1,2,3,4"))
print(setdemo)
setdemo.discard('22')   #remove and discard methods to remove one item from the set and discard can be used to ignore the error if the item is not present in the set.
print(setdemo)
del setdemo  #deletes the entire set and clear () method is used to clear the set values.
setdemo = {1,2,3,4,5,6,7,8,9,10}
print(setdemo)