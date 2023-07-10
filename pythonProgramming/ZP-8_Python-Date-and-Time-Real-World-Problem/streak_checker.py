from datetime import timedelta
from datetime import datetime
import time
streak = 0
last_checkin = datetime(day=9, month=7, year=2023)

def update_streak(last_checkin, streak):
    msg = ""
    current_checkin = datetime.now()
    # print("(current_checkin - last_checkin).days >> ",(current_checkin - last_checkin).days)
    if ((current_checkin - last_checkin).days) > 0:
        msg = "streak has broken!!!"
        last_checkin = current_checkin
        sreak = 0
    elif current_checkin.month == last_checkin.month and current_checkin.day != last_checkin.day:
        streak += 1
        msg = "streak has updated!!"
    return last_checkin,streak,msg


rslt = update_streak(last_checkin, streak)
streak = rslt[1]
last_checkin = rslt[0]
msg =rslt[2]
print(rslt,streak,msg)