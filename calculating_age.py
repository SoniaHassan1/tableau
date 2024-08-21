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

    # Iterate over the rows in the unarranged file
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
                            if '/' in date_of_birth:
                                dob = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
                                current_date = datetime.datetime.now()
                                age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
                            else:
                                age = datetime.datetime.now().year - int(date_of_birth)
                            new_row.append(row[column_index])
                            new_row.append(age)
                        else:
                            new_row.append(row[column_index])
                    else:
                        new_row.append('')
                    found = True
                    break
            if not found:
                new_row.append('')
        new_writer.writerow(new_row)
        
