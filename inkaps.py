"""С использованием инкапсуляции создать класс персонажа со следующими характеристиками: \
    пара координат, здоровье и имя. Считается, что здоровье можно менять только в пределах от 0 до 100, \
            имя неизменяемо и задается один раз, а пара координат может меняться не через сеттер,\
                а через метод Move в зависимости от заданного направления. Сам метод Move должен \
    менять координаты и выводить надпись формата
Персонаж <CharacterName> переместился из точки (0,0) в точку (1,0). Текущее здоровье - 100"""


class Character:
    def __init__(self):
        self.__name = 'Персонаж 1'
        self.__health = 100
        self.__X0 = 0
        self.__Y0 = 0

    def get_health(self):
        return self.__health

    def get_health(self, value):
        if value < 0 or value > 100:
            print('Ошибка')
        else:
            self.__health = value

    def start_move(self, direction):
        if direction == 'w' or direction == 'W':
            self.__Y0 += 1
        elif direction == 's' or direction == 'S':
            self.__Y0 -= 1
        elif direction == 'a' or direction == 'A':
            self.__X0 -= 1
        elif direction == 'd' or direction == 'D':
            self.__X0 += 1
        else:
            print('Направление некорректно')
        print(f'Персонаж {self.__name} переместился в точку {self.__X0, self.__Y0}. Текущее здоровье {self.__health}')

def main():
    person = Character()
    while True:
        direction = input('Введите напраление "w", "a", "s", "d" или (-) чтобы закончить: ')
        if direction == '-':
            print('До новых встреч')
            break
        person.start_move(direction)

main()