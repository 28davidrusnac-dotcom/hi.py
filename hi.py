a=float(input("enter first number"))
b=float(input("enter second number"))

print("""
Choose an operation:
+ addition
- Substraction
* Multiplication
/ Division
** Exponent
// Integer division
%Remainder
""")

op= input("operation:")

if op=="+":
    result=a+b

elif op== "-":
    result= a-b
elif op== "*":
    result= a*b
elif op== "/":
    if b==0:
        print("Division by zero is not allowed.")
        exit()
    result= a/b
elif op== "**":
    result=a**b

elif op== "//":
    result= a//b

elif op== "%":
    result= a%b

else:
    print("invalid operation.")


print(f"result: {result}")
