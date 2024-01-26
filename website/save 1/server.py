from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from pprint import pprint

import util

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
    text: str

@app.get("/")
async def main():
    content = open("templates/index.html", "r").read()
    return HTMLResponse(content=content)


@app.post("/process")
async def process_text(item: Item):
    text = item.text
    result = util.cut_text(text)
    keys = {"test1":["hello", "world"], "test2":["hello"], "test3":["world"]}
    print(text)
    print(keys)
    return {"result": text, "keys": keys}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8082)