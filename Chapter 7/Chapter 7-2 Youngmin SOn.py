# Youngmin Son
# IST 140
#Exercise 7.2
x=0
while x < 2:
    name = raw_input('Enter a file name: ')
    spamconf = []
    try:
        fhand = open(name)
    except:
        print 'Cannot open File :', name
        exit()
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence'):
            spamconf.append(float(line.split()[1]))
    print "Average spam confidence: %s" % str((sum(spamconf)) / len(spamconf))
    x+=1



