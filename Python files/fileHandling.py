# Step 1: Write to a file
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")

# Step 2: Read from the file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content read from {filename}:\n{content}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Step 3: Append to the file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Content appended to {filename}")

# Step 4: Main function to execute the steps
def main():
    filename = 'example.txt'
    
    # Writing initial content to the file
    initial_content = "Hello, Abdullah Here!\n"
    write_to_file(filename, initial_content)
    
    # Reading the content from the file
    read_from_file(filename)
    
    # Appending new content to the file
    additional_content = "Welcome to file handling this is testing.\n"
    append_to_file(filename, additional_content)
    
    # Reading the content again to see the changes
    read_from_file(filename)

if __name__ == "__main__":
    main()
