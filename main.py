from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hasdfasdjfello World232342qwer4312413qwqeqeqe"}
