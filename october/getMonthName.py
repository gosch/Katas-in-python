
def getMonthName(mo):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months[mo-1] if mo > 0 and mo< 13 else 'invalid month'

print(getMonthName(7))
