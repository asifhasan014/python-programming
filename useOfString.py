first_name="Asif"
last_name="Hasan"
full_name=first_name+last_name
print(full_name)
full_name=first_name+" "+last_name
print(full_name)
first_name="Asif"
last_name=" Hasan"
full_name=first_name+last_name
print(full_name)

#print(full_name+3) error
print(full_name+str(3))
full_name = full_name+" "
print(full_name*3)

#String formatting
name,age = "Asif Hasan Talukder", 30
print("your name is "+name+" and your age is "+str(age))
print("your name is {} and your age is {}".format(name,age))
print(f"your name is {name} and your age is {age}")

#String slicing with soap argument
name = "python"
print("positive index "+name[1:4])
print("positive index "+"python"[1:4])
print("positive index "+name[1:])
print("positive index "+name[:6])
print("negetive index "+name[-4:6])

#String slicing with step argument
print("step argument positive index "+"python"[0:6:2])
print("string reverse "+"python"[-1::-1])

