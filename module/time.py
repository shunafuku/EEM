import datetime

def now_datetime() -> str:
    now = datetime.datetime.now()
    remove_microsec: str = now.strftime("%Y-%m-%d %H:%M:%S")
    return remove_microsec