from transformers import pipeline# Use a pipeline as a high-level helper
from fastapi import FastAPI



app = FastAPI()

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message":"Hello World"}


@app.get("generate")
def generate(text:str):
    output = pipe(text)

    return {"output":output[0]['generated_text']}

