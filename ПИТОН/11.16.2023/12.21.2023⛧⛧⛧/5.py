def display_time(hours, minutes, seconds):
    

    if hours > 24:
        measege = "время неправильно"
    if minutes or seconds > 60:
        measege = "время неправильно"

    if hours < 10:
        hours = str(hours)
        hours = "0" + hours
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
    if seconds < 10:
        seconds = str(seconds)
        seconds = "0" + seconds
    
    template = '%s:%s:%s'
    measege = template % (hours, minutes, seconds)
    return measege
    

print(display_time(12, 36, 4))