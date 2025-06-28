from Models.userStoryModels import UserStoryInput
from Controller.testController import generate_test_from_user_story

if __name__ == "__main__":
    input_data = UserStoryInput(
        user_story="""
        Go to https://example.com/login.
        Fill in the email as "test@example.com" and password as "Test1234".
        Click the login button.
        Wait for dashboard to appear.
        """,
        run_code=False
    )

    generate_test_from_user_story(input_data)
