def print_params(a, b, c):
    print(a, b, c)

values_list = [1, 'DOne', 123.1234]
values_list1 = [1, 'DOne']
values_list2 = [2]
print_params(*values_list)
print_params(*values_list1, 2)

values_dict = {'a': 31, 'b': 'Harrararra', 'c': 1231.4562}
print_params(**values_dict)
values_dict = {'b': 31, 'c': 1231.4562}
print_params(*values_list2, **values_dict)


# print_params(c = '23414')
# print_params(1,2)
