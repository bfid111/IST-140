import re
text =raw_input("Enter a regular expression: ")
f = open('mbox.txt')
count=0
for line in f:
    line = line.rstrip()
    if re.search(text, line):
        count+=1
print('mbox.txt had %d that matched %s') % (count, text)