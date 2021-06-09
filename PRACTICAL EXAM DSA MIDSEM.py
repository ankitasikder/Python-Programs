#!/usr/bin/env python
# coding: utf-8

# In[1]:


b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print("The decimal value of the number is", value)


# In[ ]:





# In[3]:


# Remove Negative Elements in List 
n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
test_list = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
print("The original list is : " + str(test_list)) 
res = [ele for ele in test_list if ele > 0] 
print("List after filtering : " + str(res))


# In[1]:


#LONGEST COMMON SUBSEQUENCES
def Lcs(str1,str2,lenstr1,lenstr2):
    if lenstr1 == 0 or lenstr2 == 0: 
       return 0; 
    elif str1[lenstr1-1] == str2[lenstr2-1]: 
       return 1 + Lcs(str1, str2, lenstr1-1, lenstr2-1); 
    else: 
       return max(Lcs(str1, str2, lenstr1, lenstr2-1), Lcs(str1, str2, lenstr1-1, lenstr2));
a = input()
b = input()
result =Lcs(a, b,len(a),len(b))
print(result)


# romi
# imu
# 
# 
# 
# 
