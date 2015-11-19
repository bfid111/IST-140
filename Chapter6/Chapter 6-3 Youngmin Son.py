# Youngmin Son
# IST 140
# Chapter 6 Exercises

word = 'banana'
letter = 'a'

def count(string, let):
  count = 0
  for letter in string:
    if letter == let:
      count = count + 1
  print count

count(word,letter)
count('apple','a')
count('college','e')