def convert_seconds(seconds):
    #makes sure that seconds are within the bounds of a day
    if seconds < 0 or seconds > 86400:
        return "Not a valid input"
    #converts seconds to hours
    seconds_to_hours = seconds // 3600
    #converts to the remainder then the remainder is the leftover seconds after you get the hours
    seconds_to_minutes = (seconds % 3600)//60
    # gives what ever is left over after all the other seconds have been converted to either hours or minutes
    seconds_to_seconds = seconds % 60
    #makes sure that if hours are less than 12, then it's AM
    if seconds_to_hours < 12:
        time_period = "AM"
    else:
        time_period = "PM"
        #converts the hours into the 12-hour format
    seconds_to_hours = seconds_to_hours % 12
    return str(seconds_to_hours) + " " + str(seconds_to_minutes) + " " + str(seconds_to_seconds) + " " + str(time_period)
print(convert_seconds(67434))


