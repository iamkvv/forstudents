from random import randint
import pandas as pd


class Drom:
  def __init__(self, cnt_cars, sc_cls):
    self.cars=[]
    self.race_name = 0
    self.df_empty= pd.DataFrame({}, index=[])

    for i in range(cnt_cars):
      self.cars.append(sc_cls("0-0-" + str(i + 1),  self)) #создаем экз-ры указанного класса
  
  def _clear_car_dist(self): #приватный метод
   for car in self.cars:
     car.dist = 0

  def race(self): #Запустим гонку
    self.race_name += 1 #Имя гонки
    self._clear_car_dist() #Обнулим счетчики машин

    for i in range(5): #5 заездов
      for car in self.cars:
        car.move()
    
    # получим DataFrame текущей гонки
    df_curr = pd.DataFrame({ car.number:[car.dist] for car in self.cars},  index = [self.race_name]) 
    self.df_empty = pd.concat([self.df_empty,df_curr])  #и добавим его к предыдущим рез-м
  


class Car:
  def move(self):
    self.dist += randint(0,10)

class SportCar(Car):
  def __init__(self, number, drom ):
    self.dist = 0
    self.number = number
    self.autodrom = drom
  
  def __str__(self):
    #срабатывает при использовании print(c)
      return f'Авто1: {self.number}; Расстояние1: {self.dist}' 
  def __repr__(self):
    #срабатывает при указании имени экз-ра
      return f'Авто: {self.number}; Расстояние: {self.dist}' 