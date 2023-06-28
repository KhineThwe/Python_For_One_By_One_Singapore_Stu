def process_file(filename):
    try:
        file = open(filename,"r")

        content = file.read()

        file.close()

        words = content.split()
        word_count = len(words)
        print("Word Count: ",word_count)
    except FileNotFoundError:
        print("Error: File Not Found")
    except IOError:
        print("Error: An I/O error occurred.")
    except Exception as e:
        print("An err ocurred: ",str(e))

if __name__ == '__main__':
    try:
        filename = input("Enter the filename")

        process_file(filename)

    except KeyboardInterrupt:
        print("Process Interrupted By The user.")
    except Exception as e:
        print("An error occurred: ",str(e))