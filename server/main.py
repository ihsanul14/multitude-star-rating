from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config
from framework.delivery import HttpDelivery

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,         
    allow_methods=["*"],            
    allow_headers=["*"],            
)
HttpDelivery(app).delivery_http()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(config('PORT')))