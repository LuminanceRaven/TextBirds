def errorHandling(error, number, details, solution):
    return error, number, details, solution

def reverse(text):
    reversed = text[::-1]
    if reversed == text:
        errorHandling("Palindrome", "1", "The string is a palindrome.", "Just leave the string normal.")
    else:
        return reversed

def charCount(text, spaces):
    if spaces == True:
            char_count = len(text)
            return char_count
    else:
        if ' ' in text:
            removed = text.replace(' ', '')
            char_count = len(text)
            return char_count
        else:
            errorHandling("No Spaces", "2", "The string doesn't have spaces.", "Change the spaces variable to ''True''.")

def uppercase(text):
    uppercased = text.upper()
    return uppercased

def lowercase(text):
    lowercased = text.lower()
    return lowercased

def removeSpaces(text):
    if ' ' in text:
        removed = text.replace(' ', '')
        return removed
    else:
        errorHandling("No Spaces", "2", "The string doesn't have spaces.", "Just leave the string normal.")

def removeChar(char, text):
    if char in text:
        removed = text.replace(char, '')
        return removed
    else: 
        errorHandling("No Character", "3", "The string doesn't have the character.", "Just leave the string normal.")        

def replaceChar(char, char2, text):
    if char in text:
        replaced = text.replace(char, char2)
        return replaced
    else:
        errorHandling("No Character", "3", "The string doesn't have the character.", "Just leave the string normal.")         

def similar(text, text2):
    if text == text2:
        return True
    else:
        return False
    
def checkChar(char, text):
    if char in text:
        return True
    else:
        return False

def isPalindrome(text):
    reversed = text[::-1]
    if text == reversed:
        return True
    else:
        return False
