import random

friends = ["Bob","jenn", "dan", "james"]

#1 option
print (random.choice(friends ))

#2 option
random_index = random.randint(0,3)

print(friends[random_index])

# both ways are equally valid

#/what does index out of range mean?
