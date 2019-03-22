import mysql.connector
from student import Student
from course import Course

cnx = mysql.connector.connect(
    user='root', password='1', host='127.0.0.1', database='bootcamp')

cursor = cnx.cursor()

query_for_students = ("select * from students")

query_for_courses = ("select * from course")

cursor.execute(query_for_students)

students = []

for student in cursor:
    s = Student(student[1], student[2], student[3])
    students.append(s)


cursor.execute(query_for_courses)

courses = []

for cc in cursor:
    c = Course(cc[1], cc[2])
    courses.append(c)

for s in students:
    print('Soyadı: %s | Adı: %s | Yaşı: %d' % (s.surname, s.name, s.age()))

for c in courses:
    print('Adı: %s | Adresi: %s' % (c.name, c.address))

cnx.cursor()
cnx.close()
