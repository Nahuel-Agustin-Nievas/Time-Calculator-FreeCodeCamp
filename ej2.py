def add_time (start, duration, day_week= False):

    weekdays_index= {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6

    }
    
     
    
    
    weekdays_arr = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    #start format separation
    time1= start.split()[0]
    pmam1= start.split()[1]
    hour1 = int(time1.split(":")[0])
    minute1 = int(time1.split(":")[1])

    # print(time1)
    # print(pmam1)
    # print(hour1)
    # print(minute1)

    if pmam1 == "PM":
        hour1 += 12

   # duration format separation
    hour2 = int(duration.split(":")[0])
    minute2 = int(duration.split(":")[1])
    # print(hour2)
    # print(minute2)


    #calculations
    total_minutes = minute1 + minute2 
    final_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour1 + hour2 + extra_hours
    # print(total_minutes)
    # print(total_hour)
    

    
    
    final_hour = (total_hour % 24) % 12
    


    #hour 0
    if final_hour == 0:
        final_hour = 12
        final_hour = str(final_hour)

    #calculating days
    total_day= (total_hour // 24)
    # total_day = int (hour2 // 24)
    
    

    # deciding mid day (AM/PM)
    ampm_final = ""
    if (total_hour % 24) <= 11:
        ampm_final = "AM"
    else:
        ampm_final = "PM"
 
    #minutes under 10
    if final_minutes <=9:
        final_minutes = "0" + str(final_minutes)

    
    

    new_time = str(final_hour) + ":" + str(final_minutes) + " " + ampm_final
    
    if(day_week):
         day_week = day_week.lower()
         index = int((weekdays_index[day_week]) + total_day) % 7
         new_day = weekdays_arr[index]
         new_time += ", " + new_day

    if(total_day == 1):
       return new_time + " " + "(next day)"
    elif (total_day > 1):
         return new_time + " (" + str(total_day) + " days later)"

    
    return new_time
    