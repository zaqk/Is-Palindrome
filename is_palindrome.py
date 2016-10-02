

def isPalindrome(string):

    print('is ' + str(string) + ' a palindrome? ', end='')

    if string == None:
        print(str(False))

    elif len(string) <= 1:
        print(str(False))


    elif string.lower() == string[::-1].lower():
        print(str(True))

    else:
        print(str(False))






isPalindrome('racecar')
isPalindrome(None)
isPalindrome('a')
isPalindrome('test')
isPalindrome('test2')
isPalindrome('Palindromeemordnilap')
isPalindrome('')