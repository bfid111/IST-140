fname =  raw_input('Enter file name: ')
file = open(fname)
d = dict()
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or words[1].find('@') == -1:
        continue
    address = words[1]
    d[address] = d.get(words[1],0) + 1
lst = list()
for address, count in d.items():
    lst.append((count,address))
lst.sort()
for key, val in lst:
   print key, val