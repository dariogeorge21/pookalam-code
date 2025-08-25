def count_characters_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            character_count = len(content)
            print(f"The number of characters in the file is: {character_count}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'plan3 without.txt' with the actual path to your file
file_path = 'plan3 without.txt'
count_characters_in_file(file_path)