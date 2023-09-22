#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('python --version')


# In[2]:


get_ipython().system('pwd')


# In[3]:


get_ipython().system('ls')


# In[4]:


get_ipython().system('ls -al')


# In[5]:


get_ipython().system('cat test.dat')


# In[18]:


fread = None
try : 
    fread = open('test.dat', 'r')
    #result = fread.read()
    #result = fread.readline()   #초기값
    #while result :
    #    print(result, end='')
    #    result = fread.readline()
    for line in fread.readlines(): 
        print(line, end='')
except : 
    print('File Not Found')
finally : 
    fread.close()


# In[19]:


poet = """
죽는 날까지 하늘을 우르러
한점 부끄럼이 없기를、
잎새에 이는 바람에도
나는 괴로워했다。
별을 노래하는 마음으로
모든 죽어가는것을 사랑해야지
그리고 나한테 주어진 길을
거러가야겠다。

오늘밤에도 별이 바람에 스치운다。
"""


# In[20]:


fwrite = None
try:
    fwrite = open('서시.txt', 'w')
    fwrite.write(poet)
    print("File Save Successfully.")
except Exception as err:
    print(err)
finally : 
    fwrite.close()


# In[22]:


with open('서시.txt', 'rt') as fread : 
    try: 
        count = 1
        for line in fread.readlines() : 
            print(f'{count} : {line}', end='')
            count += 1
    except : 
        print('File Not Found')


# In[23]:


import json


# In[24]:


list_ = ['Hello, world', 5, True, 89.5]
type(list_)


# In[25]:


str_ = json.dumps(list_)
type(str_)


# In[26]:


print(str_)


# In[27]:


obj = json.loads(str_)
type(obj)


# In[28]:


obj[2]


# In[38]:


student = {
    "hakbun" : "2023-003",
    "name" : "한지민", 
    "age" : 24,
    "address" : "서울시 강남구 역삼동"
}
type(student)


# In[39]:


str_ = json.dumps(student, ensure_ascii=False, indent='\t')
type(str_)
print(str_)


# In[40]:


with open('student.dat', 'wt') as fwrite :
    fwrite.write(str_)
    print("File Save Successfully.")


# In[41]:


with open("student.dat", "rt") as fread : 
    result = fread.read()
    #print(type(result))
    obj = json.loads(result)
    #print(type(obj))
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[45]:


with open('sungjuk.json', 'rt') as fread:
    result = json.load(fread)    # load = read() -> loads()
    #print(type(result))     #list
    #print(len(result))
    #print(type(result[0]))   #dict
    print(result[0]['irum'])


# In[46]:


import os
print(os.name)


# In[47]:


print(os.getcwd())


# In[48]:


get_ipython().system('pwd')


# In[49]:


os.chdir('/')
print(os.getcwd())


# In[50]:


import sys


# In[54]:


print(f"Version : {sys.version}")
print(f"Version Info : {sys.version_info}")
print(f"Platform : {sys.platform}")


# In[55]:


import platform


# In[58]:


print(f"Platform Architecture : {platform.uname()}")


# In[59]:


import socket


# In[60]:


print(f"Host name : {socket.gethostname()}")


# In[61]:


hostname = socket.gethostname()
print(socket.gethostbyname(hostname))


# In[62]:


print(socket.gethostbyname('www.google.com'))


# In[63]:


print(os.system("ls"))


# In[68]:


print(os.getcwd())


# In[67]:


os.chdir("/home/ubuntu")


# In[72]:


#print(os.system("date"))
import subprocess


# In[75]:


subprocess.run(["ls", "-a"])


# In[76]:


get_ipython().system('pip list')


# In[77]:


get_ipython().system('pip install pymysql')


# In[ ]:


get_ipython().system('pip install nbconvert')

