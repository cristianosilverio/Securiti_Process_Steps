#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import json


# In[3]:


import os


# In[4]:


import csv


# # API Authorization

# ## Reading config file

# In[5]:


with open('tenant.cfg','r') as api_file:
    api_config = csv.reader(api_file)
    type(api_config)
    api_config = list(csv.reader(api_file))


# ## Setting API HTTP Header

# In[6]:


if api_config[1][0] == 'X-TIDENT':
    X_TIDENT = api_config[1][1]
else:
    print('Erro: Parâmetro não reconhecido - X-TIDENT')


# In[7]:


if api_config[2][0] == 'X-API-KEY':
    X_API_KEY = api_config[2][1]
else:
    print('Erro: Parâmetro não reconhecido - X-API-KEY')


# In[8]:


if api_config[3][0] == 'X-API-SECRET':
    X_API_SECRET = api_config[3][1]
else:
    print('Erro: Parâmetro não reconhecido - X-API-SECRET')


# In[9]:


http_header = {
    'X-TIDENT':X_TIDENT,
    'X-API-KEY':X_API_KEY,
    'X-API-SECRET':X_API_SECRET
}


# # Get Process list

# ## Retrieve process list

# In[10]:


url_processes = "https://app.securiti.ai/privaci/v1/admin/data_map/process"


# In[11]:


payload_processes = {}


# In[12]:


processes = requests.request("GET", url_processes, headers=http_header, data=payload_processes)


# ## Save process id and name

# In[19]:


with open('processes.tmp','w',newline='') as process_file:
    editor = csv.writer(process_file,delimiter=';')
    editor.writerow(('Process id','Process name'))
    counter = 0
    for p in processes.json()['data']:
        process_id = processes.json()['data'][counter]['id']
        process_name = processes.json()['data'][counter]['name']  
        editor.writerow((process_id,process_name))
        counter = counter + 1


# In[ ]:




