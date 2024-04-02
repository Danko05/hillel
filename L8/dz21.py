def is_palindrome(text):
    text = ''.join(i for i in text if i.isalnum()).lower()
    if text == text[::-1]:
        return True
    else:
        return False



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
