class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        self.enrolled = []
        self.lectures = []
        self.homeworks = []
        for i in range(number_of_lectures):
            self.lectures.append(Lecture("Lecture " + str(i+1), i+1, teacher))
            self.lectures[i].course = self
        teacher.extend_lectures(self.lectures)

    def __str__(self):
        return f'{self.name} ({self.start_date})'

    def enroll_student(self, student):
        self.enrolled.append(student)

    def enrolled_by(self):
        return self.enrolled

    def get_lecture(self, number):
        assert number > 1 and number <= self.number_of_lectures, f"Invalid lecture number"
        return self.lectures[number-1]

    def add_homework(self, homework):
        self.homeworks.append(homework)
        for student in self.enrolled:
            student.assign_homework(homework)

    def get_homeworks(self):
        return self.homeworks


class Lecture:
    def __init__(self, name, number, teacher):
        self.name = name
        self.number = number
        self.teacher = teacher

    def new_teacher(self, teacher):
        self.teacher.lectures.remove(self)
        self.teacher = teacher
        self.teacher.extend_lectures([self])

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course

    def get_homework(self):
        try:
            return self.homework
        except AttributeError:
            pass

    def set_homework(self, homework):
        homework.set_course(self.course)
        homework.set_lecture(self)
        self.homework = homework
        self.course.add_homework(homework)


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.done_dict = {}

    def __str__(self):
        return f"{self.name}: {self.description}"

    def done(self, student):
        self.done_dict[student] = None

    def done_by(self):
        return self.done_dict

    def set_course(self, course):
        self.course = course
    
    def set_lecture(self, lecture):
        self.lecture = lecture


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.assigned_homeworks = []

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"

    def enroll(self, course):
        course.enroll_student(self)

    def assign_homework(self, homework):
        self.assigned_homeworks.append(homework)

    def do_homework(self, homework):
        homework.done(self)
        homework.course.teacher.add_to_check(homework)
        self.assigned_homeworks.remove(homework)


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.lectures = []
        self.homeworks_to_check = []

    def extend_lectures(self, lectures):
        self.lectures.extend(lectures)

    def teaching_lectures(self):
        return self.lectures

    def add_to_check(self, homework):
        self.homeworks_to_check.append(homework)

    def check_homework(self, homework, student, mark):
        if not (student in homework.done_dict):
            raise ValueError("Student never did that homework")
        if homework.done_dict[student] != None:
            raise ValueError("You already checked that homework")
        assert mark >= 0 and mark <= 100, f"Invalid mark"
        homework.done_dict[student] = mark
        self.homeworks_to_check.remove(homework)

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures

    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by() == students

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        assert student.assigned_homeworks == [functions_homework]

    assert main_teacher.homeworks_to_check == []
    students[0].do_homework(functions_homework)
    assert students[0].assigned_homeworks == []
    assert students[1].assigned_homeworks == [functions_homework]

    assert functions_homework.done_by() == {students[0]: None}
    assert main_teacher.homeworks_to_check == [functions_homework]

    for mark in (-1, 101):
        try:
            main_teacher.check_homework(functions_homework, students[0], mark)
        except AssertionError as error:
            assert error.args == ('Invalid mark',)

    main_teacher.check_homework(functions_homework, students[0], 100)
    assert main_teacher.homeworks_to_check == []
    assert functions_homework.done_by() == {students[0]: 100}

    try:
        main_teacher.check_homework(functions_homework, students[0], 100)
    except ValueError as error:
        assert error.args == ('You already checked that homework',)

    try:
        main_teacher.check_homework(functions_homework, students[1], 100)
    except ValueError as error:
        assert error.args == ('Student never did that homework',)

    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher

    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    assert substitute_teacher.homeworks_to_check == []
