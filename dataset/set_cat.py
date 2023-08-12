import csv

# List of source CSV files
source_files = ['leetcode_questions_Array.csv', 'leetcode_questions_string.csv', 'leetcode_questions_Hash-Table.csv', 'leetcode_questions_dynamic_programming.csv', 'leetcode_questions_Math.csv', 'leetcode_questions_sorting.csv', 'leetcode_questions_Greedy.csv', 'leetcode_questions_Depth-First-Search.csv', 'leetcode_questions_database.csv', 'leetcode_questions_binary_search.csv', 'leetcode_questions_bfs.csv', 'leetcode_questions_tree.csv']  # Replace with your file names

concatenated_file = 'concatenated_data.csv'

# Create a new CSV file for writing
with open(concatenated_file, 'w', newline='', encoding='utf-8') as new_csvfile:
    csv_writer = csv.writer(new_csvfile)

    # Loop through each source CSV file
    for source_file in source_files:
        with open(source_file, 'r', newline='', encoding='utf-8') as source_csv:
            csv_reader = csv.reader(source_csv)
            
            # Skip the header if it exists in source files
            next(csv_reader)
            
            # Write each row from the source CSV to the concatenated CSV
            for row in csv_reader:
                csv_writer.writerow(row)

print("Concatenation completed.")