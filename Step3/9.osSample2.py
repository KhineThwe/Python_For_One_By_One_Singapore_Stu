import os
os.chdir('/Users/khine/Desktop/')
# print(os.getcwd())
# print(os.listdir())

# os.makedirs('OS-Demo-2/Sub-Dir-1')
os.chdir('/Users/khine/Desktop/OS-Demo-2/')
print(os.listdir())

# Parent Directory path
parent_dir = "/Users/Khine/"

# Directory
directory = "Desktop/OS-Sample/"

# Path
path = os.path.join(parent_dir, directory)

print("Path: ",path)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir('/Users/khine/Desktop/OS-Demo-Sample/')

# os.mkdir('/OS-Demo-3/Sub-Dir-2/')
print(os.getcwd())
#for deleting folder


