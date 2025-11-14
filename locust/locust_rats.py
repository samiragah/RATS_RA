#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install zope.event


# In[3]:


# locust rats

# locust_rats.py
from locust import HttpUser, task, between

class RATSUser(HttpUser):
    host = "http://localhost:8000"  # تنظیم host درون کلاس
    wait_time = between(1, 3)
    
    @task
    def request_signal_rats(self):
        self.client.post("/request-signal", json={"symbol": "AAPL", "interval": "1h"})


# In[4]:


#locust -f locust_rats.py


# In[ ]:




