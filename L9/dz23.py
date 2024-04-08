def popular_words(text, words):
    text1 = text.lower()
    my_list = text1.split(' ')
    result = {}
    for i in words:
        counter = my_list.count(i)
        result[i] = counter
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
