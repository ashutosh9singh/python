sec=int(input("enter time in seconds: "))
hr=sec//3600
remaining_sec=sec%3600
minutes=remaining_sec//60
seconds=remaining_sec%60
print(f"time is {hr} hour {minutes} minutes {seconds} seconds")
