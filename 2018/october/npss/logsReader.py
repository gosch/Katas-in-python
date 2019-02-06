import re

def check_is_date(column):
    exp1 = re.compile(r"\d{4,} \d{2,}:\d{2,}:\d{2,}")
    exp2 = re.compile(r"\w{3,} \w{3,} \d{2,} \d{2,}:\d{2,}:\d{2,} \d{4,}")
    r1 = exp1.match(column.strip())
    r2 = exp2.match(column.strip())
    return r1 or r2

logfile = open(r'210073327.log.csv', mode='rt', encoding='utf-8')
# print(logfile.read())

rows = []
rows2 = []

for line in logfile:
    column_line = 32 * [""]
    data = {}
    for ind, column in enumerate(line.strip().split(",")):
        column_line[ind] = column
        if ind == 0:
            data['SSO'] = column
        if ind == 1:
            data['Tool'] = column

        if check_is_date(column):
            data['Date'] = column

    rows.append(column_line)
    rows2.append(data)

print(rows[0])


counter_dict = {}
# for column in rows:
#     if column[1] not in counter_dict:
#         counter_dict[column[1]] = 1
#     else:
#         counter_dict[column[1]] += 1
# counter = 0
# for key in counter_dict.keys():
#     print(key + " = " + str(counter_dict[key]))

for row in rows2:
    print('SSO ' + row['SSO'] + 'Tool ' + row['Tool'] + 'Date ' + data['Date'] )

print(len(rows2))
