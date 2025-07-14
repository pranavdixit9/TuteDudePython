## task_1.py

**Functionality:**  
This script reads and prints the content of a specified text file line by line.

- The program defines a function `read_file(filename)` that:
  - Attempts to open the file in read mode.
  - Prints each line of the file after stripping trailing whitespace.
  - Handles `FileNotFoundError` if the file does not exist.
  - Handles any other unexpected errors during file reading.


## task_2.py

**Functionality:**  
This script interacts with the user to write and append text to a file, then displays the final file content.

- First, it prompts the user to enter some text to write to a file named `output.txt`. This overwrites any existing content.
- Next, it prompts the user to enter additional text to append to the same file.
- Finally, it reads and prints the entire content of `output.txt` to show the combined result.
