def single_root_words(root_word,*other_words):
    same_words = []
    for item in other_words:
        if item.upper() in root_word.upper():
            same_words.append(item)
        elif root_word.upper() in item.upper():
            same_words.append(item)
    print('same_words', same_words)
result1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
print(result2)