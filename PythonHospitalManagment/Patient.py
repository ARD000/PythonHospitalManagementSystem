# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:10:46 2023

@author: ammad
"""

class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """       
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.postcode = postcode
        self.symptoms = []
        self.__doctor = 'None'
        
               
    def full_name(self) :
        """full name is first_name and surname"""
        full_name = self.first_name + " " + self.surname
        return full_name
    
    def get_doctor(self) :
        return self.__doctor
            
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
        
    def print_symptoms(self):
        """prints all the symptoms"""
        for symptom in self.symptoms:
            print(symptom)
        
    def __str__(self):
        doctor_name = self.__doctor if self.__doctor else 'Not Assigned'
        return f'{self.full_name():^30}|{str(doctor_name):^30}|{self.age:^5}|{self.mobile:^15}|{self.postcode:^10}'

