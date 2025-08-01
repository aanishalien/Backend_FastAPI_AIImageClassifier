import os
from dotenv import load_dotenv
from supabase import create_client,Client
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from supabase import create_client, client

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)