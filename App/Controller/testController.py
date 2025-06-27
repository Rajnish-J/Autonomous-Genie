from Service.testGeneratorService import TestGeneratorService
from Models.userStoryModels import UserStoryInput

def generate_test_from_user_story(data: UserStoryInput) -> str:
    print("Generating code from user story...\n")
    code = TestGeneratorService.generate_code(data.user_story)

    print("\n--- Generated Playwright Code ---\n")
    print(code)

    if data.run_code:
        print("\nRunning the generated Playwright test...\n")
        TestGeneratorService.run_code(code)

    return code
