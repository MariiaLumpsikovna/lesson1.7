grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students = sorted(students)
a = sorted(list(students))


GPA1 = (sum(grades[0]))/len(grades[0])
GPA2 = (sum(grades[1]))/len(grades[1])
GPA3 = (sum(grades[2]))/len(grades[2])
GPA4 = (sum(grades[3]))/len(grades[3])
GPA5 = (sum(grades[4]))/len(grades[4])
b = [GPA1, GPA2, GPA3, GPA4, GPA5]


c = dict([[a[0], b[0]], [a[1],b[1]], [a[2], b[2]], [a[3], b[3]], [a[4], b[4]]])
print(c)
