class Person(object):

    def __init__(self, name, adress, birthday):
        self.name = name
        self.adress = adress
        self.birthday = birthday


class Employe(Person):

    def __init__(self, name, adress, birthday, staffnumber, pay):
        self.staffnumber = staffnumber
        self.pay = pay
        super().__init__(self, name, adress, birthday)


class Studentassistent(Person):

    def __init__(self, name, adress, birthday, department):
        self.department = department
        super().__init__(self, name, adress, birthday)


class Student(Person):

    def __init__(self, name, adress, birthday, studentnumber):
        self.studentnumber = studentnumber
        super().__init__(self, name, adress, birthday)


class Mayor(Student):

    def __init__(self, mayor_1, mayor_2, mayor_3):
        self.mayor_1 = mayor_1
        self.mayor_2 = mayor_2
        self.mayor_3 = mayor_3


class Personnelmanagment(Employe):

    def select(self, Person):
        pass

    def transfersalary(self, Employe):
        pass


def main():
    """
    main function
    """


if __name__ == "main":
    main()

