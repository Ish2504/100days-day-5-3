#Write your code below this row 👇
count = 0
for number in range(2, 101, 2):  
  count += number

print(count)

count1 = 0
for number in range(1, 101):
  if number % 2 == 0:
    count1 += number

print(count1)