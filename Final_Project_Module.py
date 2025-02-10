#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Jorge Ceballos
Final Project Module
"""

#this is my module file with all my functions that is imported in the main program file
def display_menu(): #defining the display_menu function
    print("\nSelect an option:") #print statement for asking which option
    print("1. Add or Modify Data") # option one for if they want to add or modify data
    print("2. Finish and Display Output File") #print statement for option 2 for if they want to exit the program

def view_census_data(total_population, age_data, gender_data, education_levels, education_data, industry_types, employment_data):#view_census_data function with parameters to be used 
    #this displays data for texas
    print("\nTexas Census Data:")
    print(f"Total Population: {total_population}")
    print(f"Subtotals by Age:")
    print(f"  0-19: {age_data[0]}\n  20-29: {age_data[1]}\n  30-44: {age_data[2]}\n  45-64: {age_data[3]}\n  65+: {age_data[4]}") #subtotals with age by using age_data list and getting each value from the idnex of the list
    print(f"Subtotals by Gender:")
    print(f"  Male: {gender_data[0]}\n  Female: {gender_data[1]}") #getting the value from hender_data list by getting the index 
    print(f"Subtotals by Education (%):")
    for level, percentage in zip(education_levels, education_data): #for loop taking the education level and percentage from value passed into function. the zip function combines the 2 listselement by element so it becoems a pair
        print(f"  {level}: {percentage}%") #ptints each education level with its percentage for all education levels
    print(f"Employment by Industry (%):")
    for industry, percentage in zip(industry_types, employment_data): #for loop taking the industry tyoe and percentage from values passed to function. THe zip function combines the 2 lists element by elementso industry will be the first element of the first list and percentage will be the first element in the second list
        print(f"  {industry}: {percentage}%") #fprint statement with the industry name and its percentage

def view_health_industry_data(health_data, health_industry_keys, health_industry_data): #defining function to view the health industry data with parameters which will be arguments passed when function is called in the main program 
    
    print("\nTexas Health Industry Data:")
    print(f"Cancer Death Rate: {health_data[0]} per 100,000") #f print statement with the first element in health_data list
    print(f"Heart Disease Death Rate: {health_data[1]} per 100,000") #f print statement with the second element in health_data list
    print("Key Statistics:")
    for stat, value in zip(health_industry_keys, health_industry_data): #for loop taking the chosen category and value and combing the lists with the zip function 
        print(f"  {stat}: {value}") #displays the statistic and its value

def calculate_impact(stored_value, user_value): #defining function which calculates the impact, difference and percentage change. with parameters which are the stored value and the new user_value
    try: #try statement 
        difference = user_value - stored_value #calculates the difference from the new and old value
        percentage_change = (difference / stored_value) * 100 if stored_value != 0 else 0 #calculates the change percentage
        impact_message = "Positive" if difference > 0 else "Negative" #impact message variable which is positive if the difference is greater than zero. otherwise its negative
        return difference, percentage_change, impact_message #returns these 3 variables
    except ZeroDivisionError: #except for if the user enters the same value
        return 0, 0, "Neutral"

def write_to_file(variable, stored, user, difference, percentage, message): #defining write to output file function with these paramters

    with open("output.txt", "a") as file: #opens the output.txt file and appends with "a"
        file.write(f"Variable Changed: {variable}\n") #chosen variable changed
        file.write(f"Stored Value: {stored}\n")  #stored or original value
        file.write(f"User Value: {user}\n") #the new user value
        file.write(f"Difference: {difference}\n") #writes the difference
        file.write(f"Percentage Change: {percentage:.2f}%\n") #writes the percentage change with fprint. 2 decimal places
        file.write(f"Impact: {message}\n") #impact message
        file.write("\n")

def display_output_file(): #defining display output file
  
    try: #try statement to display output file
        with open("output.txt", "r") as file: #opens output file to read with "r"
            print("\n--- Output File Content ---") #title
            print(file.read()) #file.read to display output file contents
    except FileNotFoundError: #except statement for if file is not found
        print("\nOutput file not found. No data has been recorded yet.")

