
def main():
    # Opening a file for writing and creating one if it doesn't exist:
    # f = open("textfile.txt", "w+")
    # The open function takes two arguments. The first is the file to
    # operate on and the second is the kind of access you want. The 'w'
    # is requesting writing access to the 'textfile.txt' file and the
    # '+' creates the file if it doesn't already exist.

    # Opening the file for appending text to the end:
    f = open("textfile.txt", "r")
    # The a argument appends the end of the file, instead
    # of overwriting everything that is already in the file.

    # Writing some lines of code to the file:
    # for i in range(10):
    #     f.write("This is line" + str(i) + "\r\n")
        # The write function writes data to the file.
    
    # Closing the file:
    # f.close()

    # Opening the file and reading the contents:
    if f.mode == 'r': # This checks the file can be read.
        # contents = f.read() # This reads the content.
        # print(contents) # This prints the contents to the console.
        fl = f.readlines()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()