#writing to a file
try:
    file = open("output.txt", "w")  # Open file in write mode
    file.write("Hey there, i am using whatsapp")  # Write data to the file
    print("Data written to file successfully.")
    file.close()  # Close the file
except:
    print("Error: Failed to write to file.")

#appending to a file
try:
    file = open("output.txt", "a")  # Open file in append mode
    file.write("\nHello AKA.")  # Append data to the file
    print("Data appended to file successfully.")
    file.close()  # Close the file
except:
    print("Error: Failed to append to file.")

#reading line by line
try:
    file = open("output.txt", "r")  # Open file in read mode
    lines = file.readlines()  # Read all lines of the file into a list
    print("File lines:")
    for line in lines:
        print(line.strip())  # Print each line after removing trailing newline characters
    file.close()  # Close the file
except FileNotFoundError:
    print("Error: File not found.")

#read file
try:
    file = open("output.txt", "r")
    data = file.read()
    print("File content:", data)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")