def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File not found."

file_path = "example.txt" 
print(count_lines_in_file(file_path)) 
