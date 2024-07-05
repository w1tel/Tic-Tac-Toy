# file = open(file='students.txt', mode='rt', encoding='UTF-8')
# students = file.read().split('!')
# for i in students:
#     if 'Джон Перц' in i:
#         index_item = students.index(i)
# students.pop(index_item)
# print(students)
# file.close()
#
# file = open(file='students2.0.txt', mode='wt', encoding='UTF-8')
# file.write("!".join(students))
# file.close()

file = open(file='students2.0.txt', mode='rt', encoding='UTF-8')
students = file.read().split('!')
for i in students:
    if 'Джулия Милан' in i:
        new_note = i.split("\n")
        for j in new_note:
            if j.isdigit():
                index_score =new_note.index(j)
                new_note[index_score] = "100"
                break
        new_note = "\n".join(new_note)

        index_item = students.index(i)
        students[index_item] = new_note

print(students)
file.close()

file = open(file='students2.0.txt', mode='w', encoding='UTF-8')
file.write("!".join(students))
file.close()



