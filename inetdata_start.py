import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.co.uk")
    print("Result code: " + str(webUrl.getcode()))

if __name__ == "__main__":
    main()