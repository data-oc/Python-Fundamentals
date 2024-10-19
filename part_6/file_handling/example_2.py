file_read = open("D:\\my_directory\\my_file_2.txt", "r", encoding="UTF-8")

employee_data_1 = file_read.read()
print(employee_data_1)

file_read.seek(0)
employee_data_2 = file_read.readline()
print(employee_data_2)

file_read.seek(0)
employee_data_3 = file_read.readlines()
print(employee_data_3)

file_read.close()