import numpy as np
from numpy import random

list_names = [['Даня', 'Панк', 5], ['Саша', 'Панк', 4],['Маша', 'Отличник', 5] ]


class Student:
    def __init__(self, name, behavior, grades):
        self.name = name
        self.behavior = behavior
        self.grades = grades  
        self.lev_energy = 10
        self.lev_intell = 10
        self.lev_happy = 10

    def Behavior_get(self):
        return self.behavior
    
    def gen_health(self):  
        self.health = random.randint(0,101)
        return self.health
    
    def get_health(self):
        print('Уровень начального здоровья: ', self.health)
        return self.health
        
    def happy_start(self):
        if self.behavior == 'Отличник':
            self.lev_happy = 100

        elif self.behavior == 'Троечник':
            self.lev_happy = 80

        elif self.behavior == 'Панк':
            self.lev_happy = 1000

        print('Уровень начального счастья: ', self.lev_happy)
        return self.lev_happy
        
    def energy(self):
        if self.behavior == 'Отличник':
            self.lev_energy = 100

        elif self.behavior == 'Троечник':
            self.lev_energy = 80
                    
        elif self.behavior == 'Панк':
            self.lev_energy = 1000

        print('Уровень начальной энергии: ', self.lev_energy)
        return self.lev_energy
        
    def intelligent(self):
        if self.behavior == 'Отличник':
            self.lev_intell = 100
        
        elif self.behavior == 'Троечник':
            self.lev_intell = 50
        
        elif self.behavior == 'Панк':
            self.lev_intell = 10

        print('Уровень начального интеллекта:', self.lev_intell)
        return self.lev_intell
    
    def progress(self):        
        if self.grades >= 4 and self.lev_intell >= 40 and self.lev_energy >= 50:
            number_grades = 'High'
        else:
            number_grades = 'Low'
        print(f'Оценка в период обучения: {number_grades}') 
        
        
class Game():
    def __init__(self):
        for i in range(len(list_names)):
            student1 = Student(list_names[i][0],list_names[i][1],list_names[i][2])
            print('\n***')
            print(student1.name)
            student1.gen_health()
            student1.get_health()
            student1.happy_start()
            student1.intelligent()
            student1.energy()
            student1.progress()
            print('***')
        
            day = 1

            for j in range(days):
                print(f'\nДень:{day}')
                number_chance = random.randint(0,101)        
                
                if student1.lev_intell <= 0 or student1.lev_energy <= 0 or student1.lev_happy <= 0 or student1.health <= 0:
                    day += 1 
                    print ('Студент скоропостижно скончался')
                    
                elif student1.lev_intell > 0 and student1.lev_energy > 0 and student1.lev_happy > 0 and student1.health > 0:
                    
                    if student1.behavior == 'Отличник' and 0 < number_chance < 31:
                        doing = 'Делает дз'
                        student1.lev_intell += 1
                        student1.lev_energy -= 1
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy} ')
                    
                    elif student1.behavior == 'Отличник' and 30 < number_chance < 81:
                        doing = 'Усердно трудится'
                        student1.lev_intell += 5
                        student1.lev_energy -= 3
                        student1.lev_happy -=3
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy}, и уровень счастья: {student1.lev_happy} ')
                        
                    elif student1.behavior == 'Отличник' and 80 < number_chance < 101:
                        doing = ' Пьёт и веселится'
                        student1.lev_intell += 2
                        student1.lev_energy -= 10
                        student1.lev_happy +=15
                        student1.health -= 2
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy},  уровень счастья: {student1.lev_happy} и уровень жизни: {student1.health}')
                    
                    elif student1.behavior == 'Троечник' and 0 < number_chance < 51:
                        doing = 'Делает дз'
                        student1.lev_intell += 1
                        student1.lev_energy -= 1
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy}')
                      
                    elif student1.behavior == 'Троечник' and 50 < number_chance < 91:
                        doing = ' Пьёт и веселится'
                        student1.lev_intell += 2
                        student1.lev_energy -= 10
                        student1.lev_happy +=15
                        student1.health -= 2
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy},  уровень счастья: {student1.lev_happy} и уровень жизни: {student1.health}')            
                         
                    elif student1.behavior == 'Троечник' and 90 < number_chance < 101:
                        doing = ' Разочаровался в жизни и хочет умереть'
                        student1.lev_happy -=10
                        student1.health -= 5
                        print(f'Что делает студент: {doing}, его изменённый уровень счастья: {student1.lev_happy} и уровень жизни: {student1.health}')             
                        
                        
                    elif student1.behavior == 'Панк' and 0 < number_chance < 96:
                        doing = 'Ходит на концерты, пьёт и наслаждается жизнью'  
                        student1.lev_intell -= 3
                        student1.lev_energy -= 3
                        student1.lev_happy +=10
                        student1.health -= 2
                        print('Я панк, мне пофиг')
                        print(f'Что делает студент: {doing}, его изменённый уровень интеллекта: {student1.lev_intell}, а также уровень энергии: {student1.lev_energy},  уровень счастья: {student1.lev_happy} и уровень жизни: {student1.health}')
                            
                    elif student1.behavior == 'Панк' and 95 < number_chance < 101:
                        doing = 'Умер от некачественного алкоголя'  
                        student1.lev_intell = 0
                        student1.lev_energy = 0
                        student1.lev_happy = 0
                        student1.health = 0
                        
                    if student1.grades >= 4 and student1.lev_intell >= 40 and student1.lev_energy >= 50:
                        number_grades = 'High'
                    else:
                        number_grades = 'Low'
                    print(f'Оценка в период обучения: {number_grades}') 
                    day += 1 
                    
def main(): 
    global days                
    print(f'Участники игры -Сдохни или умри-: {list_names[0][0], list_names[1][0] , list_names[2][0]    }')
    days = int(input('Введите количество дней пребывания в игре: '))

    process = Game()

main()

