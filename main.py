# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv


class Animal:
    """class of Animal"""

    def __init__(self, number=1, name="void-name", breed="void_breed", age=1):  # конструктор
        self._name = name  # свойство имя
        self._breed = breed  # свойство кличка
        try:
            if not self.number_ok(number):  # если номер некорректный
                raise Exception("number must be integer number from 1 to 100")  # бросить исключение
        except Exception as e:  # перехват исключения
            print(str(e))  # вывод исключения
        try:
            if not self.age_ok(age):  # если возраст некорректный
                raise Exception("age must be integer number from 1 to 30")  # бросить исключение
        except Exception as e:  # перехват исключения
            print(str(e))  # вывод исключения
        else:
            self._number = number  # свойство номер
            self._age = age  # свойство возраст

    def __getitem__(self, key):  # метод для получения свойства
        return getattr(self, key)

    def __repr__(self):  # перегрузка repr()
        return f"{self._number}, {self._name}, {self._breed}, {repr(self._age)}"

    def __iter__(self):  # реализация итератора
        return iter(self.make_list())

    def __next__(self):  # следующий элемент - для реализации итератора
        return next(iter(self))

    def make_list(self):  # метод создающий список из свойств
        return [self._number, self._name, self._breed, self._age]

    def show_data(self):  # метод для вывода данных на экран
        print(f"number: {self._number}")  # вывод номера
        print(f"name: {self._name}")  # вывод имени
        print(f"breed: {self._breed}")  # вывод клички
        print(f"age: {self._age}")  # вывод возраста

    def get_list(self):  # реализация генератора
        return (item for item in self.make_list())  # возвращаем список с помощью генератора

    def get_collection(self):  # возвращаем словарь
        return {"number": self._number,
                "name": self._name,
                "breed": self._breed,
                "age": self._age}

    @staticmethod  # статический метод для проверки номера на корректность
    def number_ok(number):
        return 0 < number < 100

    @staticmethod  # статический метод для проверки возраста на корректность
    def age_ok(age):
        return 1 < age < 30


class Dog(Animal):  # класс Собака - наследуется от класса Животное
    """class of Dog"""
    def __init__(self, number=1, name="void-name", breed="void_breed", age=1, color="void-color"):  # конструктор
        super().__init__(number, name, breed, age)  # вызов конструктора из класса-предка Животное
        self._color = color  # установка свойства окрас

    def __iter__(self):  # итератор
        return iter(self.make_list())

    def __next__(self):  # следующий элемент - для реализации итератора
        return next(iter(self))

    def __repr__(self):  # перегрузка repr()
        return f"{ super().__repr__()}, {self._color}"

    def show_data(self):  # вывод свойств
        super().show_data()  # вызов метода класса-предка
        print(f'color: {self._color}', '\n')  # вывод данных

    def make_list(self):  # метод для создания списка из свойств
        result = super().make_list()  # создание списка из свойств, унаследованных от класса-предка
        result.append(self._color)  # добавление к списку своего свойства - окраса
        return result

    def get_collection(self):  # метод для формирования словаря
        output = super().get_collection()  # формирование словаря из свойств класса-предка
        output["color"] = self._color  # добавление в словарь нового ключа-значения - окрас
        return output


def get_from_csv_file(file_name):  # функция чтения из файла
    with open(file_name, 'r') as f:
        return [item for item in csv.DictReader(f)]  # чтение из файла


def write_to_file(data_to_file):  # функция для записи в файл
    file = open('output.csv', 'w', newline="")  # открытие файла
    columns = ["number", "name", "breed", "age", "color"]  # названия столбцов
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()  # запись заголовков
    writer.writerows(data_to_file)  # запись данных


def by_number_key(dog):  # ключ для сортировки по номеру
    return getattr(dog, "_number")  # возвращаем значение свойства номер


def by_breed_key(dog):  # ключ для сортировки по породе
    return getattr(dog, "_breed")  # возвращаем значение свойства порода


def by_age_key(dog):  # ключ для сортировке по возрасту
    return getattr(dog, "_age")  # возвращаем значение свойства возраст


def main():
    print("data from file:")
    data_from_file_list = get_from_csv_file("data.csv")  # читаем из файла
    dogs_list = list()  # создаем пустой список для элементов класса Dog

    for item in data_from_file_list:  # пробегаемся по данным из файла
        # создаем очередной экземпляр класса Dog с параметрами, прочитанными из файла
        regular_dog = Dog(int(item["number"]), item["name"], item["breed"], int(item["age"]), item["color"]) # создаем
        regular_dog.show_data()  # выводим на экран свойства очередного экземпляра класса
        dogs_list.append(regular_dog)  # записываем в список очередной экземпляр класса

    print("2.1: sort by 'breed':")
    sort_by_breed = sorted(dogs_list, key=by_breed_key)  # сортируем по породе
    for item in sort_by_breed:  # пробегаемся по отсортированному списку
        item.show_data()  # выводим очередной экземпляр класса

    print("2.2: sort by 'number':")
    sort_by_number = sorted(dogs_list, key=by_number_key)  # сортируем по номеру
    for item in sort_by_number:  # пробегаемся по отсортированному списку
        item.show_data()  # выводим очередной экземпляр класса

    age = int(input("2.3: enter age of dog:"))  # вводим возраст
    # записываем в список только те экземпляры, у которых возраст больше введенного
    get_by_age = [item for item in dogs_list if getattr(item, "_age") > age]
    if len(get_by_age) == 0:  # если список пуст
        print('is no one there')  # выводим сообщение
    else:
        sort_by_age = sorted(get_by_age, key=by_age_key)   # сортируем по возраста
        for item in sort_by_age:  # пробегаемся по отсортированному списку
            item.show_data()  # выводим очередной экземпляр класса
        write_to_file([item.get_collection() for item in sort_by_age])  # записываем в файл в виде словаря

    # comment for test - just make some changes
    # comment [2] - for test branch_1 branch

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
