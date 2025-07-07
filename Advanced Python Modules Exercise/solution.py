import shutil
import os
import re

# Unzip the file to this dir
shutil.unpack_archive('Advanced Python Modules Exercise/unzip_me_for_instructions.zip', 'Advanced Python Modules Exercise')
# Create regex object once. Better performance than recreating it n times in proceeding loop
phone_re = re.compile(r'\d{3}-\d{3}-\d{4}', re.ASCII)
# Read content of each file and check for matching pattern
for root, dirs, files in os.walk('Advanced Python Modules Exercise/extracted_content'):
    for file in files:
        path = os.path.join(root, file)
        content = open(path).read()
        if phone_re.search(content) is not None:
            print(path)
            # Found the file, no need to continue running
            exit()