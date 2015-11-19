# Name : Youngmin Son (ybs5050)
# IST 140, Chapter 4 Exercises

#Exercise 4.1
import random

for x in range(10):
    a = random.random()
    print a

#Exercise 4.2
def print_lyrics():
    print "I'm a umberjack, and I'm okay."
    print 'I sleep all night and I work all day.'
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    +repeat_lyrics

#Exercise 4.3

def repeat_lyrics():
    print_lyrics
    print_lyrics

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'
repeat_lyrics
#Exercise 4.4

print 'What is the purpose of the def keyword in Python?'
print 'The Answer is " C  " It indicates that the following indented section of code is to be stored for later'

#Exercise 4.5

print 'It will print ABC Zap ABC'

#Exercise 4.6

error = "Enter numeric input , ERROR "
def computepay(hour, rate):
    temphour = float(hour)
    temprate = float(rate)
    try:
        #print error when hour or rate is not numeric
        float(temphour)>=0
    except:
        print(error)
    try:
        float(temprate)>=0
    except:
        print (error)

    if temphour > 40:
        overtime = temphour - 40
    else:
        overtime = 0
    overpay = float(0.5 * overtime * temprate)
    totalpay = float((temphour*temprate) + overpay)

    print ("Total Pay :") + str(totalpay)

hours = float(raw_input("Enter hours  : "))
rates = float(raw_input("Enter Rate : "))
computepay(hours,rates)

#Exercise 4.7


def computegrade(grade1):

    grade = float(grade1)
    if grade < 0.0 or grade > 1.0:
        print "Bad score"
    if grade >= 0.9 and grade < 1.0:
        print "A"
    if grade >= 0.8 and grade < 0.9:
        print "B"
    if grade >= 0.7 and grade < 0.8:
        print "C"
    if grade > 0.6 and grade < 0.7:
        print "D"
    if grade <= 0.6:
        print "F"
try:
    gradeinput = float(raw_input('Enter a score between 0.0 and 1.0 : '))
except:
    print "Bad Score"
computegrade(gradeinput)




