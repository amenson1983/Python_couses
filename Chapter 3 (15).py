seconds = float(input("Put seconds here:"))
day = seconds//86400
day_rest = seconds%86400
hour = day_rest//3600
hour_rest = day_rest%3600
min = hour_rest//60
min_rest = hour_rest%60
print(day, "days")
print(hour, "hours")
print(min, "minutes")
print(min_rest, "seconds")


