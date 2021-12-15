#"Time Calculator Project" by HL
import re

def add_time(start, duration, week = None):
    '''This function calculates the the end time given a start time and duration and optionally the day of the week the end time is on
    Parameters: a string of the start time in 12 hour clock format HH:MM with an AM or PM formatted ending. a duration in hours and minutes, an optional argument for the day of the week
    Returns: the ending time in 12 hour clock format and AM/PM for the end time along with how many days later it is and optionally a day of the week if the third argument is given   '''
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

