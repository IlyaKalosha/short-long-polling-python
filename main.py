import asyncio

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import time
from typing import Dict
import uvicorn


app = FastAPI()

data_store = {"status": "pending", "message": "Waiting for completion"}


@app.get("/short_poll")
async def short_poll() -> dict[str, str]:
    if data_store["status"] != "completed":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found")
    return data_store


@app.get("/long_poll")
async def long_poll() -> dict[str, str]:
    timeout = 60
    start_time = time.time()

    while True:
        if data_store["status"] == "completed":
            return data_store

        if time.time() - start_time > timeout:
            return data_store

        await asyncio.sleep(1)


@app.post("/update_status")
async def update_status(status: str, message: str):
    if status not in ["pending", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    data_store["status"] = status
    data_store["message"] = message
    return JSONResponse(content={"detail": "Status updated successfully"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
