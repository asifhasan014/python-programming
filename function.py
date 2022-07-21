# def add_two_number(num1, num2):
#     return num1+num2

# a= int(input("input your first number: "))
# b= int(input("input your first number: "))

# total=add_two_number(a,b)

# print("sum of two number is: "+ str(total))
# print(f"sum of two number is: {total}")

#Function Inside function

def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    return greater(greater(a,b),c)

print(greatest(100,150,95))