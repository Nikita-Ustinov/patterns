from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, amount: int):
        pass

    @abstractmethod
    def feed(self) -> None:
       pass

    @abstractmethod
    def getAmount(self) -> int:
        pass


class Hotdog(Food):
    def __init__(self, amount: int):
        self.hotdogs = amount

    def feed(self) -> None:
        if self.hotdogs > 0:
            self.hotdogs -= 1
    
    def getAmount(self) -> int:
        return self.hotdogs
        


class Book(Food):
    def __init__(self, amount: int):
        self.book = amount

    def feed(self) -> None:
        if self.book > 0:
            self.book -= 1

    def getAmount(self) -> int:
        return self.book



def print_info_decorator(foo):
    def wrapper_print(*args):
        print('-----')
        print('Name: '+ args[0]._name)
        print('ID: '+ str(args[0]._id))
        print('Login: '+ args[0]._login)
        foo(args[0])
    return wrapper_print


class Person(ABC):
    def __init__(self, id: int, name: str, food: Food):
        self._id = id
        self._name = name
        self.food = food
        self._login: str = ""

    @abstractmethod
    def print_info(self) -> None:
        pass

    def feed(self) -> None:
        if self.food.getAmount() > 0:
            self.food.feed()
        else:
            print("Have nothing to eat...")


class Student(Person):
    def __init__(self, id: int, name: str, food: Hotdog):
        super().__init__(id, name, food)
        self._login = str(id)+'_'+name

    @print_info_decorator
    def print_info(self) -> None:
        print('Hotdogs left: '+ str(self.food.getAmount()))
        
    
class Teacher(Person):
    def __init__(self, id: int, name: str, food: Book):
        super().__init__(id, name, food)
        self._login: str = str(id)+'_'+name


    @print_info_decorator
    def print_info(self) -> None:
        print('Books left: '+ str(self.food.getAmount()))



class AbstractFactory(ABC):
    @abstractmethod
    def createPerson(self, food: Food) -> Person:
        pass
    
    @abstractmethod
    def createFood(self) -> Food:
        pass


class StudentFactory(AbstractFactory):
    def createPerson(self, food) -> Student:
        return Student(0, 'Piter Parker', food)

    def createFood(self) -> Hotdog:
        return Hotdog(3)


class TeacherFactory(AbstractFactory):
    def createPerson(self, food) -> Teacher:
        return Teacher(1, 'Tony Stark', food)

    def createFood(self) -> Book:
        return Book(25)


def main(factory: AbstractFactory) -> None:
    food = factory.createFood()
    person = factory.createPerson(food)
    person.feed()
    person.feed()
    person.print_info()


main(TeacherFactory())
main(StudentFactory())

