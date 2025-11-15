from dotenv import load_dotenv
import os

load_dotenv()  # reads .env file into environment

print("TINKER_API_KEY present:", bool(os.getenv("TINKER_API_KEY")))