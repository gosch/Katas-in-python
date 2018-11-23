import re
import csv
import calendar
y = ""
m = ""
ctotal = calendar


def check_is_date(d):
    exp1 = re.compile(r"\d{8,8}.+\d{1,2}:\d{2,2}:\d{2,2}")
    exp2 = re.compile(r"\w{3,3} \w{3,3}.+\d{1,2}.+ \d{1,2}:\d{2,2}:\d{2,2}.*")
    exp3 = re.compile(r"\d{4,4} \d{2,2} \d{2,2}.+\d{1,2}:\d{2,2}:\d{2,2}.*")
    r1 = exp1.match(d.strip())
    r2 = exp2.match(d.strip())
    r3 = exp3.match(d.strip())
    global y
    global m
    if r1:
        y = d[:4]
        m = d[4:6]
    elif r3:
        y = d[:4]
        m = d[6:8]
    elif r2:
        y = d[20:]
        m = d[4:7]
        for i, name in enumerate(ctotal.month_abbr):
            if name == m:
                m = str(i)
    return r1 or r2 or r3


# Report 1: userid,wks,count,yyyy,mm
def report1(month_list, log_data):
    for month in month_list:
        with open('r1_UserID_Script_Count_2018_' + month + '.csv', mode='w+', newline='') as csv_file:
            fieldnames = ['UserID', 'Script', 'Count', 'Year', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for sso, sso_value in log_data.items():
                if month in sso_value:
                    for script, count in sso_value[month].items():
                        writer.writerow({'UserID': sso, 'Script': script, 'Count': count, 'Month': month, 'Year': '2018'})


# Report 2: userid,all,count,yyyy,mm
def report2(month_list, log_data):
    for month in month_list:
        with open('r2_UserID_allScripts_Count_2018_' + month + '.csv', mode='w+', newline='') as csv_file:
            fieldnames = ['UserID', 'Script', 'Count', 'Year', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for sso, sso_value in log_data.items():
                counter = 0
                if month in sso_value:
                    for scripts_counter in sso_value[month].values():
                        counter += scripts_counter
                writer.writerow({'UserID': sso, 'Script': 'all', 'Count': counter, 'Month': month, 'Year': '2018'})


# Report 3: all,wks,count,yyyy,mm
def report3(months, log_data):
    for month in months:
        with open('r3_allUserID_allScript_Count_2018_' + month + '.csv', mode='w+', newline='') as csv_file:
            fieldnames = ['UserID', 'Script', 'Count', 'Year', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            script_data = {}
            for user_data in log_data.values():
                if month in user_data:
                    for script, count in user_data[month].items():
                        if script in script_data:
                            script_data[script] += count
                        else:
                            script_data[script] = count
            for script, count in script_data.items():
                writer.writerow({'UserID': 'all', 'Script': script, 'Count': count, 'Month': month, 'Year': '2018'})


# Report 4: all,npssRun,105201,2018,9
def report4(months, log_data_csv_dict):
    for month in months:
        with open('r4_allUserID_npssRun_Count_2018_' + month + '.csv', mode='w+', newline='') as csv_file:
            fieldnames = ['UserID', 'Script', 'Count', 'Year', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            counter = 0
            for row in log_data_csv_dict.values():
                if row['Month'] == month:
                    if row['Script'] == 'npssRun':
                        counter += 1
            writer.writerow({'UserID': 'all', 'Script': 'npssRun', 'Count': counter, 'Month': month, 'Year': '2018'})


# Report 5: userid,wks,count,yyyy,13
def report5(log_data):
    with open('r5_UserID_Script_Count_2018.csv', mode='w+', newline='') as csv_file:
        fieldnames = ['UserID', 'Script', 'Count', 'Year']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for user, user_data in log_data.items():
            script_data = {}

            for month_data in user_data.values():
                for script, count in month_data.items():
                    if script in script_data:
                        script_data[script] += count
                    else:
                        script_data[script] = count
            for script, count in script_data.items():
                writer.writerow({'UserID': user, 'Script': script, 'Count': count, 'Year': '2018'})


# Report 6:
def report6(log_data):
    with open('r6_UserID_allScripts_Count_2018.csv', mode='w+', newline='') as csv_file:
        fieldnames = ['UserID', 'Script', 'Count', 'Year']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for sso, sso_value in log_data.items():
            counter = 0
            for month_value in sso_value.values():
                for scripts_counter in month_value.values():
                    counter += scripts_counter
            writer.writerow({'UserID': sso, 'Script': 'all', 'Count': counter, 'Year': '2018'})


# Report 7: all,wks,count,yyyy
def report7(log_data):

    with open('r7_allUserID_allScript_Count_2018.csv', mode='w+', newline='') as csv_file:
        fieldnames = ['UserID', 'Script', 'Count', 'Year', 'Month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        script_data = {}
        for user_data in log_data.values():
            for month_data in user_data.values():
                for script, count in month_data.items():
                    if script in script_data:
                        script_data[script] += count
                    else:
                        script_data[script] = count
        for script, count in script_data.items():
            writer.writerow({'UserID': 'all', 'Script': script, 'Count': count, 'Year': '2018'})


# Report 8: all,npssRun,105201,2018,9
def report8(log_data_csv_dict):

    with open('r8_allUserID_npssRun_Count_2018.csv', mode='w+', newline='') as csv_file:
        fieldnames = ['UserID', 'Script', 'Count', 'Year']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        counter = 0
        for row in log_data_csv_dict.values():
            for month_data in row.values():
                counter += month_data['npssRun']
        writer.writerow({'UserID': 'all', 'Script': 'npssRun', 'Count': counter, 'Year': '2018'})


csvArr = []
csvDict = {}

logfile = open(r'210073327.log.csv', mode='rt', encoding='utf-8')
for i, line in enumerate(logfile):
    column_line = 32 * [""]
    data = {}
    year = {}
    month = {}
    for ind, column in enumerate(line.strip().split(",")):
        column_line[ind] = column
        if ind == 0:
            data['SSO'] = column
        if ind == 1:
            data['Script'] = column
        if check_is_date(column):
            data['Date'] = column
            data['Year'] = y
            data['Month'] = m
    csvArr.append(column_line)
    csvDict[i] = data


counter_dict = {}
for column in csvArr:
    if column[1] not in counter_dict:
        counter_dict[column[1]] = 1
    else:
        counter_dict[column[1]] += 1
# counter = 0
for key in counter_dict.keys():
    print(key + " = " + str(counter_dict[key]))


# Add leading zeros
for i, line in enumerate(csvDict):
    if len(csvDict[i]['Month'].strip()) == 1:
        csvDict[i]['Month'] = '0' + csvDict[i]['Month'].strip()
    csvDict[i]['Year'] = csvDict[i]['Year'].strip()

all_information_dict = {}
for key, value in csvDict.items():
    if value['SSO'] in all_information_dict:
        if value['Month'] in all_information_dict[value['SSO']]:
            if value['Script'] in all_information_dict[value['SSO']][value['Month']]:
                all_information_dict[value['SSO']][value['Month']][value['Script']] += 1
            else:
                all_information_dict[value['SSO']][value['Month']][value['Script']] = 1
        else:
            all_information_dict[value['SSO']][value['Month']] = {value['Script']: 1}
    else:
        all_information_dict[value['SSO']] = {value['Month']: {value['Script']: 1}}


# sanity check
ctotal = 0
for key, value in all_information_dict.items():
    for ssoVal in list(value.values()):
        for scriptVal in list(ssoVal.values()):
            ctotal += int(scriptVal)
print(ctotal)

# Moths array initialization
months = [format(i+1, '02d') for i in range(12)]

report1(months[7:10], all_information_dict)
report2(months[7:10], all_information_dict)
report3(months[7:10], all_information_dict)
report4(months[7:10], csvDict)
report5(all_information_dict)
report6(all_information_dict)
report7(all_information_dict)
report8(all_information_dict)
