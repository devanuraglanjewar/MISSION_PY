# Write a program to greeting you Good morning, Good afternoon, Good evening, Good night as per the time.
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
if hours >= 6 and hours <12:
    print("Good Morning")
elif hours >=12 and hours<18:
    print("Good Afternoon")
elif hours >=18 and hours<22:
    print("Good Evening")
else:
    print("Good Night")
