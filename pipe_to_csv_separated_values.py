import sys

def transform_line(line):
    columns = line.split("|")
    output_line = []

    for column in columns:
        value = column 
        if '"' in column:
            value = column.replace('"', '""')
        
        if "," in column:
            value = '"' + value + '"'
        
        output_line.append(value)
    return ",".join(output_line)
            

def transform_file(input_file_name, output_file_name):
    final_string = []
    
    with open(input_file_name, "r") as my_file:
        
        for line in my_file:
            final_string.append(transform_line(line))
        
    with open(output_file_name, "w") as outfile:
        outfile.write("".join(final_string))

if __name__ == "__main__":
    args = sys.argv
    transform_file(args[1], args[2])