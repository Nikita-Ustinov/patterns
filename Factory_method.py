from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


# -------------------------------------
def print_info_decorator(foo):
    def wrapper_print(*args):
        print('-----')
        print('Name: '+ args[0]._name)
        print('ID: '+ str(args[0]._id))
        foo(args[0])
    return wrapper_print
# -------------------------------------


class Student(Person):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._login = str(id)+'_'+name
        self.hotdogs = 3

    def feed(self):
        if self.hotdogs > 0:
            self.hotdogs -= 1
    
    @print_info_decorator
    def print_info(self):
        print('Login: '+ self._login)
        print('Hotdogs left: '+ str(self.hotdogs))


class Teacher(Person):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._login: str = str(id)+'_'+name
        self.books: int = 3

    def feed(self):
        if self.books > 0:
            self.books -= 1
    
    @print_info_decorator
    def print_info(self):
        print('Login: '+ self._login)
        print('Books left: '+ str(self.books))


class Room(ABC):
    
    @abstractmethod
    def __init__(self):
        self.PersonsList: [Person] = []


class TeachersRoom(Room):

    def __init__(self):
        super().__init__()
        self.PersonsList.append(teach1)
        self.PersonsList.append(teach2)


class StudentsRoom(Room):

    def __init__(self):
        super().__init__()
        self.PersonsList.append(std1)
        self.PersonsList.append(std2)
        self.PersonsList.append(std3)




std1 = Student(0, 'Vasya')
std1.feed()
std1.print_info()

std2 = Student(1, 'Jhon Snow')
std2.feed()
std2.print_info()

std3 = Student(2, 'Batman')
std3.feed()
std3.print_info()

teach1 = Teacher(3, 'Vasilij Petrovij')
teach1.feed()
teach1.print_info()

teach2 = Teacher(4, 'Genadij Petrovij')
teach2.feed()
teach2.print_info()

room1 = TeachersRoom()
room2 = StudentsRoom()

print('Done')
