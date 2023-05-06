import os
import datetime
os.chdir('/Users/khine/Desktop/OS-Demo-1/Sub-Dir-1')
# os.makedirs('OS-Demo-1/Sub-Dir-1')

print(os.listdir())

# source = '/Users/khine/Desktop/OS-Demo-1/Sub-Dir-1/demo.txt'

# destination file path
dest = '/Users/khine/Desktop/OS-Demo-1/Sub-Dir-1/demo-1.txt'

# os.rename(source,dest)
# print(os.listdir())

print(os.stat(dest).st_size)
