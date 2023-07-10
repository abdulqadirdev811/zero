from datetime import timedelta, datetime
"""
The reviews of the buisness on the google looks like this 
# an hour ago
# a day
# a month ago
# an year ago

we want to convert it to the datetime format
"""


def convert_google_reviews(time_str):
    current_time = datetime.today()
    num_to_subtract = time_str.split()[0]
    if "a" in num_to_subtract:
        num_to_subtract = 1
    else:
        num_to_subtract = int(num_to_subtract)

    if "day" in time_str:
        current_time = datetime(day=current_time.day - num_to_subtract,
                                year=current_time.year, month=current_time.month)
    elif "month" in time_str:
        current_time = datetime(
            day=current_time.day, year=current_time.year, month=current_time.month - num_to_subtract)
        pass
    elif "year" in time_str:
        current_time = datetime(
            day=current_time.day, year=current_time.year - num_to_subtract, month=current_time.month)
        pass

    return current_time

rslt = convert_google_reviews("3 years ago")
print(rslt)
