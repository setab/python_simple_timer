import time


def timer(t):
    while t:
        mints, secs = divmod(t, 60)
        countdown = '{:02d}:{:02d}'.format(mints, secs)

        time.sleep(1)
        print(countdown, end="\r")
        t -= 1
    print("times up")


t = int(input("please inter time in seconds :"))
timer(t)

