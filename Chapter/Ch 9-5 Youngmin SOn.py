file_name = "mbox-short.txt"
lines = [line.strip('\n') for line in open(file_name, 'r')
if line.startswith("From ")]
sender = {}

for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    sender[domain] = sender.get(domain, 0) + 1

print sender