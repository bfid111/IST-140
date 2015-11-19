
# Name : Youngmin Son (ybs5050)
# IST 140, Chapter 2 Exercises

#Exercise 2.2
name = raw_input('Enter your name : ')
print ("Hello" + " " + name)

#Exercise 2.3
hour = raw_input('Enter Hours : ')
rate = raw_input('Enter Rate : ')
total =  (float(hour) * float(rate))
print ("Pay: " + str(total))

#Exercise 2.4
width = 17
height = 12.0

print("width/2 is : " + str(width/2))
print("width/2.0 is : " + str(width/2.0))
print("height/3 is : " + str(height/3))
print("1 + 2 * 5 is : " + str(1 + 2 * 5))

#Exercise 2.5

temp = raw_input('Enter a Celcius temperature ')
farenheit = float(float(temp)*9/5+32)
print("Farenheit Temperature is : " ) + str(farenheit)
