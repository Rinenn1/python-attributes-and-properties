#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Any", breed="Pug"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @property
    def breed(self):
        return self._breed
        
    @name.setter
    def name(self, value):
        if not isinstance (value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = "Any"
        else:
            self._name = value

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
