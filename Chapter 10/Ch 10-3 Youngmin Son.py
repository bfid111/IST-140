import string

def frequent(f):
   d = dict()
   for line in file:
      line = line.translate(None, string.punctuation)
      line = line.translate(None, ' ')
      line = line.lower()
      line = line.translate(None, '0123456789')
      line = line.strip()
      for letter in line:
         d[letter] = d.get(letter, 0) + 1
   lst = list()
   for key, val in d.items():
      lst.append((val,key))
   lst.sort(reverse=True)
   return lst

fname =  raw_input('Enter file name: ')
file = open(fname)
res = frequent(file)
for key, val in res[0:10]:
   print val, key