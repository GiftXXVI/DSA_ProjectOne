"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

text_senders = []
text_receivers = []
for text in texts:
    text_senders.append(text[0])
    text_receivers.append(text[1])

call_diallers = []
call_recipients = []
for call in calls:
    call_diallers.append(call[0])
    call_recipients.append(call[1])

numbers = text_receivers + text_senders + call_diallers + call_recipients
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(f'There are {len(unique_numbers)} different numbers in the records.')
