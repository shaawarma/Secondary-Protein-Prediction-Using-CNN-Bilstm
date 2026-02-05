from src.config import WINDOW_SIZE
import os

print(WINDOW_SIZE)


print(os.getcwd())          # where Python thinks your project root is
print(os.listdir())        # what folders it sees here
print(os.path.exists("data/"))  # should be True
