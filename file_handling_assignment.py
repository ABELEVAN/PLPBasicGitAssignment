# file_handling_assignment.py

# File Creation: Create and write to "my_file.txt"
try:
    # Open the file in write mode ('w') to create it and write initial content
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 12345.\n")
        file.write("Line 3 is here with more text.\n")
    print("File created and written successfully.")

except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display: Read and display the content of "my_file.txt"
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nReading file content:")
        print(content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending: Open "my_file.txt" in append mode and add more content
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 4 to the file.\n")
        file.write("Line 5 with a number: 67890.\n")
        file.write("This is line 6, appended to the file.\n")
    print("\nContent appended successfully.")

    # Read the file again to show the appended content
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nUpdated file content after appending:")
        print(content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to write to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

finally:
    print("\nScript execution completed.")
