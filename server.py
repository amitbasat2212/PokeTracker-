from urllib import response
from fastapi import FastAPI

app = FastAPI()

import uvicorn

import pokimonsRoute
import trainerRoute

app.include_router(pokimonsRoute.router)
app.include_router(trainerRoute.router)


if __name__ == "__main__":
     uvicorn.run("server:app", host="0.0.0.0", port=8080,reload=True)
