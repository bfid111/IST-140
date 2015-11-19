# Youngmin Son
# IST 140
# Chapter 6 Exercises

str = 'X-DSPAM-Confidence: 0.8475'

pos = str.find(':')
print pos
data = float(str[pos+1:])
print data

