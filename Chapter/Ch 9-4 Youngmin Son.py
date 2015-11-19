file_name = "mbox-short.txt"
lines = [line.strip('\n')
for line in open(file_name, 'r')
if line.startswith("From ")]
sender = {}

for line in lines:
    words = line.split()
    sender[words[1]] = sender.get(words[1], 0) + 1

most = 0
winner = None
for person in sender:
    if sender[person] > most:
        most = sender[person]
        winner = person

print winner, sender[winner]