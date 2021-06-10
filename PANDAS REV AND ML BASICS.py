#!/usr/bin/env python
# coding: utf-8

# # Pandas Fundementals

# In[1]:


import pandas as pd


# In[2]:


#1ST--->SERIES
#2ND--->DATAFRAME
haga=pd.Series([1,2,3,4,5,6,7,8,9,10])


# In[3]:


haga


# In[70]:


boys=["Biswa","Rahul","Pati","BAKA","Kelto","Rajesh"]
girls=["Ankita","Rashmi","Sneha","Konkona","Tinni","Rubai"]
hizras=["Soumen","Arup","Asu","Vaja","Ayush","Bere"]
ziplist=list(zip(boys,girls,hizras))
df=pd.DataFrame(data=ziplist,columns=['Boys','Girls','Hizras'])


# In[18]:


df#Creating A Dataframe


# In[20]:


ziplist


# In[22]:


df2=pd.DataFrame({"Boys":boys,"Girls":girls,"Hizras":hizras})#Another Process of Create DataFrame
df2


# In[23]:


df


# In[24]:


df2


# In[26]:


pd.concat([df,df2],axis=0)#Vertical Concat


# In[27]:


pd.concat([df,df2],axis=1)#Horizontally Concat


# In[34]:


df.drop(["Boys"],axis=1)#Drop "Boys" Column


# In[35]:


loadDataset=pd.read_csv("salaries.csv")


# In[36]:


loadDataset


# In[37]:


loadDataset=pd.read_csv("weather_data.csv")


# In[38]:


loadDataset


# # DataFrame Slicing

# In[41]:


df


# In[44]:


df.iloc[2:5]


# In[46]:


df.iloc[:,2]


# In[53]:


df.iloc[2:5,0:2]


# In[54]:


df.loc[[1,2,3,4]]


# In[55]:


loadDataset


# In[57]:


loadDataset[4:]


# In[61]:


loadDataset.loc[[1,4]]


# In[62]:


df


# In[72]:


df.drop(["Hizras"],axis=1,inplace=True)


# In[73]:


df


# # GROUPING DATAFRAME

# In[74]:


loadDataset


# In[75]:


berepok=loadDataset.groupby("event")


# In[76]:


berepok


# In[77]:


for temperature in berepok:
    print(temperature)


# # APPLY FUNCTION

# In[78]:


def hot_temp(x):
    return x>30
loadDataset["hot_temp"]=loadDataset['temperature'].apply(hot_temp)


# In[79]:


loadDataset


# In[80]:


loadDataset.describe()


# # MERGING DATAFRAMES

# In[82]:


df


# In[83]:


df2


# In[84]:


MergeDataset=pd.merge(df,df2,on=['Girls'],how='outer')


# In[85]:


MergeDataset


# In[86]:


phone_no=['6290272740','8295742180','7278000101','7278000102','8583939774','9748385553']


# In[87]:


names=['Biswa','Rahul','Soumen1','Soumen2','Ankita','MILI']


# In[88]:


table1data=list(zip(phone_no,names))


# In[90]:


address=['SaltLake','Newtown','Jhopra','Bosti','Hanapara','USA']


# In[92]:


table2data=list(zip(phone_no,address))


# In[103]:


dataframe1=pd.DataFrame(data=table1data,columns=["Phone_no","Name"])
dataframe2=pd.DataFrame(data=table2data,columns=["Phone_no","Address"])


# In[104]:


dataframe1


# In[131]:


dataframe2


# In[108]:


mergeDataframe=pd.merge(dataframe1,dataframe2,on=['Phone_no'])


# In[109]:


mergeDataframe


# In[110]:


dataframe1


# In[113]:


dataframe1['FATHER']=['Tarak','Goutam','Nunu','Nunu','Achin','Mr.Monojit']


# In[114]:


dataframe1


# In[129]:


mergeDataframe=pd.merge(dataframe1,dataframe2,on=['Phone_no'],how='left')


# In[130]:


mergeDataframe


# # PIVOT TABLE

# In[132]:


loadDataset


# In[133]:


loadDataset.pivot_table(values='temperature',index='event',aggfunc='mean')


# In[135]:


loadDataset.pivot_table(columns='temperature')


# In[137]:


help(pd.DataFrame.pivot_table)


# # PANDAS FINISH --- HAPPY CODING

# # NOW DECESSION TREE CLASSIFICATION IN ML CREATE SKLEARN MODEL

# In[138]:


