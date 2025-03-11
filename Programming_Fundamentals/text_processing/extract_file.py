file_path = input().split("\\")

file_name_type = file_path[-1].split(".")

print(f"File name: {file_name_type[0]}")
print(f"File extension: {file_name_type[1]}")