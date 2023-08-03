from fastapi import FastAPI, Response

# I like to launch directly and not use the standard FastAPI startup
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello_text/{name}")
async def say_hello_text(name: str):
    the_message =  f"Hello {name}"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
