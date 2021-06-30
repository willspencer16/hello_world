
def main():
    # Opening a file for writing and creating one if it doesn't exist:
    f = open("textfile.txt", "w+")
    # The open function takes two arguements. The first is the file to
    # operate on and the second is the kind of access you want. The 'w'
    # is requesting writing access to the 'textfile.txt' file and the
    # '+' creates the file if it doesn't already exist.

if __name__ == "__main__":
    main()