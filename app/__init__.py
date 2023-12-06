from flask import Flask
from config import openai_api_key

app = Flask(__name__)
openai_api_key = openai_api_key
