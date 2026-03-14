print("No Hello for you!!")
print("ones")
print("twice")

from dotenv import load_dotenv
import os
def print_author():
	load_dotenv(dotenv_path='.env')
	author = os.getenv('AUTHOR')
	print(author)
print_author()
