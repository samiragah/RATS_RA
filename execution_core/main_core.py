#!/usr/bin/env python
# coding: utf-8

# ## RATS Main core

# In[1]:


# main_core

from pydantic import BaseModel
from fastapi import FastAPI
import random
import uvicorn
import threading
import asyncio

# calling fatsAPI
app = FastAPI()

class SignalRequest(BaseModel):
    symbol: str          # trading symbol
    interval: str        # time frame

@app.post("/generate-signal")
async def generate_signal(data: SignalRequest):
    processing_time = random.uniform(0.1, 0.5)      # ms
    await asyncio.sleep(processing_time)
    
    #-- signal execution
    signal = "BUY" if random.random() > 0.5 else "SELL"    
    return {
        "signal": signal,
        "latency_ms": round(processing_time * 1000, 2),
        "component": "Execution Core"
    }

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8001)

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
print("Execution Core running on http://127.0.0.1:8001")


# In[ ]:




