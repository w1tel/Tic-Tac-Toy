

file = open(file='steps.txt', mode='rt')
result = file.read().split()
file.close()
steps_sum = 0
for i in result:
    steps_sum = steps_sum + int(i)

print(steps_sum // 365)


