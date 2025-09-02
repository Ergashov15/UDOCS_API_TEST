import os
from dotenv import load_dotenv

load_dotenv()

TOKENS = {
    "default": os.getenv("TOKEN")
}
if not TOKENS["default"]:
    raise EnvironmentError("Default TOKEN environment variable is missing or not loaded correctly!")

#################################### URL


BASE_URL = {
    "default": os.getenv("BASE_URL")
}
if not BASE_URL:
    raise ValueError("BASE_URL environment variable is missing or not loaded correctly!")


####################################
