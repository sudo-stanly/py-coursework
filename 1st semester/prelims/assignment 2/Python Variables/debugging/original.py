import time
import datetime
from datetime import datetime, timedelta

day = int(input("Enter day/s: "))
def lab_func(num_of_days):
    #y = datetime.now() - timedelta(days - num_of_days) #! -> days is not defined
    y = datetime.now() - timedelta(num_of_days)
    t = datetime.now()
    if y < t:
        print("No")
    else:
        print("Yes")
        
    return lab_func

lab_func(day)    