# Open the file in read mode
with open("plan3 without.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        line = line.strip("\n")   # remove only the newline at end
        # join characters with space
        spaced_line = " ".join(line)
        print(spaced_line)
