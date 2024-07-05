# my_name = input()
#
# file = open(file='my_name.txt', mode='wt', encoding='utf-8')
# file.write(my_name)
# file.close()
#
# file = open(file='my_name.txt', mode='rt', encoding='utf-8')
# print(file.read())
# file.close()

file = open(file='number_list.txt', mode='w')
for i in range(1, 101):
    file.write(str(i))
    file.write(' ')
    i = i + 1
file.close()



# file = open(file='number_list.txt', mode='rt', encoding='utf-8')
# my_sum = sum(map(int, file.read().split()))
# print(my_sum)
# file.close()

file = open(file='number_list.txt', mode='r')
num = (file.read())
print(num)
