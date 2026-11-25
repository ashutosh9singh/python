days=int(input("enter the number of days: "))
years=days//365
new_days=days%365
weeks=new_days//7
days=new_days%7
print(f"the number of year is {years} and weeks is {weeks} and days is {days}")
