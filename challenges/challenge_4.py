from itertools import combinations

class Named:
    """Assign a name to instances of child classes."""

    _instances = {}

    def __new__(cls, *args, **kwargs):
        """Store numbers isntances and assign names based on it."""
        instance = super().__new__(cls)
        cls._instances[cls] = cls._instances.setdefault(cls, 0) + 1
        instance.name = f'{cls.__name__} {cls._instances[cls]}'
        return instance


class Car(Named):
    """A car for the task."""

    CAPACITY = 4

    def __init__(self, cold=None):
        """Initializator."""
        self.cold = cold
        self.students = set()

    def add_student(self, student):
        """Add a student to a car and set the current car in student's fields."""
        if len(self.students) == self.CAPACITY:
            raise EnvironmentError('Car is full')
        print(f'Putting {student} in {self}')
        self.students.add(student)
        student.set_car(self)

    def remove_student(self, student):
        """Remove a student from a car and unset the current car in student's fields."""
        if student not in self.students:
            raise EnvironmentError('Student is not in the car.')
        print(f'Removing {student} from {self}')
        self.students.remove(student)
        student.unset_car()

    def __repr__(self):
        """Pretty print."""
        return self.name


class Student(Named):
    """Student for the task."""

    def __init__(self, smoke=None, chalga=None, cold=None):
        """Initializator."""
        self.smoke = smoke
        self.chalga = chalga
        self.cold = cold
        self.car = None

    def set_car(self, car):
        """Set a car for this student."""
        self.car = car

    def unset_car(self):
        """Unset a car for this student."""
        self.car = None

    def is_comfy(self):
        """Check if student is comfy in their current car."""
        if self.car is None:
            return None
        if self.car.cold and self.cold is False:
            return False
        for student in self.car.students:
            if student is self:
                continue
            if student.smoke and self.smoke is False:
                return False
            if student.chalga and self.chalga is False:
                return False
        return True

    def __repr__(self):
        """Pretty print."""
        return self.name

def confort_in_one_car(car,students):
    list_of_students = students

    for student in list_of_students:
        if not student.is_comfy():                 
            car.remove_student(student)



def organize (cars, students):

    list_of_students = students
    list_of_cars = cars
    lenght_students = len(list_of_students)
    lenght_cars = len(list_of_cars)

    if not (list_of_cars and list_of_students):
        return False
    if lenght_students/ lenght_cars > 4:
        return False
    
    number = 0
    while number < lenght_cars:

        for car in list_of_cars:
            for student in list_of_students:
                if not student.car :
                    try:
                        car.add_student(student)
                        if not student.is_comfy():
                            car.remove_student(student)

                    except EnvironmentError:
                        continue

            if not confort_in_one_car(car, car.students):   
                try:              
                    car.remove_student(student)
                except EnvironmentError:
                        continue

            number += 1
        
    for student in list_of_students:
        if not student.is_comfy():
            return False
        
    return True



        
"""
--------------------------------------------------------------------------------------------------------------------------------------------------------
"""

car_1 = Car(cold= False)
car_2 = Car(cold= False)
car_3 = Car(cold= False)


Pesho = Student(smoke=True, chalga=True,cold=False)
Joro = Student(smoke=False, chalga=False,cold=False)
gosho = Student(smoke=True, chalga=False,cold=False)
Emo = Student(smoke=False, chalga=False,cold=False)
Marta = Student(smoke=False, chalga=False,cold=False)


print(organize([car_1,car_2,car_3],[Pesho,Joro,gosho,Emo,Marta]))
