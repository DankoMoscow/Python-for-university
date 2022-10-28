import random
key_list = ['w', 'a', 's', 'd']

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
    def __str__(self):
        return f'Размеры поля: {int(self.width)}, {int(self.height)}'
   
    def update_field(self, first_coor, second_coor, first_coor_monster, second_coor_monster):
        field = [['0' for x in range(self.width)] for y in range(self.height)]                   
        field[second_coor-1][first_coor-1] = '1' 
        field[second_coor_monster-1][first_coor_monster-1] = '*' 
        for line in field:
            print(' '.join(line))        
       
    def print_field(self):
        field = [['0' for x in range(self.width)] for y in range(self.height)]
        for line in field:
            print(' '.join(line))

class Coordinate:  
    def __init__(self, first_coor: int, second_coor: int):
        self.first_coor = first_coor
        self.second_coor = second_coor

       
    def __str__(self):
        return f'Координаты: {int(self.first_coor)}, {int(self.second_coor)}'
   
    def set_coordinates(self):
        print(f'текущие координаты: {int(self.first_coor)}, {int(self.second_coor)}')
        if self.first_coor > width or self.second_coor > height or self.first_coor == 0 or self.second_coor == 0:
            raise Exception("Выход за пределы поля!")
            
        return self.first_coor, self.second_coor
   
class Character:  
    def __init__(self, first_coor, second_coor):
        self.first_coor = first_coor
        self.second_coor = second_coor
       
    def __str__(self):
        return f'Новые координаты персонажа: {int(self.first_coor)}, {int(self.second_coor)}'
       
    def move(self, direction):
        if direction == 'w':
            if self.second_coor > 1:
                self.second_coor -= 1
            else:
                self.second_coor = self.second_coor
      
        elif direction == 's':
            if self.second_coor < height:
                self.second_coor += 1
            else:
                self.second_coor = self.second_coor

        elif direction == 'd':
            if self.first_coor < width:
                self.first_coor += 1
            else:
                self.first_coor = self.first_coor

        elif direction == 'a':
            if self.first_coor > 1:
                self.first_coor -= 1
            else:
                self.first_coor = self.first_coor 
            
            
            
class Monster(Character):
    def __init__(self, first_coor_monster, second_coor_monster):
        self.first_coor_monster = first_coor_monster
        self.second_coor_monster = second_coor_monster
        
    def __str__(self):
        return f'Новые координаты монстра: {int(self.first_coor_monster)}, {int(self.second_coor_monster)}'
                
    def move(self):
        global key_list, direction
        direction = random.choices(key_list)[0]
        if direction == 'w':
            if self.second_coor_monster > 1:
                self.second_coor_monster -= 1
            else:
                self.second_coor_monster = self.second_coor_monster
      
        elif direction == 's':
            if self.second_coor_monster < height:
                self.second_coor_monster += 1
            else:
                self.second_coor_monster = self.second_coor_monster

        elif direction == 'd':
            if self.first_coor_monster < width:
                self.first_coor_monster += 1
            else:
                self.first_coor_monster = self.first_coor_monster

        elif direction == 'a':
            if self.first_coor_monster > 1:
                self.first_coor_monster -= 1
            else:
                self.first_coor_monster = self.first_coor_monster 
    
    
def main():    
    global width, height
    width = (input('Введите ширину: '))
    while width.isnumeric() == 0:
        print('Введите корректное значение, типа int')
        width = input('Введите ширину: ')
    width = int(width)    
    
    height = (input('Введите высоту: '))   
    while height.isnumeric() == 0:
        print('Введите корректное значение, типа int')
        height = input('Введите высоту: ')
    height = int(height)   
        
    field_1 = Field(width, height)
    print(field_1.__str__())
    field_1.print_field()
    
    first_coor = int(input('Введите первую координату: '))
    while first_coor> width or first_coor < 1:
        first_coor = int(input(f'Координата персонажа должна быть числом от 1 до {width}: '))
    
    
    second_coor = int(input('Введите вторую координату: '))
    while second_coor > width or second_coor < 1:
        second_coor = int(input('Координата персонажа должна быть числом от 1 до {height}:  '))
       
    
    first_coor_monster = random.randint(1, width)   
    second_coor_monster = random.randint(1, height)  
    
    if first_coor == first_coor_monster and second_coor == second_coor_monster:
        print('Game over')
    else:
        coordinate = Coordinate(first_coor, second_coor)
        coordinate_monster = Coordinate(first_coor_monster, second_coor_monster)
        
        character = Character(first_coor, second_coor)
        monster = Monster(first_coor_monster, second_coor_monster)
        
        print('Персонаж:')
        first_coor_current, second_coor_current = coordinate.set_coordinates()
        print('Монстр:')
        first_coor_monster_current, second_coor_monster_current = coordinate_monster.set_coordinates()
           
        key = input('Введите направление движения персонажа: w/a/s/d. Если хотите выйти - нажмите p: ')
        while key != 'p': 
            while key not in key_list:
                print('Направление движения некорректно')
                key = input('Введите направление движения персонажа: w/a/s/d ') 
                     
            character.move(key)
            if key == 'w' and character.second_coor <= 1:
                print("Нельзя выходить за пределы поля. Положение не изменилось")
            elif key == 's' and character.second_coor >= height:
                print("Нельзя выходить за пределы поля. Положение не изменилось")
            elif key == 'd' and character.first_coor >= width:
                print("Нельзя выходить за пределы поля. Положение не изменилось")
            elif key == 'a' and character.first_coor <= 1:
                print("Нельзя выходить за пределы поля. Положение не изменилось")

            monster.move()
            if direction == 'w' and monster.second_coor_monster <= 1:
                print("Замечена попытка монстра слинять за пределы поля. Положение не изменилось")
      
            elif direction == 's' and monster.second_coor_monster >= height:
                print("Замечена попытка монстра слинять за пределы поля. Положение не изменилось")
    
            elif direction == 'd' and monster.first_coor_monster >= width:
                print("Замечена попытка монстра слинять за пределы поля. Положение не изменилось")
    
            elif direction == 'a' and monster.first_coor_monster <= 1:
                print("Замечена попытка монстра слинять за пределы поля. Положение не изменилось")
                    
                
            coordinate = Coordinate(character.first_coor, character.second_coor) 
            coordinate_monster = Coordinate(monster.first_coor_monster, monster.second_coor_monster)
            
            first_coor_current, second_coor_current = coordinate.set_coordinates()   
            first_coor_monster_current, second_coor_monster_current = coordinate_monster.set_coordinates()
            
            field_1.update_field(first_coor_current, second_coor_current,  first_coor_monster_current, second_coor_monster_current)
            if first_coor_current == first_coor_monster_current and second_coor_current == second_coor_monster_current:
                print('Game over, monster has eaten you, лооооооох')
                break 
            enter = input('Нажмите ENTER для следующего хода')
            if enter == '':  
                key = input('Введите направление движения персонажа: w/a/s/d. Если хотите выйти - нажмите p: ')
main()                