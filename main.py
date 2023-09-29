from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def index():
    return {"Detail":"Welcome to QDA"}