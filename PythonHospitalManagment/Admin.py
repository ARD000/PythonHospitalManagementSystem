# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:18:16 2023

@author: ammad
"""
from doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address =''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print("---Hi Welcome to the Hospital Management System---")
        print("---Please Login---")
        #Get the details of the admin

        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        
        if username == self.__username and password == self.__password:
            print("Login successful")
            return True
        else:
            print("Login Failed")
            return False

        # check if the username and password match the registered ones
        

    def find_index(self,index,doctors):        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):            
            return True        
        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter first_name: ")
        surname = input("Enter surname: ")
        speciality = input("Speciality: ")
        
        return first_name, surname, speciality
        

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Input: ")
        

        if op == '1':
            print("-----Register-----")
            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()            

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:                
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    name_exists = True
                    break
                
            if name_exists:
                print('Name already exists.')                                    
            else:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print("Doctor registered successfully")
                               
        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index!=False:
                        break                        
                    else:
                        print("Doctor not found")                    
                        # doctor_index is the ID mines one (-1)                        
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ') # make the user input lowercase
            
            if op == '1':
                new_first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first_name)
                print('First name updated.')

            elif op == '2':
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)
                print('Surname updated.')

            elif op == '3':
                new_speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)
                print('Speciality updated')

            else:
                print('Invalid operation chosen.')            

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            
            try:
                doctor_index = int(doctor_index) - 1
                
                if self.find_index(doctor_index, doctors):
                    doctor = doctors[doctor_index]
                    doctors.remove(doctor)
                    print('Doctor with ID', doctor_index + 1, 'has been deleted.')
                else:
                    print('The id entered is incorrect')

            except ValueError:
                print('The id entered is incorrect')
         
            
    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for patient in patients :
            doctor_full_name = patient.assigned_doctor_full_name if patient.assigned_doctor_full_name else "None"
            print(f'{patient.full_name} | {doctor_full_name} | {patient.age} | {patient.mobile} | {patient.postcode}')


    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1
            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that you would like to assign to the selected patient:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1
            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors) != False:
                doctor = doctors[doctor_index]
                patient = patients[patient_index]
                patient.assigned_doctor_fullname = doctor.full_name
                
                doctor.add_patient(patient)
                patient.link(doctor)
                    
                # link the patients to the doctor and vice versa           
                print('The patient is now assigned to the selected doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')
        
        try:
            patient_index = int(patient_index) - 1
            
            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return
            
            patient = patients[patient_index]
            discharged_patients.append(patient)  
            patients.pop(patient_index)  
            print('The patient has been discharged.')
            
        except ValueError:
            print('The ID entered is incorrect')            
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        for patient in discharged_patients:
            print(patient)


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter new username: ')
            if username == input('Enter new username again: '):
                self.__username = username
                print('Username updated successfully')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print('Password updated successfully')

        elif op == 3:
            address = input('Enter new address: ')
            if address == input('Enter new address again: '):
                self.__address = address
                print('Address updated successfully')

        else:
            print('Invalid input, try again')


