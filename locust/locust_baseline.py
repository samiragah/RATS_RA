#!/usr/bin/env python
# coding: utf-8

# In[1]:


# locust_baseline
# this is for base line testing with Locust

from locust import HttpUser, task, between

class MonolithicUser(HttpUser):
    host = "http://localhost:8002"  # ← پورت baseline
    wait_time = between(1, 3)
    
    @task
    def request_signal_mono(self):
        self.client.post("/request-signal-mono", json={"symbol": "AAPL", "interval": "1h"})


# In[ ]:




