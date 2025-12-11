"""Q1:
Write a Python program that takes a sentence from the user and prints:

Number of characters

Number of words

Number of vowels

Hint: Use split(), loops, and vowel checking."""

s1=input("enter a sentence")

char = len(s1)

words=len(s1.split())

vowel="AEIOUaeiou"
count=0

for ch in s1:
    if ch in vowel:
        count=count+1

print("characters:", char)
print("words:" ,words)
print("vowels are:", count)
