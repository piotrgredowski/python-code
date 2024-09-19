"""Simple FastAPI application for demo purposes."""

import fastapi

app = fastapi.FastAPI()


@app.get("/")
def hello(name: str = "World"):
    import random

    return f"Hello, {name}! {random.random()}"  # noqa: S311
