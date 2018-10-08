def howManySundays(n, startDay):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    d = days.index(startDay)
    return (d + n) // 7


print(howManySundays(6, 'Monday'))
