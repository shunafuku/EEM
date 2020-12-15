import datetime

def get_time():
    now = datetime.datetime.now()
    now_time = (str(now.year)
                + "-"
                + str(now.month)
                + "-"
                + str(now.day)
                + " "
                + str(now.hour)
                + ":"
                + str(now.minute)
                + ":"
                + str(now.second))
    return now_time