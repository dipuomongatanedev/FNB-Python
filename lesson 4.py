#atm withdrawer 

bank_balance= 500 
withdrawal=float(input("how much money would you like to withdraw?"))

if withdrawal<=500:
    print("withdrawal successful")
elif withdrawal<=0:
    print("invalid amount, you must withdraw more than R0")

else:
    print("declined, insufficient funds")
