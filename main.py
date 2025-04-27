from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello ":"World"}

@app.get("/hello")
def main():
    return  {"Hello" : "from fastapi-project!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
