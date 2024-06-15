from fastapi import FastAPI
from transformers import pipeline

##create a new FastApi app instance

app=FastAPI()

# Initialize the text generation pipeline

pipe=pipeline("text2text-generation", model="google/flan-t5-small")

@app.get('/')
def home():
    return {"message":"Hello world"}

#define a function to handle the Get request '/generate'

@app.get("/generate")
def generate(text:str):
    ## use the pipeline to generate text from the given input text
    output=pipe(text)

    ##return the generated text
    return{"output":output[0]['generated_text']}