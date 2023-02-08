def ispalindrome(s):
    reverse = ''
    for car in s:
        reverse = car + reverse
    if s == reverse:
        return True
    else:
        return False

