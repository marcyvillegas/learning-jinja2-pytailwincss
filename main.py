from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from models.sign_up import SignUp

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

sampleList = [
    {"name": "Marcy", "age": 22},
    {"name": "Margott", "age": 18},
    {"name": "Mitchell", "age": 25},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/name")
async def name(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "name": "sample name"}
    )


@app.get("/list")
async def list(request: Request):
    return templates.TemplateResponse(
        "list.html",
        {"request": request, "name": "sample name", "sampleList": sampleList},
    )


@app.get("/redirect/to/{page_name}")
async def get_param(request: Request, page_name: str):
    return templates.TemplateResponse(
        "param.html", {"request": request, "page_name": page_name}
    )


@app.get("/parent")  # from /templates/form
async def parent(request: Request):
    return templates.TemplateResponse("parent.html", {"request": request})


@app.get("/child_1")
async def child_1(request: Request):
    return templates.TemplateResponse("child1.html", {"request": request})


@app.get("/sample_macro")
async def form(request: Request):
    return templates.TemplateResponse("sample_macro.html", {"request": request})


@app.get("/form")
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/submit")
async def successful_submit(request: Request, cat_name: str = Form(...)):
    return templates.TemplateResponse(
        "successful_form.html", {"request": request, "result": cat_name}
    )


@app.get("/form_2")  # from /templates/form
async def form_2(request: Request):
    return templates.TemplateResponse("form_2.html", {"request": request})


@app.get("/get_countries")
async def ajax_get(request: Request):
    return templates.TemplateResponse("get_countries.html", {"request": request})


@app.get("/navigation")
async def navigation(request: Request):
    return templates.TemplateResponse("navigation.html", {"request": request})


@app.get("/users")
async def get_users():
    return sampleList


@app.post("/submit_form_2")
async def submit_form_2(data: SignUp) -> SignUp:
    print(data)

    # the data variable will be returned by the controller, where the database manipulation will happen
    #  data = await controller.process( arguments here )
    return data
