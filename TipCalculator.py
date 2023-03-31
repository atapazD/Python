#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip Calculator")
total = float(input("What is the total bill amount?\n$"))
people = int(input("How many will split the bill?\n"))
tipPercent = int(input("How much tip%?\n"))
tipPercent = 1 + (tipPercent/100)

splitTotal = total/people * tipPercent
splitTotal = "{:.2f}".format(splitTotal) #the "{:.2f}" is a way to format to the 2 decimal places and forcing the hundreths place to be shown
print(splitTotal)
              
