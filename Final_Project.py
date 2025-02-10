1#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Jorge Ceballos
Final Project
"""



import Final_Project_Module as fpm #importing the module file with all the functions except the main function


def main(): #defining main function
   
    with open("output.txt", "w") as file:  # this clears the output file at the start of my program with "w" so it's blank after each time its run
        file.write("Texas Industry Analysis - Output File\n")  #title for output
        file.write("=" * 50 + "\n\n")
    
    total_population = 29145505 #total population variable that will be passed to function later
   
    age_data = [8253343, 4186118, 6163429, 6871475, 3451949] #age data list that will be passed to function later

    gender_data = [14307610, 14618704] #gender data list that will be passed to function later

    education_levels = [ #education levels list that will be passed to function later
        "Less than High School",
        "High School or equivalent degree",
        "Some college",
        "Associate's Degree",
        "Bachelor's Degree",
        "Graduate or Professional Degree",
        ]

    education_data = [13.7, 24.2, 19.8, 8.1, 21.6, 12.6] #education data list that will be passed to function later

    industry_types = [ #employment data list that will be passed to function later
        "Educational Services, Health Care, and Social Assistance",
        "Professional, Scientific, and management, and administrative, and waste management services",
        "Retail Trade",
        "Manufacturing",
        "Arts, Entertainment, and Recreation, and accommodation, and food services",
        "Construction",
        "Finance and Insurance, and real estate, and rental and leasing",
        "Transportation and Warehousing, and utilities",
        "Public Administration",
        "Other Services",
    ]

    employment_data = [21.7, 13.1, 10.8, 8.7, 8.5, 8.4, 7.1, 6.8, 3.9, 4.8] #employment data list that will be passed to function later. these are percentages for job types above

    health_data = [145, 169] #health data list. these are rates for the 2 health concerns

    health_industry_keys = [ #these are the new added 5 important data facts about the health industry as insturcted
        "Total Healthcare Workers",
        "Revenue Healthcare Industry makes for Texas",
        "Total Hospitals",
        "Annual Patients (customers)",
        "Obesity Rate",
    ]

    health_industry_data = [992990, 104000000000, 650, 20000000, 37.4] #these are the numbers for the above health industry stats

    print("\n--- Initial Data ---") #this presents the census and health industry data by passing all the above lists and variables to the functions
    fpm.view_census_data(total_population, age_data, gender_data, education_levels, education_data, industry_types, employment_data) #view_census_data function to present the data with fpm which gets it from my imported module
    fpm.view_health_industry_data(health_data, health_industry_keys, health_industry_data) # view_health_industry_data function to present the data with fpm which gets it from my imported module
    
    while True: #while loop to keep repeating the program until the user chooses to exit
        fpm.display_menu() #calling display menu function which asks the user what they want to do
        choice = input("Enter your choice: ") #user input for them to input the integer for their choice

        if choice == "1": #if statement for user choice
            print("\nDo you want to modify Census Data or Health Industry Data?") #print statement asking which data they would like to change
            data_choice = input("Enter 'Census' or 'Health': ").strip().lower() #input asking them to type in census or health and strip gets rid of any spaces and lower() converts to lowercase

            if data_choice == "census": #if they want to change census data
                print("\nCensus Data Categories:") #prints a list of the categories they can change with numbers for each
                print("1. Total Population")
                print("2. Age Distribution")
                print("3. Gender Distribution")
                print("4. Education Levels")
                print("5. Employment by Industry")

                category = input("Select a category number to modify: ") #input asking for which category they want to chnage

                if category == "1": #if statement asking for which category they chose, the rest of the if statements are for the same thing
                    stored_value = total_population #stores the total_population variable that I gave and stores it in stored_value variable
                    variable = "Total Population" #this is the chosen variable or category which I use later on
                elif category == "2":
                    index = int(input("Select Age Group (0 for 0-19, 1 for 20-29, etc.): ")) #input asking for which specific age group pupolation they want to change
                    stored_value = age_data[index] #stores the age_data for the chosen group in the stored_value variable
                    variable = f"Age Group {index}" #this is the chosen variable or category which I use later on
                elif category == "3":
                    index = int(input("Select Gender (0 for Male, 1 for Female): ")) #input for gender distribution asking if they want to change male or female data
                    stored_value = gender_data[index] #storing the data for either male or female data in the stored_value variable
                    variable = "Male" if index == 0 else "Female" #this is the chosen variable or category which I use later on
                elif category == "4":
                    index = int(input("Select Education Level (0 for Less than High School, etc.): ")) #input asking for which data in the education level they want to change
                    stored_value = education_data[index] #storing the chosen education level in the srored_value variable
                    variable = education_levels[index] #this is the chosen variable or category which I use later on
                elif category == "5":
                    index = int(input("Select Industry (0 for Educational Services, etc.): ")) #input asking for which industry data they want to change
                    stored_value = employment_data[index] #storing the chosen industry in the stored_value variable
                    variable = industry_types[index] #this is the chosen variable or category which I use later on
                else:
                    print("Invalid category.")
                    continue

            elif data_choice == "health": #same thing but now if they chose to change health industry data
                print("\nHealth Industry Data Categories:") #list asking which category they would like to change
                print("1. Cancer Death Rate")
                print("2. Heart Disease Death Rate")
                print("3. Total Healthcare Workers")
                print("4. Revenue")
                print("5. Total Hospitals")
                print("6. Annual Patients")
                print("7. Obesity Rate")

                index = int(input("Select a category number to modify: ")) #input for which category they would like to modify
                if index in [1, 2]: #if statemnet for ut they chose one of the health concerns from project 1
                    stored_value = health_data[index - 1] #minus one because python index starts with 0
                    variable = "Cancer Death Rate" if index == 1 else "Heart Disease Death Rate" #storing the chosen concern in variable
                elif 3 <= index <= 7: #else if stateent for the new 5 pieces of industry data added for the final project
                    stored_value = health_industry_data[index - 3] #storing the chosen variable and subtrating 3 because this is a new list
                    variable = health_industry_keys[index - 3] #storing the chosen industry number in variable
                else:
                    print("Invalid category.")
                    continue
            else: #if they dont input either census or health
                print("Invalid choice.")
                continue

            user_value = float(input(f"Enter your hypothetical value for {variable}: ")) #input for what they user wants the new value for their chosen category to be 
            
            # Calculate impact
            difference, percentage_change, impact_message = fpm.calculate_impact(stored_value, user_value) #calling the function that calculates the difference and percentage change by passing the stored value and the user value and returning it into these 3 variables

            # Write to output file
            fpm.write_to_file(variable, stored_value, user_value, difference, percentage_change, impact_message) #calling function that writes the new data and calculations to the output file

            # Update the stored data
            if data_choice == "census": #if statement for if the user chose census 
                if category == "1": #the folowing are if and else if statements storing the user inputed value in the variable
                    total_population = user_value
                elif category == "2":
                    age_data[index] = user_value
                elif category == "3":
                    gender_data[index] = user_value
                elif category == "4":
                    education_data[index] = user_value
                elif category == "5":
                    employment_data[index] = user_value
            elif data_choice == "health": #else if statement for if the user chose to change health data
                if index in [1, 2]:
                    health_data[index - 1] = user_value #for if they chose one of the 2 concerns
                else:
                    health_industry_data[index - 3] = user_value # storing the user value in the chosen variable they chose to change

            print(f"\nImpact for {variable} recorded. Difference: {difference}, Percentage Change: {percentage_change:.2f}%, Impact: {impact_message}") #f print statement telling the user what was changed and the difference, percentage change and if its positive or negative

        elif choice == "2": #if they choose #2 in the display menu
            
            fpm.display_output_file() #calls the function to display the final output file
            print("\n")
            print("Exiting the program. Goodbye!") #lets them know the program is being exited
            break
        else:
            print("Invalid choice. Please select a valid option.")
                
      

if __name__ == '__main__': #if statement to make sure this is the main program and not a module
    main() #calling the main function
