lines = [word.strip('\n')
for word in open('words.txt', 'r')]
word_dict = {}
for line in lines:
    words = line.split()
    for word in words:
        word_dict[word] = None


print "from" in word_dict
print "hello" in word_dict
print "car" in word_dict