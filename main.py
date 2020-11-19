import uvicorn
from typing import Optional
from fastapi import FastAPI
from starlette.responses import Response, JSONResponse

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
