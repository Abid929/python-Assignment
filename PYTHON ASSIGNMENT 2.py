#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=float(input("Enter Marks in English :\t"))
b=float(input("Enter Marks in Maths: \t"))
c=float(input("Enter Marks in Physics: \t"))
d=float(input("Enter Marks in Chemistry: \t"))
e=float(input("Enter Marks in Computer Science: \t"))
avg=((a+b+c+d+e)/500)*100
if(avg>=80):
    
 print("Congratulations ! You have secured A grade, and your percentage is ", avg)
elif(avg>=60 and avg<80):
 print("Congratulations ! You have secured B garde your percentage is ", avg )
elif (avg>=40 and avg<60):
   print("Congratulations ! You have secured C grade, and your percentage is ", avg)
elif (avg<40):
 print( "You are fail")


# In[3]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[4]:


test_list = [ 1, 1, 2, 3, 5,8,13,21,34,55,89 ] 
  

print ("The list is : " + str(test_list))


# In[5]:


total = 0
  
 
list1 = [1, 1, 2, 3, 5,8,13,21,34,55,89,]  
  

for ele in range(0, len(list1)): 
    total = total + list1[ele] 
  

print("Sum of all elements in given list: ", total)


# In[8]:


lst = [1, 1, 2, 3, 5,8,13,21,34,55,89,102]   
print("Largest element is:",max(lst))



# In[9]:


array=[1, 1, 2, 3, 5,8,13,21,34,55,89]
a=array[:4]
print(a)

