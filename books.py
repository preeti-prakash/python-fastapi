from fastapi import FastAPI

app = FastAPI()         #allows uvicorn to identify that we are creating a web app of fastapi

@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Preeti"}
