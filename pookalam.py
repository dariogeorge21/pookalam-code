# Open the file in read mode
with open("pookalam.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        line = line.strip("\n")   # remove only the newline at end
        # join characters with space
        spaced_line = " ".join(line)
        print(spaced_line)
