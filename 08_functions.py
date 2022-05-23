def percentage(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

marks1 = [45, 78, 86, 77]
percentage1 = percentage(marks1)

marks2 = [75, 98, 99, 78]
percentage2 = percentage(marks2)

print(percentage1, percentage2)