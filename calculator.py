
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
op = str(input("Enter operator (+, -, *, /) "))

#round of answer to 2 decimals
roundof = 2

if (op == "+"): 
    sum = x+y
    print(f"{x} {op} {y} = {round(sum, roundof)}")
   
elif (op == "-"): 
    sum = x-y
    print(f"{x} {op} {y} = {round(sum, roundof)}")

elif (op == "*"): 
    sum = x*y
    print(f"{x} {op} {y} = {round(sum, roundof)}")
    
elif (op == "/"):
    sum = x/y
    print(f"{x} {op} {y} = {round(sum, 2)}")
    

else:
    print("Invalid operator")





