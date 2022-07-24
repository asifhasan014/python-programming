# f = open('file1.txt')
#oprn different directory 
# f = open(r"D:\myfile\file1.txt")

# print(f.read())
# f.close()

#file read with bock
with open('file1.txt') as f:
    data = f.read()
    print(data)
