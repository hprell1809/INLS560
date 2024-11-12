def sort_lines(input_file, output_file):
    with open (input_file, 'r') as f:
        lines = f.readlines()

    # Separate the first two lines to remain unsorted
    header = lines[:2]
    body = lines[2:]

    sorted_body = sorted(body, key=lambda line: line[0].lower(), reverse=True)

    sorted_lines = header + sorted_body

    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# Specify input and outfile file names
input_file = ''
output_file = ''

# Call the function to sort lines
sort_lines(input_file, output_file)