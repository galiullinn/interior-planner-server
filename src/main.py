from fastapi import FastAPI

app = FastAPI(
    title="Interior Planner API",
)


@app.get("/")
async def root() -> dict:
    return {"message": "Interior Planner API"}
