def list_sum(my_list):
	res = 0
	for i in (my_list):
		res += i
	return res

my_list = [2, 5, 4, 8, 3, 9]
main_result = list_sum(my_list)
print(f' The sum of the list is: {main_result}')