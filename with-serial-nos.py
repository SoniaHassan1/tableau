import csv

# Read the question file
with open('unarranged.csv', 'r') as question_file:
    question_reader = csv.reader(question_file)
    question_data = list(question_reader)

# Read the processed file
with open('processed_file.csv', 'r') as processed_file:
    processed_reader = csv.reader(processed_file)
    processed_data = list(processed_reader)

# Create a new file
with open('new_file2.csv', 'w', newline='') as new_file:
    new_writer = csv.writer(new_file)

    # Get the column names from the processed file
    processed_column_names = processed_data[0]

    # Create a dictionary to map question names to variable names
    question_variable_map = {
        '1. Would you describe your current diet as healthy and balanced?': 'diet',
        '2. What is your ethnic group?': 'ethnic_group',
        '3. How many hours do you spend on university-related work, separate from your Course Timetable, per week during exams?': 'hours_per_week_university_work',
        '4. How would you rate your family class? (family earnings per year)': 'family_earning_class',
        '5. How would you define your quality of life? (as defined by the World Health Organization)': 'quality_of_life',
        '6. How would you define your alcohol consumption?': 'alcohol_consumption',
        '7. Would you consider yourself an introvert or extrovert person? (Definitions from Oxford Languages)': 'personality_type',
        '8. In general, do you feel you experience stress while in the University? (tick all that apply)': 'tress_in_general',
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
        '19. Do you normally feel stressed before exams?': 'tress_before_exams',
        '20. How often in the last week or two did you feel afraid that something awful might happen?': 'feel_afraid',
       
        # Add/Edit more questions as needed
    }

    # Map processed column names to variable names
    variable_names = []
    for column_name in processed_column_names:
        for question, variable_name in question_variable_map.items():
            if column_name in question:
                variable_names.append(variable_name)
                break
        else:
            variable_names.append(column_name)

    # Write the header row
    new_writer.writerow(processed_column_names)

    # Iterate over the rows in the question file
    for i, row in enumerate(question_data[1:]):
        row[0] = str(i)
        row[1] = str(i+1)
        new_writer.writerow(row)
