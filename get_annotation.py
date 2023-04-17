import os
import sys
import pandas as pd

# Define path to extract_gff3_annotation.py script relative to project root
extract_script_path = os.path.join(os.path.dirname(__file__), 'extract_annotation_gff.py')
#extract_script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'myscripts', 'extract_annotation_gff.py')

print(extract_script_path)

# Check if input file path is provided
if len(sys.argv) < 3:
    print("Please provide table file path and input file path as arguments")
    sys.exit(1)

# Read in table with start_position, end_position, and chromosome_name columns
table_path = sys.argv[1]
table = pd.read_csv(table_path)

# Get input file path
input_file_path = sys.argv[2]

# Loop over rows in table and extract annotations for each chromosome
for _, row in table.iterrows():
    # Define output filename as chromosome_name.txt relative to project root
    output_filename = os.path.join(os.path.dirname(__file__), '..', 'reports', 'GWAS', 'outliers', 'annotation', f"{row['chromosome_name']}.txt")
    
    # Build command string to execute extract_gff3_annotation.py script with input file path provided as argument
    command_str = f"python {extract_script_path} {input_file_path} {row['start_position']} {row['end_position']} {row['chromosome_name']} > {output_filename}"
    
    # Execute command in shell
    os.system(command_str)
