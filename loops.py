# List
numbers = [12, 7, 45, 23, 3, 67, 34, 18]
# loop
for num in numbers:
    if num < 10:
        print(f"{num} is less then 10")
    elif 10 <= num <= 30:
        print(f"{num} is greater than 10 and less than 30")
    else:
        print(f"{num} is greater than 30")
