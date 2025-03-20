
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
op = str(input("Enter operator (+, -, *, /) "))

if (op == "+"): 
    sum = x+y
    print(f"{x} {op} {y} = {round(sum, 2)}") #round(sum, 2) rounds of to two decimals
   
elif (op == "-"): 
    sum = x-y
    print(f"{x} {op} {y} = {round(sum, 2)}")

elif (op == "*"): 
    sum = x*y
    print(f"{x} {op} {y} = {round(sum, 2)}")
    
elif (op == "/"):
    sum = x/y
    print(f"{x} {op} {y} = {round(sum, 2)}")
    

else:
    print("Invalid operator")



