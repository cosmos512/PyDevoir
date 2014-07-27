# This program reads and displays the contents
# of the animalsounds.txt file.
def main():
    # Open a file named animalsounds.txt.
    infile = open('animalsounds.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(file_contents)

# Call the main function.
main()
