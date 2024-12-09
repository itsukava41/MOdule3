def get_multiplied_digits(number):
    str_number = str(number)
    print(str_number,'str_number')
    first = int(str_number[0])
    if first == 0:
        first = 1
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
result1 = get_multiplied_digits(402030)
print(result1)
result2 = get_multiplied_digits(40203)
print(result2)
result3 = get_multiplied_digits(4)
print(result3)