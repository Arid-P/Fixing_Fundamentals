import os
from dotenv import load_dotenv

load_dotenv()
print(f"{os.getenv("TEST_SECRET") = }")
print(f"{os.getenv("GITHUB_TOKEN") = }")
