my_file = open("D:\\my_directory\\my_binary_file.bin", "wb+")

my_string = b"one two three"
my_number = b"[1, 2, 3]"

my_file.write(my_string)
my_file.write(my_number)

my_file.seek(0)
binary_data = my_file.read()
print(binary_data)

my_file.close()