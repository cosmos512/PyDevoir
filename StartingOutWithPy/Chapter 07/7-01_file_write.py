# This program writes three lines of data
# to a file.
def main():
    # Open a file named animalsounds.txt.
    outfile = open('animalsounds.txt', 'w')

    # Write the sounds of three animals
    # to the file.
    outfile.write('Moo.\n')
    outfile.write('Woof.\n')
    outfile.write('Meow.\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()
