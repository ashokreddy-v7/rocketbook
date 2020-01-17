num1 = int(input("enter an integer= "))
print(num1)

if(num1 < 0):
    num1 = abs(num1)
    print("-ve sign removed",num1)
elif(num1==0):
    print("Invalid. "+ str(num1) +"is not integer")
else:
    print("Valid number",num1)