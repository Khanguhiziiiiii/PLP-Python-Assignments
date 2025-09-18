# File Read & Write Challenge

try:
    # Open the input file in read mode
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File has been read and modified version saved in 'output.txt'.")

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")



# Error Handling Lab

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content successfully read:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
