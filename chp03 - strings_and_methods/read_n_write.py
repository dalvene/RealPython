my_output_file = open("hello.txt", 'w')
lines_to_write = ["This is my file.", "\n There are many like it,", "\nbut this one is mine."]
my_output_file.writelines(lines_to_write)
my_output_file.close()


my_output_file = open("hello.txt", 'a')
next_line = ["\nNON SEQUITUR"]
my_output_file.writelines(next_line)
my_output_file.close()

my_input_file = open("hello.txt",'r')
for line in my_input_file.readlines():
    print(line, end="")
my_input_file.close()
