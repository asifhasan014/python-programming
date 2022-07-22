print("list programming")
array = [1,2,3,4,5,6]
array2 =["abc","xyz","123"]
array3 =[1,2,3,4,5,6,"abc","xyz","123"]

print(array)
print(array2)
print(array3)
print(array[3])
print(array2[:1])
print(array3[:-1])
print(array3[-1])

#list comprehension
square = []
for i in range(1,11):
    square.append(i**2)
print(square)
square2 = [i**2 for i in range(1,11)]
print(f"second list: {square2}")
# print("second list "+ str(square2))
new_list2 = [i*2 if (i%2 == 0) else -i for i in range(1,11)]
print(f"new_list2: {new_list2}")