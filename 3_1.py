
calls = 0

def count_couls():
    global calls
    calls += 1

def string_info(string):
    count_couls()
    len_str = len(string)
    up_str = string.upper()
    lw_str = string.lower()
    str_info = (len_str,up_str,lw_str)
    print(str_info)

def is_contains(string, list_to_search):
    count_couls()
    if any(substr.upper() in string.upper() for substr in list_to_search):
        print(True)
    else:
        print(False)

print(string_info('LOL'))
print(string_info('akihABara'))

print(is_contains('Urban', ['ban', 'urBAN', 'ban']))
print(is_contains('ALOHA', ['AlohaAAA', 'asdwwWWW', 'A<loha', 'aLOha']))
print(calls)