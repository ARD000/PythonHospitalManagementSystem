# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:23:15 2023

@author: ammad
"""


# Imports
from Admin import Admin
from doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin', '123', 'B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone' , 'Carlos', 'Cardiology')]
    patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'), Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'), Patient('Daivd', 'Smith', 15, '07123456789', 'C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print("-----Main Menu-----")
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View Patients')
        print(' 3- Discharge patients')
        print(' 4- View discharged patients')
        print(' 5- Assign doctor to a patient')
        print(' 6- Update admin details')
        print(' 7- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)
            # 1- Register/view/update/delete doctor
         

        elif op == '2':
            print('ID |          Full Name           |      Doctor`s Full Name & Specialty      | Age |    Mobile     | Postcode ')
            admin.view(patients)
            # 2 - patients
        elif op == '3':     # 3 - discharge patients
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)
                elif op == 'no' or op == 'n':
                        break
                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '4':
            admin.view_discharge(discharged_patients)
            # 4 - view discharged patients
        elif op == '5':
            # 5- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '6':
            # 6- Update admin detais
            admin.update_details()
        elif op == '7':
            break
            # 7 - Quit

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()

