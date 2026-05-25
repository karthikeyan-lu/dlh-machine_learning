#!/usr/bin/env python3
"""105-main"""

from pymongo import MongoClient
insert_school = __import__('31-insert_school').insert_school
top_students = __import__('105-students').top_students

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    j_students = [
        {
            'name': "John",
            'topics': [
                {'title': "Algo", 'score': 10.3},
                {'title': "C", 'score': 6.2},
                {'title': "Python", 'score': 12.1}
            ]
        },
        {
            'name': "Bob",
            'topics': [
                {'title': "Algo", 'score': 5.4},
                {'title': "C", 'score': 4.9},
                {'title': "Python", 'score': 7.9}
            ]
        },
        {
            'name': "Sonia",
            'topics': [
                {'title': "Algo", 'score': 14.8},
                {'title': "C", 'score': 8.8},
                {'title': "Python", 'score': 15.7}
            ]
        }
    ]

    for j_student in j_students:
        insert_school(students_collection, **j_student)

    students = top_students(students_collection)

    for student in students:
        print("[{}] {} => {}".format(
            student.get('_id'),
            student.get('name'),
            student.get('averageScore')
        ))
