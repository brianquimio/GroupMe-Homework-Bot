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
            diff = d - now
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
addAssignment('Networks Project 1', '2/15/16 11p')
addAssignment('Mobile Hw2: App Proposals', '2/15/16 11p')
addAssignment('Networks Exam 1', '2/17/16 11a')
addAssignment('SWE Project 2', '2/18/16 10p')
addAssignment('Mobile Tutorial 4', '2/19/16 11p')
addAssignment('Gov Exam 1', '2/19/16 10a')
addAssignment('Mobile Tutorial 5', '2/26/16 11p')
addAssignment('SWE Exam 1', '3/3/16 7p')
addAssignment('Mobile Tutorial 6', '3/4/16 11p')
addAssignment('Networks Hw3', '3/7/16 11a')
addAssignment('Mobile Hw3: App Mock Up', '3/11/16 11p')
addAssignment('Networks Hw4', '3/21/16 11a')
addAssignment('SWE Project 3', '3/24/16 10p')
addAssignment('Gov Paper: Should people with criminal records have a right to vote?', '3/25/16 10a')
addAssignment('Networks Exam 2', '3/28/16 11a')
addAssignment('Gov Exam 2', '4/1/16 10a')
addAssignment('Mobile Hw4: Alpha Release', '4/4/16 11p')
addAssignment('SWE Project 4', '4/7/16 10p')
addAssignment('Networks Hw5', '4/13/16 11a')
addAssignment('Mobile Hw5: Alpha Evals', '4/13/16 11p') 
addAssignment('Gov Paper: Should states sentence nonviolent drug offenders to length prison terms?', '4/15/16 10a')
addAssignment('Networks Project 2', '4/20/16 11p')
addAssignment('SWE Project 5', '4/21/16 10p')
addAssignment('Networks Hw6', '4/27/16 11a')
addAssignment('Mobile Hw6: How to Page', '4/27/16 11p')
addAssignment('Networks Exam 3', '5/2/16 11a')
addAssignment('Mobile Hw7: Beta App', '5/4/16 11p')
addAssignment('SWE Exam 2', '5/5/16 7p')
addAssignment('Mobile Hw8: Web Ad', '5/6/16 11p')
addAssignment('Gov Exam 3', '5/6/16 10a')


findAssignments()

print('Done')
