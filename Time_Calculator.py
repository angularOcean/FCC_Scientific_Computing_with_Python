print("Time Calculator Project")
import re
import math

def add_time(start, duration, week = None):
    #print('Start', start, 'Duration', duration)
    new_time = None
    start2 = None
    dur2 = None
    newt1 = None
    newt2 = None
    newt3 =  0
    daysweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    startday = None
    endday = None


    start2 = re.split('[: ]',start)
    start2[0] = int(start2[0])
    start2[1] = int(start2[1])
    if re.search('PM', start2[2]) != None:
        start2[0] = int(start2[0] + 12)

    dur2 = re.split('[: ]',duration)
    dur2[0] = int(dur2[0])
    dur2[1] = int(dur2[1])

    newt2 = (start2[1] + dur2[1])%60

    newt1 = start2[0] + dur2[0]+ (start2[1] + dur2[1])//60


    if newt2 <= 9:
        newt2 = str('0')+ str(newt2)
    if newt1 >= 24:
        newt3 = newt1%24
        if newt3 >= 12:
            newt3 = newt3-12
            if newt3 == 0:
                new_time = str(newt3+12) + ':' + str(newt2) + ' PM'
            else:
                new_time = str(newt3) + ':' + str(newt2) + ' PM'
        else:
            if newt3 == 0:
                new_time = str(newt3+12) + ':' + str(newt2) + ' AM'
            else:
                new_time = str(newt3) + ':' + str(newt2) + ' AM'
    if newt1 < 24:
        if newt1 >= 12:
            newt1 = newt1-12
            if newt1 == 0:
                new_time = str(newt1+12) + ':' + str(newt2) + ' PM'
            else:
                new_time = str(newt1) + ':' + str(newt2) + ' PM'
        else:
            if newt1 == 0:
                new_time = str(newt1+12) + ':' + str(newt2) + ' AM'
            else:
                new_time = str(newt1) + ':' + str(newt2) + ' AM'

    if week != None:
        week = week.lower()
        startday = daysweek.index(week)
        if newt1//24 >=1:
            loop = int(startday) + newt1//24
            if loop//7 > 0:
                endday = daysweek[loop%7]
                new_time = new_time + ", " + endday.capitalize()
            else:
                endday = daysweek[loop]
                new_time = new_time + ", " + endday.capitalize()
        else:
            new_time = new_time + ", " + week.capitalize()

    if newt1//24 == 1:
        new_time = new_time + " (next day)"
    if newt1//24 >1:
        new_time = new_time + " (" + str(newt1//24)+ " days later)"






    print('The time is:', new_time)
    return new_time


#add_time("3:30 PM", "2:12")
#print('Expected', "5:42 PM" )

#add_time("11:55 AM", "3:12")
#print('Expected', "3:07 PM")

#add_time("11:40 AM", "0:25")
#print('Expected',"12:05 PM" )

#add_time("11:59 PM", "24:05")
#print('Expected',"12:04 AM (2 days later)")

#add_time("5:01 AM", "0:00")
#print('Expected',"5:01 AM" )

#add_time("3:30 PM", "2:12", "Monday")
#print('Expected', "5:42 PM, Monday")

#add_time("2:59 AM", "24:00", "saturDay")
#print('Expected',"2:59 AM, Sunday (next day)" )

#add_time("11:59 PM", "24:05", "Wednesday")
#print('Expected', "12:04 AM, Friday (2 days later)")

#add_time("8:16 PM", "466:02", "tuesday")
#print('Expected', "6:18 AM, Monday (20 days later)")
