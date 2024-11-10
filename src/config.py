from os import getenv
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class GlobalSettings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    BACKEND_PORT: int = int(getenv('BACKEND_PORT', 8080))
    BACKEND_HOST: str = str(getenv('BACKEND_HOST', "localhost"))    

global_settings = GlobalSettings()