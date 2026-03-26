with open('file.txt' , 'r') as read:
   content = read.readline()
   reversed(content)
   with open('file.txt' , 'w') as write:
       for line in reversed(content):
        write.write(line)

