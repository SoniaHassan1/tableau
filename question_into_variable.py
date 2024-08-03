#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:16:33 2024

@author: raheeldanish
"""

import csv

# Read the question file
with open('question.csv', 'r') as question_file:
    question_reader = csv.reader(question_file)
    question_data = list(question_reader)

# Read the processed file
with open('processed_file.csv', 'r') as processed_file:
    processed_reader = csv.reader(processed_file)
    processed_data = list(processed_reader)

# Create a new file
with open('new_file1.csv', 'w', newline='') as new_file:
    new_writer = csv.writer(new_file)

    # Get the column names from the processed file
    processed_column_names = processed_data[0]

    # Get the column names from the question file
    question_column_names = question_data[0]

    # Create a dictionary to map question types to variable types
    question_type_map = {
        'Single Answer': 'tring',
        'Multiple Answer': 'list',
        'Rating Scale': 'int',
        'Open-Ended': 'tring',
        # Add more question types as needed
    }

    # Write the header row
    new_header_row = []
    for column_name in processed_column_names:
        if column_name in question_column_names:
            question_type = question_data[0][question_column_names.index(column_name)]
            variable_type = question_type_map.get(question_type, 'tring')
            new_header_row.append(f'{column_name} ({variable_type})')
        else:
            new_header_row.append(column_name)
    new_writer.writerow(new_header_row)

    # Iterate over the rows in the question file
    for row in question_data[1:]:
        new_row = []
        for column_name in processed_column_names:
            if column_name in question_column_names:
                column_index = question_column_names.index(column_name)
                question_type = question_data[0][column_index]
                variable_type = question_type_map.get(question_type, 'tring')
                if variable_type == 'tring':
                    new_row.append(row[column_index])
                elif variable_type == 'list':
                    new_row.append(eval(row[column_index]))  # Convert to list
                elif variable_type == 'int':
                    new_row.append(int(row[column_index]))
                else:
                    new_row.append(row[column_index])
            else:
                new_row.append('')
        new_writer.writerow(new_row)

    # Iterate over the rows in the processed file
    for row in processed_data[1:]:
        new_row = []
        for column_name in processed_column_names:
            if column_name in processed_column_names:
                column_index = processed_column_names.index(column_name)
                new_row.append(row[column_index])
            else:
                new_row.append('')
        new_writer.writerow(new_row)