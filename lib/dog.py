#!/usr/bin/env python3

class Dog:
   def __init__(self, name,breed = "Mutt"):
       self.name = name
       self.breed = breed
Lunar = Dog("Lunar","Husky")
print(Lunar.name)
print(Lunar.breed)
