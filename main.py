from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)


@app.get("/")
async def read_root():
    return {"message": "Hello, World!",
            "docs": "/docs",
            "health": "/health"}


@app.get("/health")
async def health_check():
    return {"status": "healthy",
            "service": "My FastAPI Application"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0", 
        port=8000,
        reload=True
    )