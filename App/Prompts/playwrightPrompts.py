from langchain_core.prompts import ChatPromptTemplate

playwright_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a senior QA automation engineer. Generate Playwright code (Python) "
     "to perform the actions described. Use Chromium. Output only the complete code."),
    ("user", "{user_story}")
])
