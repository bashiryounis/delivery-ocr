import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

load_dotenv(verbose=True)

class Config(BaseSettings):
    GOOGLE_API_KEY:str = Field(env="GOOGLE_API_KEY")
    MAIN_DIR: str = Field(env="MAIN_DIR",default="/app/main_dir")
    GENERATIVE_MODEL:str = Field(default="gemini-1.5-pro")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config = Config()
