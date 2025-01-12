
st = "this is a string"
# print(st.split(" "))  
words = st.split(" ")     #this line will split the string into words and store it in the list
# coding = True  #this is a boolean variable
nwords = [] 
# print(type(nwords))  #output will be list
# if (coding): 
    # print("Condition is true, This is the coding block")
for word in words:
    if(len(word) > 3):  
            r1='dft'
            r2='ere'           
            newwords = r1+ word[1:]+word[0] + r2   #if the length of the string is greater than 3, then the first character of the string will be moved and appended to the end of the string. Random characters to the string.
            nwords.append(newwords)
print(nwords)           
print(" ".join(nwords))