from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello ":"World"}

@app.get('/greet')
async def greet_name(name: str) -> dict:
    return {"Message":f"Hello World : {name}"}



@app.get("/hello")
def main():
    return  {"Hello" : "from fastapi-project!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
