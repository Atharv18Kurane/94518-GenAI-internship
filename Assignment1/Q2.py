"""Q2:

Count Even and Odd Numbers

Take a list of numbers as input (comma-separated).

Count how many are even and how many are odd.

Print results.

Example Input:
10, 21, 4, 7, 8"""

num=input("Enter numbers (comma-separated):")
num_list = [int(num)for num in num.split(",")]

even_count=0
odd_count=0

for num in num_list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Even count is:",even_count)
print("Odd count is :", odd_count)




