from fastapi import FastAPI

app = FastAPI(title="Cloud Deployment Lab")


@app.get("/")
def home():
    return {"message": "My cloud deployment pipeline is working!"}

@app.get("/health")
def health():
    return {"status": "ok"}