class Person:
    def __init__(self, fname):
        self.firstname = fname
    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()

# Example


class PersonExample:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printfullname(self):
        print(self.firstname, self.lastname)


x = PersonExample("Paulo", "Santos")
x.printfullname()


class StudentExample(PersonExample):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.personage = age

    def presentation(self):
        print("This student is", self.firstname, self.lastname, ". Age:", self.personage)


y = StudentExample("Paulo", "Santos", "25")
y.presentation()
