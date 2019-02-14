def hello (a_name) :
	print("Hello " + a_name)

def hello2 (name_a, name_b) :
	print("Hello! " + name_a + " and " + name_b + "!")


def sum_two(x,y):
	z = x + y
	return z

def my_sum(a_list):
	total = 0
	for n in a_list:
		total = total + n
	return total

def my_count(a_list):
	count = 0
	for n in a_list:
		count = count + 1
	return count
# return number of items in the list

def my_prod(a_list):
	total = 1
	for n in a_list:
		total = total * n 
	return total

def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count

def my_count_ones(a_list):
	count = 0
	for n in a_list:
		if n == 1:
			count = count + 1
	return count

def is_list_empty(a_list):
	if my_count(a_list) == 0:
		return True
	else: False

def my_max(a_list):
	if is_list_empty(a_list):
		return None
	maximum = a_list[0]
	for n in a_list:
		if n > maximum:
			maximum = n
	return maximum


import os
def get_filenames(a_dirname):
	list_of_files = os.listdir(a_dirname)
	print("list of file names:")
	print(list_of_files)
	print("--------")
	all_files = []
	for filename in list_of_files:
		full_path = os.path.join(a_dirname,filename)
		if not os.path.isdir(full_path):
			all_files.append(full_path)	
	return all_files, list_of_files





