
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
with open('new_file.csv', 'w', newline='') as new_file:
    new_writer = csv.writer(new_file)

    # Get the column names from the processed file
    processed_column_names = processed_data[0]

    # Get the column names from the question file
    question_column_names = question_data[0]

    # Write the header row
    new_writer.writerow(processed_column_names)

    # Iterate over the rows in the question file
    for row in question_data[1:]:
        new_row = []
        for column_name in processed_column_names:
            if column_name in question_column_names:
                column_index = question_column_names.index(column_name)
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
        
