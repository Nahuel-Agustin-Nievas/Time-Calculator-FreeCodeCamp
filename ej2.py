# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM



# def addtime (a):

#     hour1= int(a.split(":")[0])
#     minute1= int(a.split(":")[1])
#     # hour2= b.split(":")[0]
#     # hour2= b.split(":")[1]
    
#     print(hour1)
#     print(type(hour1))
#     print(minute1)

#     print(hora1)

 




def add_time (start, duration):
    # start = "3:50 pm"

    #start format separation
    time1= start.split()[0]
    pmam1= start.split()[1]
    hour1 = int(time1.split(":")[0])
    minute1 = int(time1.split(":")[1])

    print(time1)
    print(pmam1)
    print(hour1)
    print(minute1)

   # duration format separation

    hour2 = int(duration.split(":")[0])
    minute2 = int(duration.split(":")[1])
    print(hour2)
    print(minute2)


    
    total_minutes = minute1 + minute2 
    print(total_minutes)
    final_minutes = total_minutes % 60
    print(final_minutes)
    extra_hours = total_minutes // 60
    print(extra_hours)
    total_hour = hour1 + hour2 + extra_hours
    print(total_hour)
    # final_hour = hour1 + hour2
    # final_minute= minute1 + minute2
    # print(final_hour)
    # print(final_minute)

    # final_result = str(final_hour) + ":" + str(final_minute) + " " +pmam1
    # print(final_result)
    # print(type(final_result))
    
    final_hour = (total_hour % 24) % 12

    # if final_hour == 0:
    #     final_hour = 12
    #     final_hour = str(final_hour)

    if final_minutes <=9:
        final_minutes = "0" + str(final_minutes)

    new_time = str(final_hour) + ":" + str(final_minutes) + " " + pmam1
    print(new_time)
    

# add_time("3:00 PM", "3:10")

add_time("11:55 AM", "3:12")



