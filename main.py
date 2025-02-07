def info_time(time1, time2):
    h1, m1 = list(map(int, time1.split(":")))
    h2, m2 = list(map(int, time2.split(":")))
    h = h1 + h2 + (m1 + m2) // 60
    m = (m1 + m2) % 60
    time = {"time":"", "count_am_pm":0, "count_day":0}
    time["count_am_pm"] = h//12
    h = h % 12
    time["time"] = str(h) + ":" + (str(m) if m > 9 else "0"+str(m))
    return time

def add_time(start, duration, day = None):
    start, am_pm = start.split()
    new_time = info_time(start, duration)
    if new_time['count_am_pm'] % 2 != 0:
        am_pm = "PM" if am_pm == "AM" else "AM"
    if new_time['time'] != '12:00' or new_time['time'] != '12:00':
        new_time['time'] += " " + am_pm
    result = new_time['time']
    print(new_time)
    return

add_time('3:00 PM', '3:09') 
