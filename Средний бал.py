grades = [[5, 3, 3, 5, 4],
  [2, 2, 2, 3],
  [4, 5, 5, 2],
  [4, 4, 3],
  [5, 5, 5, 4, 5]
          ]
students = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
}
sort_students = sorted(students)
dict_some = {}

avg1 = sum(grades[0]) / len(grades[0])
avg2 = sum(grades[1]) / len(grades[1])
avg3 = sum(grades[2]) / len(grades[2])
avg4 = sum(grades[3]) / len(grades[3])
avg5 = sum(grades[4]) / len(grades[4])

dict_some[sort_students[0]] = avg1
dict_some[sort_students[1]] = avg2
dict_some[sort_students[2]] = avg3
dict_some[sort_students[3]] = avg4
dict_some[sort_students[4]] = avg5
print(dict_some)