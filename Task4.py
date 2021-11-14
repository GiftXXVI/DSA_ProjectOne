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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

call_diallers = []
call_recipients = []
for call in calls:
    call_diallers.append(call[0])
    call_recipients.append(call[1])

text_senders = []
text_recipients = []
for text in texts:
    text_senders.append(text[0])
    text_recipients.append(text[1])

numbers = call_recipients + text_senders + text_recipients
tele_diallers = []
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

for dialler in call_diallers:
    if dialler not in unique_numbers:
        if dialler not in tele_diallers:
            tele_diallers.append(dialler)

sorted_diallers = sorted(tele_diallers)

print("These numbers could be telemarketers: ")
for dialler in sorted_diallers:
    print(dialler)
