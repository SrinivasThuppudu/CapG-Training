# Writing to file
file = open("Day8/sample.txt", "w")
file.write("Hello, This is a sample file")
print("File created successfully")
file.close()

# Writing again using 'with' statement
with open("Day8/sample.txt", "w") as file:
    file.write("Hello, This is a sample file")
    print("File created successfully")

# Reading the file
with open("Day8/sample.txt", "r") as file:
    content = file.read()
    print(content)

# Corrected append and read operation
with open("Day8/sample.txt", "r") as file:  # Open in 'r' mode instead of 'a'
    for line in file:
        print(line.strip())
