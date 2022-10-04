# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
import datetime


def addtime (a,b):

    hour1 = a.split("")[0]
    minute1= a.split("")[2]
    hour2= b.split("")[0]
    hour2= b.split("")[2]
    
    print(hour1)

    hora1 = datetime.datetime(hour=hour1, minute=minute1)
    print(hora1)




addtime("3:00 PM", "3:10")

