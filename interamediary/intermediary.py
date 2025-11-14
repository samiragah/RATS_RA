#!/usr/bin/env python
# coding: utf-8

# In[1]:


# intermediary

from fastapi import FastAPI
import httpx
import uvicorn
import threading

app = FastAPI()

@app.post("/request-signal")
async def request_signal(data: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:8001/generate-signal", 
                json=data, 
                timeout=10.0
            )
            return response.json()
        except Exception as e:
            return {"error": str(e), "component": "Intermediary"}

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# اجرای سرور در thread جداگانه
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
print(" Intermediary Service running on http://127.0.0.1:8000")


# In[ ]:




