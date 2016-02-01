import requests
import datetime

base_url = 'https://api.groupme.com/v3/'
bot_id = 'bd42d28ae5e3b685f3085876e7'
text_url = base_url + 'bots/post?bot_id=' + bot_id + '&text='

assignments = {}
now = datetime.datetime.now()
oneWeek = now + datetime.timedelta(days=7)

def addAssignment(name, due) :
    global assignments
    assignments[name] = due


def formatDueDate(due) :
    dueDay = due.split('/')
    dueTime = dueDay[2].split(' ')
    
    year = int(dueTime[0])
    month = int(dueDay[0])
    day = int(dueDay[1])

    pIndex = dueTime[1].rfind('p')
    hour = dueTime[1][0:pIndex]
    if pIndex > -1 :
        if hour != '12' :
            hour = int(hour) + 12
        else :
            hour = int(hour)

    else :
        if hour == '12' :
            hour = int(hour) - 12
        else :
            hour = int(hour)

    return datetime.datetime(year+2000, month, day, hour)


def printExistingAssignments () :
    global assignments
    for name in assignments :
        print(name + ":" + assignments[name])


def findAssignments () :
    global text_url
    global assignments
    global now
    global oneWeek
    
    requests.post(text_url + '!!! ASSIGNMENTS DUE !!!')
    for name in assignments :
        d = formatDueDate(assignments[name])
        if now < d and d < oneWeek :
            diff = oneWeek - d
            diffStr = str(diff)
            alert = name + ' is due in ' + diffStr[:-13] + ' hours' #, on ' + assignments[name] 
            requests.post(text_url + alert) 


addAssignment('Networks Hw1', '2/1/16 11a')
addAssignment('Mobile Hw1: App Reviews', '2/3/16 11p')
addAssignment('SWE Collatz', '2/4/16 10p')
addAssignment('Mobile Tutorial 2', '2/5/16 11p')
addAssignment('Networks Wireshark Lab2', '2/10/16 11a')
addAssignment('Gov Paper: Should Senate represent people or states?', '2/12/16 10a')
addAssignment('Mobile Tutorial 3', '2/12/16 11p')
addAssignment('Networks Hw2', '2/15/16 11a')

findAssignments()

print('Done')


