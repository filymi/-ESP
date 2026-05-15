" Вся логика API. Тут будет очень много!!! "

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK"}