x_speed = 60
y_speed = 90

y_rel_speed = y_speed - x_speed
gap = int(input())
time = 1/(y_rel_speed/gap)*60

print("{:.0f} minutos".format(time))