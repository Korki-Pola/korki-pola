with open('textfile.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())
