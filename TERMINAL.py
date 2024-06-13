import REMINDER as REM

try:
    print(" -- UMBERLLA REMINDER ON EMAIL -- ")
    print(" -- PRESS ctrl+C to exit / stop running -- ")

    CITY: str = str(input("CITY NAME: "))
    TIME: str = str(input("TIME: "))

    REM.Schedule_Notification(TIME, CITY)

except KeyboardInterrupt:
    print(" -- EXITED -- ")