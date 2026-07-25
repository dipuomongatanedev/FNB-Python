
num1 = float(input("please enter the first number"))
num2 = float(input("please enter the second number"))
#addition
print(f"addition: {round(num1 + num2,2)}")
#subtraction
print(f"subtraction:{round(num1-num2,2)}")
#multiplication
print(f"multiplication:{round(num1*num2,2)}")
#divison and handle division by 0

if num2==0:
   print("not divisible by 0")

else:print(f"division:{round(num1/num2,2)}")
      
#floor divisom
print(f"floor division:{round(num1//num2,2)}")
#modulus
print(f"modulus: {round(num1%num2,2)}")





