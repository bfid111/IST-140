import re
f = open('mbox.txt')
fa= []
a= 0
count= 0
for line in f:
   if re.search('^New.+: \d+',line):
       fa= (re.findall('\d+',line))
       a+= int(fa[0])
       count+= 1
print(format(a/count))