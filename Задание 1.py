#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Поле first — целое положительное число, номинал купюры; номинал может принимать
# значения 1, 2, 5, 10, 50, 100, 500, 1000, 5000. Поле second — целое положительное число,
# количество купюр данного достоинства. Реализовать метод summa() — вычисление
# денежной суммы.


class TaskOne:
   c = {}
   summ = 0
   b = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]

   def __init__(self):
      self.first = 0
      self.second = 0

   def read(self, prompt=None):
      self.first = input('Введите номинал купюры: ') if prompt is None else input(prompt)
      if int(self.first) in TaskOne.b:
         self.second = input('Введите количество купюр данного номинала: ') if prompt is None else input(prompt)
         TaskOne.c[self.first] = self.second
      else:
         print("Такого номинала нет в списке")

   def display(self):
      print(self.make_summa())
 
   def make_summa(self):
      for k, i in TaskOne.c.items():
         TaskOne.summ += int(k) * int(i)
      TaskOne.c = {}
      return TaskOne.summ
      

if __name__ == '__main__':
   print("Список доступных номиналов: 1, 2, 5, 10, 50, 100, 500, 1000, 5000")
   while True:
      r2 = TaskOne()
      r2.read()
      r2.display()
