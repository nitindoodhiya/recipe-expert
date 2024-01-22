from typing import Union

from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.cors import CORSMiddleware
from deepgram import DeepgramClient, PrerecordedOptions 
from transcribe import Transcribe
from recipe import getInstructions
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/process_url")
async def process_url(request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        if not url:
            raise HTTPException(status_code=400, detail="URL not provided in the request body")
        transcribe = Transcribe()
        transcript = Transcribe.transcribe(transcribe, url)
        response = await getInstructions(transcript)
        return {"response": response}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

