from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(redoc_url=None)
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="localhost", port=64436,
                log_level="info", reload=True)