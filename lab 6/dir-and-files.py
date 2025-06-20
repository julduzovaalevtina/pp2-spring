#1
import os

path = os.getcwd()

dirs = []
files = []

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_dir():
            dirs.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)

print('Directories:')
for d in dirs:
    print(' ', d)

print('\nFiles:')
for f in files:
    print(' ', f)

print('\nAll entries:')
for item in dirs + files:
    print(' ', item)


#2
import os

path = os.getcwd()

print(os.access(path, mode=os.R_OK), 
      os.access(path, mode=os.W_OK), 
      os.access(path, mode=os.X_OK),
      os.access(path, mode=os.EX_OK))

#3
import os

path = os.getcwd()

print(os.access(path, mode=os.R_OK), 
      os.access(path, mode=os.W_OK), 
      os.access(path, mode=os.X_OK),
      os.access(path, mode=os.EX_OK))

#4
with open('test.txt') as text:
    print(len(list(text)))

#5
with open('test.txt', 'w') as text:
    lst = [input() for _ in range(10 ** 6)]
    
    for i in lst:
        text.write(f'{i}\n')
        
#6
import string

for i in string.ascii_uppercase:
    open(f'{i}.txt', 'w')
    

#7
with open('test.txt') as file:
    file_for_copy = file.read()
    
    file_to_copy = open('test2.txt', 'w')
    file_to_copy.write(file_for_copy)
    
    file_to_copy.close()

#8
import os

path = ''

if os.access(path, mode=os.EX_OK):
    os.remove(path)