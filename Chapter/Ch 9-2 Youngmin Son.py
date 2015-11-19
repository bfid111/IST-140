file_name = 'mbox-short.txt'
lines = [line.strip('\n')
for line in open(file_name, 'r')
if line.startswith("From ")]
date = {}

for line in lines:
    words = line.split()
    date[words[2]] = date.get(words[2], 0) + 1

print date