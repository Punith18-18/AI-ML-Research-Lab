from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Preth AI", version="0.1.0")
app.include_router(router)

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}
