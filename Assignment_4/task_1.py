def read_file(filename):
    try:
        print("Reading file content:")
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = 'sample.txt'

read_file(file_name)