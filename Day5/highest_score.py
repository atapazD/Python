student_scores = [1500,80,120,171,55,66,77,88,99]

# total_sum = sum(student_scores) #sum adds up all of them in the list
# # print (total_sum)

# sum = 0
# for score in student_scores:
#     sum += score

# print (sum)

score = max(student_scores)
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)