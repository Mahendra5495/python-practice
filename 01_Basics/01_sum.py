# Write a Python program to find the sum of all even numbers from 1 to 100
sum = 0

for x in range(101):
    if x % 2 == 0:
        sum += x
print(f"Sum of even numbers from 1 to 100: {sum}")
