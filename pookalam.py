with open("pookalam.txt", "r") as file:
    for line in file:
        line = line.strip("\n")  
        spaced_line = " ".join(line)
        print(spaced_line)
