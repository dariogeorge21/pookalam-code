# Program to display unique ASCII characters from a file

# Initialize an empty list to store unique ASCII characters
unique_ascii_chars = []

# File path
file_path = "pookalam.txt"

try:
    # Open the file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the file content
        content = file.read()
        
        # Iterate through each character in the content
        for char in content:
            # Check if the character is not already in the list
            if char not in unique_ascii_chars:
                # Add the character to the list
                unique_ascii_chars.append(char)
    
    # Print the list of unique ASCII characters
    print("Unique ASCII characters:")
    print(unique_ascii_chars)
    # Display the count of unique ASCII characters
    print(f"Count of unique ASCII characters: {len(unique_ascii_chars)}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")