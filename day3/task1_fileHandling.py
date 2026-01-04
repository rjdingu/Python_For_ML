
f_read = open('day3/names.txt','r')
for index, line in enumerate(f_read, start=1):
                print(f"Line {index}: {line.rstrip()}")
        
f_read.close()





