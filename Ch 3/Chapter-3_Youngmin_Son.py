
# Name : Youngmin Son (ybs5050)
# IST 140, Chapter 3 Exercises

#Exercise 3.1
hour = raw_input('Enter Hours : ')
rate = raw_input('Enter Rate : ')
if float(hour) > 40:
    overpay = float(float(hour)-40) * (float(rate)*1.5)
    total = (40 * float(rate)) + overpay
    print ("Pay: " + str(total))
else:
    total = (float(hour) * float(rate))
    print ("Pay: " + str(total))

#Exercise 3.2

try:
    hour1 = float(raw_input('Enter Hours : '))
    rate1 = float(raw_input('Enter Rate : '))
except ValueError:
    print "Error, please enter numeric input"

if float(hour1) > 40:
    overpay1 = float(float(hour1)-40) * (float(rate1)*1.5)
    total1 = (40 * float(rate1)) + overpay1
    print ("Pay: " + str(total1))
else:
    total1 = (float(hour1) * float(rate1))
    print ("Pay: " + str(total1))

#Exercise 3.3

try:
    grade = float(raw_input('Enter score : '))
except ValueError:
    print "Bad score"

if grade < 0.0 or grade > 1.0:
    print "Bad score"
if grade >= 0.9 and grade < 1.0:
    print "A"
if grade >= 0.8 and grade < 0.9:
    print "B"
if grade >= 0.7 and grade < 0.8:
    print "C"
if grade >= 0.6 and grade < 0.7:
    print "D"
if grade < 0.6:
    print "F"


