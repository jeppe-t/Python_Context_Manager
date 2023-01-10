#Context manager

"""

A context manager is a concept, that takes care of related task. The important thing here is the order of execution.

A context manager gives us control, so the execution order is the same every time. This is very useful, when working
with databases or files.

The below example shows a content manager in action working with files. It takes care of opening the file, then
we do something with the file, read/write or similar and then closes the file.

"""

from datetime import datetime
from colorama import Fore, Style
print(Fore.GREEN + "\n3. Context manager" + Style.RESET_ALL)


#Example 1 - Own class implementation.
class FileManager:

    def __init__(self, filename, file_option):
        self.filename = filename
        self.file_option = file_option

    def __enter__(self):
        print('file __enter__')
        fil = open(self.filename, self.file_option)
        return fil

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('file __exit__\n')
        f.close()


#The 'with' keyword looks for an enter and exit method

print("\nExample 1 - Own class implementation")

with FileManager('logfile.txt', 'w') as f:
    f.write(f"There was a login attempt {datetime.now()}")
    print("Login attempt")

with FileManager('logfile.txt', 'r') as f:
    print(f.readline())



#Example 2 - using build-in-libraries.
from contextlib import contextmanager

@contextmanager
def generator():
    fil = open('logfile.txt')
    yield fil
    fil.close()


print("\nExample 2 - using build-in-libraries")

with generator() as y:
    print(y.readline(),'\nThis is a generator created by library')
