bill_amount = int(input("How much was your bill?"))
service = input("How was your service?").lower()
if service == "good":
    tip=(bill_amount*0.20)

elif service == "fair":
    tip=(bill_amount*0.15)

elif service == "bad":
    tip=(bill_amount*0.10)
else:
    print("find a new resturant")

print(f"Your total bill was $ {bill_amount+ tip}" )