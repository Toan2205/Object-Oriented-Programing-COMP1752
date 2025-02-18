class Student:
    def __init__(self, name, major, student_id):
        self.name = name
        self.major = major
        self.id = student_id


class ParttimeStudent(Student):
    count = 0

    def __init__(self, name, major, student_id, min_hour, max_hour):
        super().__init__(name, major, student_id)
        self.min_hour = min_hour
        self.max_hour = max_hour
        ParttimeStudent.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


class Lecturer:
    def __init__(self, lecturer_id, name, rank):
        self.name = name
        self.lecturer_id = lecturer_id
        self.rank = rank


class Project:
    def __init__(self, name, budget, leader: Lecturer = None):
        self.name = name
        self.budget = budget
        self.leader = leader
        self.members = []  # Fixed attribute name

    def assign_leader(self, lecturer: Lecturer):
        self.leader = lecturer

    def add_member(self, researcher):
        self.members.append(researcher)  # Fixed typo (self.member -> self.members)

    def display_members(self):
        for member in self.members:
            print(member.name)


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.projects = []

    def add_student(self, student: Student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Full student list!")

    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Full lecturer list!")

    def add_project(self, project: Project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Full project list!")
s1 = ParttimeStudent("Toan","OOP", 101, 10, 20)
s2 = ParttimeStudent("Truong", "Math", 102, 5, 15)

print("Total Part-time Students:", ParttimeStudent.get_count())