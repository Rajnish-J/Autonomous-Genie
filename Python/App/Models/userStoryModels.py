from pydantic import BaseModel

class UserStoryInput(BaseModel):
    user_story: str
    run_code: bool = False
