# library which is going to read out .env file
from dotenv import load_dotenv
import os # to import from local system

# load the .env file
load_dotenv()

# get the value of BASE_URL
BASE_URL = os.getenv("BASE_URL")