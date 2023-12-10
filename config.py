from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
API_HASH = getenv('API_HASH')
API_ID =  int(getenv('API_ID'))
