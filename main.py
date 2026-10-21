from fastapi import FastAPI

app = FastAPI(title="Cloud Deployment Lab")


@app.get("/")
def home():
    return {"message": "My first API is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}