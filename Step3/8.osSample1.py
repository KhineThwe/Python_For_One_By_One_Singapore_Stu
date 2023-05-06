import os

def current_path():
    print("Current Working Directory Before: ")
    print(os.getcwd())

if __name__ == '__main__':
    current_path()

    #Changing the CWD
    os.chdir('../')

    #print CWD after
    current_path()