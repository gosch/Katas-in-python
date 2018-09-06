def validTime(time):
    return (0 >= int(time[0]+time[1]) < 25) and (0 >= int(time[3]+time[4]) < 60)


print(validTime('13:58'))
