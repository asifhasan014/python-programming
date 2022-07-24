# f = open('file1.txt')
#oprn different directory 
# f = open(r"D:\myfile\file1.txt")

# print(f.read())
# f.close()

#file read with bock
# with open('file1.txt') as f:
#     data = f.read()
#     print(data)

# with open('file2.txt','w') as f:
#     f.write("Hello Asif")
# print("Data is written")

# with open('file2.txt','a') as f:
#     f.write("\nHello Adib")
# print("Data append")

#Read and write at a time
with open('file1.txt','r') as rf:
    with open('file3.txt','a') as wf:
        wf.write(rf.read())