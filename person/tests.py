from django.test import TestCase
from .models import Student, NoStudent
import datetime
from rest_framework import generics


class StudentTestCase(TestCase):
    def setUp(self):
        start_time = datetime.datetime.now()
        students = []
        batch_size = 500
        for i in range(100000):
            student = Student()
            student.first_name = str(i)
            student.last_name = str(i)
            student.code0 = f"code{i}"
            students.append(student)
        Student.objects.bulk_create(students, batch_size)

        end_time = datetime.datetime.now()
        print(f" Created in {end_time - start_time}")

    def test_lookup(self):
        start_time = datetime.datetime.now()
        for i in range(50000, 51000):
            Student.objects.get(code0=f"code{i}")

        end_time = datetime.datetime.now()
        print(f"Looked up in {end_time - start_time}")


class Student1TestCase(TestCase):
    def setUp(self):
        start_time = datetime.datetime.now()
        students = []
        batch_size = 500
        for i in range(100000):
            student = NoStudent()
            student.first_name = str(i)
            student.last_name = str(i)
            student.code0 = f"code{i}"
            students.append(student)
        NoStudent.objects.bulk_create(students, batch_size)

        end_time = datetime.datetime.now()
        print(f" Created in {end_time - start_time}")

    def test_lookup(self):
        start_time = datetime.datetime.now()
        for i in range(50000, 51000):
            NoStudent.objects.get(code0=f"code{i}")

        end_time = datetime.datetime.now()
        print(f"Looked up in {end_time - start_time}")