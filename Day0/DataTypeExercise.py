# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

newTwoDigitNum = str(two_digit_number)
#print(type(newTwoDigitNum))
digitOne = int(newTwoDigitNum[0])
digitTwo = int(newTwoDigitNum[1])

addTwoDigits =  digitTwo + digitOne

print (addTwoDigits)