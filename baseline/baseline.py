#!/usr/bin/env python
# coding: utf-8

# In[1]:


# baseline 

from fastapi import FastAPI
import random
import time
import uvicorn
import threading

app = FastAPI()

@app.post("/request-signal-mono")
async def request_signal_mono(data: dict):
    processing_time = random.uniform(0.1, 0.5)
    time.sleep(processing_time)
    
    signal = "BUY" if random.random() > 0.5 else "SELL"
    return {
        "signal": signal,
        "latency_ms": round(processing_time * 1000, 2),
        "component": "Monolithic"
    }

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8002)

# اجرای سرور در thread جداگانه
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
print(" Monolithic Baseline running on http://127.0.0.1:8002")


# In[ ]:




