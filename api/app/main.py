from fastapi import FastAPI

app = FastAPI(title="Audit log service")

@app.get("/health")
async def health():
    return {"status":"ok"}