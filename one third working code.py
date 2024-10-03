#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:28:45 2024

@author: raheeldanish
"""
import pandas as pd
import csv
import datetime

# Define the column names and their desired order
column_order = {
    'home_country': 2,
    'ethnic_group': 3,
    'year_of_birth': 4,
    'age': 5,
    'age_group': 6,
    'course_of_study': 7,
    'course_category': 8,
    'financial_support': 9,
    'financial_problems': 10,
    'family_earning_class': 11,
    'hours_per_week_university_work': 12,
    'stress_before_exams': 13,
    'stress_in_general': 14,
    'form_of_employment': 15,
    'work_hours_per_week': 16,
    'quality_of_life': 17,
    'known_disabilities': 18,
    'alcohol_consumption': 19,
    'well_hydrated': 20,
    'diet': 21,
    'social_media_use': 22,
    'personality_type': 23,
    'exercise_per_week': 24,
    'hours_socialising': 25,
    'total_social_media_hours': 26,
    'total_device_hours': 27,
    'feel_afraid': 28,
    'timetable_preference': 29,
    'ts_impact': 30,
    'ts_full': 31,
    'gender': 32,
    'institution_country': 33,
    'student_type_location': 34,
    'student_type_time': 35,
    'year_of_study': 36,
    'cost_of_study': 37,
    'hours_per_week_lectures': 38,
    'hours_between_lectures': 39,
    'Actual': 40,
    'Predictions': 41
}

# Read the unarranged file
with open('unarranged.csv', 'r') as question_file:
    question_reader = csv.reader(question_file)
    question_data = list(question_reader)

# Create a new file
with open('new_file2.csv', 'w', newline='') as new_file:
    new_writer = csv.writer(new_file)

    # Create a dictionary to map question names to variable names
    question_variable_map = {
        '1. Would you describe your current diet as healthy and balanced?': 'diet',
       '2. What is your ethnic group?': 'ethnic_group',
       '3. How many hours do you spend on university-related work, separate from your Course Timetable, per week during exams?': 'hours_per_week_university_work',
       '4. How would you rate your family class? (family earnings per year)': 'family_earning_class',
       '5. How would you define your quality of life? (as defined by the World Health Organization)': 'quality_of_life',
       '6. How would you define your alcohol consumption?': 'alcohol_consumption',
       '7. Would you consider yourself an introvert or extrovert person? (Definitions from Oxford Languages)': 'personality_type',
       '8. In general, do you feel you experience stress while in the University? (tick all that apply)': 'stress_in_general',
       '9. Would you say that you are normally well hydrated?': 'well_hydrated',
       '10. How often do you exercise per week?': 'exercise_per_week',
       '11. Do you have any known disabilities?': 'known_disabilities',
       '12. How many hours per week do you work?': 'work_hours_per_week',
       '13. What is your main financial support for your studies?': 'financial_support',
       '14. Are you in any form of employment?': 'form_of_employment',
       '15. Do you normally encounter financial issues paying your fees?': 'financial_problems',
       '16. What Country are you from?': 'home_country',
       '17. What is your year of birth?': 'year_of_birth',
       '18. What is your course of study?': 'course_of_study',
       '19. Do you normally feel stressed before exams?': 'stress_before_exams',
       '20. How often in the last week or two did you feel afraid that something awful might happen?': 'feel_afraid',
       '21. If your Course has less than 24 hours on Timetable, would you prefer your timetable to be spread or compact so you have less stress at university? (eg, 1-2 busy days or 3-4 days with less lectures)': 'ts_full' ,
       '22. What are the reasons for your timetable preference?': 'timetable_preference',
       '23. Do you feel your timetabling structure has any impact on your study, life and health?': 'ts_impact',
       '24. How many hours do you spend using technology devices per day (mobile, desktop, laptops, etc)?': 'total_device_hours',
       '25. How many hours do you spend using social media per day (Instagram, Tiktok, Twitter, etc)?': 'total_social_media_hours',
       '26. What year of study are you in?': 'year_of_study',
       '27. How would you describe your biological gender?': 'gender',
       '28. Do you consider physical activity to be helpful to your mental health?': 'exercise_per_week',
       '29. How many hours do you normally have BETWEEN lectures per day?': 'hours_between_lectures',
       '30. How many hours per week do you have active lectures? (Active means attending lectures)': 'hours_per_week_lectures',
       '31. How many hours per week do you socialise? (Meeting other people, participating in social activities etc).': 'hours_socialising',
       '32. Would you classify yourself or have you been diagnosed with mental health issues by a professional?': 'Actual',
       '33. Are you full-time or part-time student?': 'student_type_time',
       '34. Are you a home student or an international student?': 'student_type_location',
       '35.  What are the approximate costs for your studies? (tuition fee per year of study, in pound sterling ¬£)': 'cost_of_study',
    
        
    }


with open('new_file2.csv', 'w', newline='') as new_file:
    new_writer = csv.writer(new_file)
    # Write the header row
    header_row = ['Unnamed: 0', 'sno'] + list(column_order.keys())
    new_writer.writerow(header_row)

    for i, row in enumerate(question_data[1:]):
        new_row = [i, i+1]  # add serial numbers in 'Unnamed: 0' and 'sno'
    
        for variable_name in column_order:
            found = False
            for question, var in question_variable_map.items():
                if var == variable_name:
                    if question in question_data[0]:
                        column_index = question_data[0].index(question)
                        if variable_name == 'year_of_birth':
                            date_of_birth = row[column_index]
                            if isinstance(date_of_birth, str):
                                if '/' in date_of_birth:
                                    try:
                                        dob = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
                                        current_date = datetime.datetime.now()
                                        age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
                                    except ValueError:
                                        age = None
                                else:
                                    try:
                                        age = datetime.datetime.now().year - int(date_of_birth)
                                    except ValueError:
                                        age = None
                            else:
                                age = None
                            bins = [0, 16, 20, 25, 30, 150]
                            labels = ['<16', '16-20', '21-25', '26-30', '>30']
                            if age is not None:
                                age_group = pd.cut([age], bins=bins, labels=labels, right=False)[0]
                            else:
                                age_group = None
                            new_row.append(date_of_birth)  
                            new_row.append(age)
                            new_row.append(age_group) 
                       
                       # REFINING HOURS ONLY 
                       
                        elif variable_name == 'hours_per_week_university_work':
                         hours_per_week = row[column_index]
                         hours_per_week = ''.join(filter(str.isdigit, hours_per_week))
                         new_row.append(hours_per_week)  
                        
                        elif variable_name == 'exercise_per_week':
                         exercise_per_week = row[column_index]
                         exercise_per_week = ''.join(filter(str.isdigit, exercise_per_week))
                         new_row.append(exercise_per_week)  
                        
                        elif variable_name == 'total_social_media_hours':
                         total_social_media_hours = row[column_index]
                         total_social_media_hours = ''.join(filter(str.isdigit, total_social_media_hours))
                         new_row.append(total_social_media_hours) 
                        
                        elif variable_name == 'total_device_hours':
                         total_device_hours = row[column_index]
                         total_device_hours = ''.join(filter(str.isdigit, total_device_hours))
                         new_row.append(total_device_hours) 
                         
                        elif variable_name == 'hours_socialising':
                         hours_socialising = row[column_index]
                         hours_socialising = ''.join(filter(str.isdigit, hours_socialising))
                         new_row.append(hours_socialising) 
                         
                        elif variable_name == 'work_hours_per_week':
                         work_hours_per_week = row[column_index]
                         work_hours_per_week = ''.join(filter(str.isdigit, work_hours_per_week))
                         new_row.append(work_hours_per_week) 
                         
                        elif variable_name == 'hours_per_week_lectures':
                         hours_per_week_lectures = row[column_index]
                         hours_per_week_lectures = ''.join(filter(str.isdigit, hours_per_week_lectures))
                         new_row.append(hours_per_week_lectures) 
                         
                        elif variable_name == 'hours_between_lectures':
                         hours_between_lectures = row[column_index]
                         hours_between_lectures = ''.join(filter(str.isdigit, hours_between_lectures))
                         new_row.append(hours_between_lectures) 
                       
                         
                     # REFINING YES AND NO  
                        
                        elif variable_name == 'stress_in_general':
                         stress_in_general = row[column_index]
                         stress_in_general = stress_in_general.split()[0]
                         new_row.append(stress_in_general)
                        
                        elif variable_name == 'stress_before_exams':
                         stress_before_exams = row[column_index]
                         stress_before_exams = stress_before_exams.split()[0]
                         new_row.append(stress_before_exams)
                         
                        elif variable_name == 'ts_impact':
                         ts_impact = row[column_index]
                         ts_impact = ts_impact.split()[0]
                         new_row.append(ts_impact)
                         
                        elif variable_name == 'quality_of_life':
                         quality_of_life = row[column_index]
                         quality_of_life = quality_of_life.split()[0]
                         new_row.append(quality_of_life)
                         
                
                # SIMPLIFYING LONG TEXTS
                         
                        elif variable_name == 'alcohol_consumption':
                            alcohol_consumption = row[column_index]
                            if alcohol_consumption == 'I don\'t drink alcohol':
                                new_row.append('No Drinks')
                            elif alcohol_consumption == 'My alcohol consumption is below moderate':
                                new_row.append('Below Moderate')
                            elif alcohol_consumption == 'My alcohol consumption is moderate':
                                new_row.append('Moderate')
                            elif alcohol_consumption == 'My alcohol consumption is above moderate':
                                new_row.append('Above Moderate')
                            else:
                                new_row.append('')
                                
                        
                        elif variable_name == 'diet':
                            diet = row[column_index]
                            if diet == 'I think my diet is somewhat inbetween':
                                new_row.append('Somewhat Inbetween')
                            elif diet == 'No, I think my diet is unhealthy':
                                new_row.append('Unhealthy')
                            elif diet == 'Yes, I think my diet is healthy':
                                new_row.append('Healthy')
                            else:
                                new_row.append('')
                                
                                
                        elif variable_name == 'personality_type':
                            personality_type = row[column_index]
                            if personality_type == 'Somewhat in between':
                                new_row.append('Somewhat in-between')
                            elif personality_type == 'Introvert (a quiet person who is more interested in their own thoughts and feelings than spending time with other people)':
                                new_row.append('Introvert')
                            elif personality_type == 'Extrovert (a lively and confident person who enjoys being with other people)':
                                new_row.append('Extrovert')
                            else:
                                new_row.append('')
                                
                                
                        elif variable_name == 'form_of_employment':
                            form_of_employment = row[column_index]
                            if form_of_employment == 'Yes, I am part-time employed':
                                new_row.append('Part Time')
                            elif form_of_employment == 'I am unemployed':
                                new_row.append('Unemployed')
                            elif form_of_employment == 'I am self-employed':
                                new_row.append('Self Employed')
                            elif form_of_employment == 'Yes, I am full-time employed':
                                 new_row.append('Full time')
                            else:
                                new_row.append('')
                                
                        
                        elif variable_name == 'family_earning_class':
                            family_earning_class = row[column_index]
                            if family_earning_class == 'Lower class':
                                new_row.append('Lower class (below √Ç¬£25,000)')
                            elif family_earning_class == 'Middle class':
                                new_row.append('Middle class (√Ç¬£25,000-√Ç¬£54,999)')
                            elif family_earning_class == 'Higher class':
                                new_row.append('Higher class (√Ç¬£55,000-√Ç¬£90,000)')
                            else:
                                new_row.append('')
                                
                                
                        elif variable_name == 'student_type_time':
                            student_type_time = row[column_index]
                            if student_type_time == 'I am a full-time student':
                                new_row.append('Full Time')
                            elif student_type_time == 'I am a part-time student':
                                new_row.append('Part Time')
                            elif student_type_time == 'I am unsure':
                                new_row.append('I am unsure')
                            else:
                                new_row.append('')
                                
                                
                        elif variable_name == 'year_of_study':
                            year_of_study = row[column_index]
                            if student_type_time == 'Foundation year':
                                new_row.append('Foundation year')
                            elif year_of_study == 'Level 4 (first year, undergraduate)':
                                new_row.append('Undergraduate 1st year')
                            elif year_of_study == 'Level 5 (second year, undergraduate)':
                                new_row.append('Undergraduate 2nd year')
                            elif year_of_study == 'Level 6 (third year, undergraduate)':
                                new_row.append('Undergraduate 3rd year')
                            elif year_of_study == 'Level 7 (postgraduate)':
                                 new_row.append('Postgraduate 1st year')
                            else:
                                new_row.append('')
                                
                         
                         
          #              elif variable_name == 'timetable_preference':
           #                 timetable_preference = row[column_index]
            #                if timetable_preference.lower() == 'I prefer my timetable to be compact. (having all my classes in one day or two days in the week)':
             #                   new_row.append('Compact')
              #              elif timetable_preference.lower() == 'I prefer my timetable to be spread with long gaps in between classes (eg, 1-2 modules per day, spread over 3 times per week)':
               #                 new_row.append('Spread')
                #            else:
                 #               new_row.append('')
                    
            
                                             
                        elif variable_name == 'Actual':
                            actual_value = row[column_index]
                            row.append(actual_value)  # keep the 'Actual' value
                            if actual_value.lower() == 'yes':
                                Prediction = 1  # append 1 to 'Prediction' column
                            else:
                                Prediction = 0  # append 0 to 'Prediction' column
                        else:
                            new_row.append(row[column_index])  # match the order of column_order
                    else:
                        new_row.append('')
                    found = True
                    break
            if not found:
                new_row.append('')
        
                # Add the 'Prediction' value to the new row
        
        new_row.append(Prediction)
    
        
        # Remove the gap of two columns after 'age_group'
        new_row = new_row[:7] + new_row[9:]
        
        new_writer.writerow(new_row)  # write the new row to the file
