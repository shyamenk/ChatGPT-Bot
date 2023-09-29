from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = FastAPI()

openai.organization = os.getenv("OPEN_AI_ORG")
openai.api_key = os.getenv("OPEN_AI_API_KEY")


@app.get("/")
def read():
    return {"Message": "Welcome to Fast API!"}


@app.post("/talk")
def post_audio(file: UploadFile):
    audio_file = open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
