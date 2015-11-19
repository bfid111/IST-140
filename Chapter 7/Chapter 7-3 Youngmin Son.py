# Youngmin Son
# IST 140
#Exercise 7.3

name = raw_input('Enter a file name: ')
if name == 'na na boo boo' :
    print 'NA NA BOO BOO TO YOU - You have been punk''d!'
    exit()
try:
    fhand = open(name)
except :
    print 'Cannot open File :', name
    exit()
count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count+=1
print 'There were', count, 'subject lines in', name
