import time

def timestamp(func):
    def wrapper():
        time_date = time.ctime()
        print(time_date)
        func()
    return wrapper