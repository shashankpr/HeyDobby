import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WIT_TOKEN = os.environ.get("WIT_TOKEN")
