from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

sampleList = [
    {
        "name": "Marcy",
        "age": 22
    },
    {
        "name": "Margott",
        "age": 18
    },
    {
        "name": "Mitchell",
        "age": 25
    }
]

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/name')
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "sample name"})

@app.get('/list')
async def name(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "name": "sample name", "sampleList": sampleList})