#THEORITICAL PART IN ML
#ML------->1.SUPERVISED LEARNING
#          2.UNSUPERVISED LEARNING
#SUPERVISED----->TEACHER NEEDED#CLASSIFY
#USUPERVISED---->TEACHER NOT REQUIRED#CLUSTERRING
#REINFORCEMENT-->TEACHER NOT REQUIRED#SELF-IMPROVEMENT
#SML(CLASSIFICATION)-->KNN,DECESSION TREE,NAIVE BAYES etc.


# # Salaries Prediction

# In[139]:


dataset=pd.read_csv("salaries.csv")


# In[140]:


dataset


# In[141]:


from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
de_degree=LabelEncoder()


# In[145]:


inputs=dataset.drop('salary_more_than_100k',axis='columns')


# In[146]:


inputs


# In[147]:


target=dataset['salary_more_than_100k']


# In[148]:


target


# In[150]:


inputs


# In[151]:


inputs['encode_company']=le_company.fit_transform(inputs['company'])
inputs['encode_job']=le_job.fit_transform(inputs['job'])
inputs['encode_degree']=de_degree.fit_transform(inputs['degree'])


# In[152]:


inputs


# In[153]:


encode_inputs=inputs.drop(["company","job","degree"],axis="columns")


# In[154]:


encode_inputs


# In[155]:


target


# In[157]:


from sklearn import tree
model=tree.DecisionTreeClassifier()


# In[158]:


model.fit(encode_inputs,target)


# In[162]:


accuracy=model.score(encode_inputs,target)*100
print("Accuracy : ",accuracy,"%")


# In[172]:


d=0
c=0
p=0
degree=input("ENTER YOUR DEGREE : ")
company=input("ENTER YOUR COMPANY : ")
post=input("ENTER YOUR DESIGNATION : ")
if degree.lower()=="bachelors" and post.lower()=="sales executive" and company.lower()=="google":
    d=0
    p=2
    c=2
elif degree.lower()=="bachelors"  and post.lower()=="business manager" and company.lower()=="google":
    d=0
    c=2
    p=0
elif degree.lower()=="bachelors"  and post.lower()=="computer programmer" and company.lower()=="google":
    d=0
    c=2
    p=1
elif degree.lower()=="masters"  and post.lower()=="business manager" and company.lower()=="google":
    d=1
    c=2
    p=0
elif degree.lower()=="masters"  and post.lower()=="sales executive" and company.lower()=="google":
    d=1
    c=2
    p=2
elif degree.lower()=="masters"  and post.lower()=="computer programmer" and company.lower()=="google":
    d=1
    c=2
    p=1
#-------------------->bachelors,masters in google
elif degree.lower()=="bachelors" and post.lower()=="sales executive" and company.lower()=="facebook":
    d=0
    p=2
    c=1
elif degree.lower()=="bachelors"  and post.lower()=="business manager" and company.lower()=="facebook":
    d=0
    c=1
    p=0
elif degree.lower()=="bachelors"  and post.lower=="computer programmer" and company.lower()=="facebook":
    d=0
    c=1
    p=1
elif degree.lower()=="masters"  and post.lower=="business manager" and company.lower()=="facebook":
    d=1
    c=1
    p=0
elif degree.lower()=="masters"  and post.lower=="sales executive" and company.lower()=="facebook":
    d=1
    c=1
    p=2
elif degree.lower()=="masters"  and post.lower=="computer programmer" and company.lower()=="facebook":
    d=1
    c=1
    p=1
#-------------------->bachelors,masters in facebook
elif degree.lower()=="bachelors" and post.lower()=="sales executive" and company.lower()=="abc pharma":
    d=0
    p=2
    c=0
elif degree.lower()=="bachelors"  and post.lower()=="business manager" and company.lower()=="abc pharma":
    d=0
    c=1
    p=0
elif degree.lower()=="bachelors"  and post.lower()=="computer programmer" and company.lower()=="abc pharma":
    d=0
    c=0
    p=1
elif degree.lower()=="masters"  and post.lowe()=="business manager" and company.lower()=="abc pharma":
    d=1
    c=0
    p=0
elif degree.lower()=="masters"  and post.lower()=="sales executive" and company.lower()=="abc pharma":
    d=1
    c=0
    p=2
elif degree.lower()=="masters"  and post.lower()=="computer programmer" and company.lower()=="abc pharma":
    d=1
    c=0
    p=1
#-------------------->bachelors,masters in abcpharma
strr=model.predict([[c,p,d]])
if int(strr)==1:
    print("SALARY MORE THAN 100K")
elif int(strr)==0:
    print("SALARY IS NOT MORE THAN 100K")


# # ML BASICS FINISHED --- HAPPY CODING

# In[ ]:




