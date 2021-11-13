"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_diallers = [row[0] for row in calls]
call_recipients = [row[1] for row in calls]
numbers = call_diallers + call_recipients
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
summary = {}
maxindex = ''
maxvalue = 0
for number in unique_numbers:
    summary[number] = 0
    for call in calls:
        if call[0] == number or call[1] == number:
            summary[number] += int(call[3])
    if summary[number] > maxvalue:
        maxvalue = summary[number]
        maxindex = number

print(f'''
{maxindex} spent the longest time, {maxvalue} seconds, on the phone during September 2016. 
''')
