# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

newAge = int(age)

daysLeft = (90*365)-(newAge*365)
weeksLeft = (90*52)-(newAge*52)
monthsLeft = (90*12)-(newAge*12) 

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")


