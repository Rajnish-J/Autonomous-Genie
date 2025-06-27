import os
import subprocess   
import tempfile
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from Prompts.playwrightPrompts import playwright_prompt

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

os.environ["GOOGLE_API_KEY"] = API_KEY

# Load Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20", temperature=0.2)

# Chain: Prompt → LLM → Output
chain = playwright_prompt | llm | StrOutputParser()

class TestGeneratorService:
    @staticmethod
    def generate_code(user_story: str) -> str:
        return chain.invoke({"user_story": user_story})

    @staticmethod
    def run_code(playwright_code: str):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as f:
            f.write(playwright_code)
            f.flush()
            subprocess.run(["python", f.name], check=False)
