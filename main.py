from openai import OpenAI
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


openai = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request:Request):
    return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/")
# async def home():
#     return {"message": "Welcome to the chatbot API! Send a POST request to interact."}

chat_log = [{'role': 'system',
             'content': 'You are a helpful assistant.'}]

chat_responses = []

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request,user_input: Annotated[str, Form()]):

        chat_log.append({'role': 'user', 'content': user_input})
        chat_responses.append(user_input)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
            temperature=0.6
        )

        bot_response = response.choices[0].message.content
        chat_log.append({'role': 'assistant', 'content': bot_response})
        chat_responses.append(bot_response)
        return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})
