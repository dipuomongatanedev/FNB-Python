kilometers = int(input("please enter the amount of kilometers you want to drive"))
price_perliter=float(input("what is the current petrol price per litre"))

liters_needed=kilometers / 10
total_cost=liters_needed * price_perliter

print(f"the final cost is: {round(total_cost,2)}")