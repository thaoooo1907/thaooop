# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:33:17 2024

@author: ADMIN
"""

class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.grade = self.update_grade()

    def update_grade(self):
        if self.gpa < 3.5:
            return "Kém"
        elif 3.5 <= self.gpa < 5.0:
            return "Yếu"
        elif 5.0 <= self.gpa < 7.0:
            return "Trung bình"
        elif 7.0 <= self.gpa < 8.0:
            return "Khá"
        elif 8.0 <= self.gpa < 9.0:
            return "Giỏi"
        elif 9.0 <= self.gpa <= 10.0:
            return "Xuất sắc"

    def __str__(self):
        return f"Mã SV: {self.id}, Họ tên: {self.name}, Điểm TB: {self.gpa}, Xếp loại: {self.grade}"


class StudentManager:
    def __init__(self):
        self.students = []

    def initialize_students(self, student_list):
        for student in student_list:
            self.students.append(Student(student['id'], student['name'], student['gpa']))

    def add_random_student(self, id, name, gpa):
        self.students.append(Student(id, name, gpa))

    def display_students(self):
        for student in self.students:
            print(student)

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.gpa)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def find_students_by_gpa(self, gpa):
        return [student for student in self.students if student.gpa == gpa]

    def top_10_students(self):
        return sorted(self.students, key=lambda s: s.gpa, reverse=True)[:10]
if __name__ == "__main__":
    manager = StudentManager()
    students_info = [
        {'id': 'SV001', 'name': 'Nguyen Van A', 'gpa': 8.5},
        {'id': 'SV002', 'name': 'Tran Thi B', 'gpa': 6.0},
        {'id': 'SV003', 'name': 'Le Van C', 'gpa': 9.2},
        {'id': 'SV004', 'name': 'Pham Thi D', 'gpa': 4.8},
        {'id': 'SV005', 'name': 'Vo Van E', 'gpa': 7.5},
    ]

    manager.initialize_students(students_info)
    print("Danh sách sinh viên:")
    manager.display_students()
    top_student = manager.get_top_student()
    if top_student:
        print("\nSinh viên có điểm TB cao nhất:")
        print(top_student)
    print("\nTìm sinh viên theo mã 'SV002':")
    student = manager.find_student_by_id('SV002')
    if student:
        print(student)
    else:
        print("Không tìm thấy sinh viên.")
    print("\nTìm sinh viên có điểm TB 8.5:")
    found_students = manager.find_students_by_gpa(8.5)
    for s in found_students:
        print(s)
    print("\n10 sinh viên có điểm TB cao nhất:")
    top_students = manager.top_10_students()
    for s in top_students:
        print(s)
