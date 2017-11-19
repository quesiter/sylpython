import sys
from collections import Counter
import re

class Person(object):
    """
    返回成绩
    """

    def __init__(self, grades):
        self.grades = grades

    def get_grade():
        return self.grades


class Student(Person):

    def __init__(self, grades):
        Person.__init__(self, grades)

    def get_grade(self):
        pattern1 = re.compile('[ABC]')
        self.Pass = sum(Counter(pattern1.findall(self.grades)).values())
        pattern2 = re.compile('D')
        self.Fail = sum(Counter(pattern2.findall(self.grades)).values())
        return "Pass: {}, Fail: {}".format(self.Pass, self.Fail)


class Teacher(Person):

    def __init__(self, grades):
        Person.__init__(self, grades)

    def get_grade(self):
        result = Counter(self.grades).most_common()
        string = ["{}: {}".format(x,y) for x, y in result]
        string = ", ".join(string)
        return string




if __name__ == '__main__':
    s = sys.argv[2]
    if 'teacher' == sys.argv[1]:
        grade = Teacher(s)
    elif 'student' == sys.argv[1]:
        grade = Student(s)
    print(grade.get_grade())
