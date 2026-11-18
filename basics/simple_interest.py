principal_amt=float(input("enter principla amount: "))
rate=float(input("enter rate per year: "))
time=float(input("enter time in years: "))

#simple intrest calculation 
si=(principal_amt*rate*time)/100

#total returning amount
total=principal_amt+si

print(f"the total intrest is:{si:.2f}")
print(f"the total amount is: {total:.2f}")
