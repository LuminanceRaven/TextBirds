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
            char_count = len(removed) # Fixed the bug when it counts the text chararcter count and not the removed character count
            return char_count
        else:
            errorHandling("No Spaces", "2", "The string doesn't have spaces.", "Change the spaces variable to ''True''.")

# Deleted the uppercase and lowercase functions

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

def isPalindrome(text, spacesCount):
    reversed = text[::-1]
    if spacesCount != True:
        if text == reversed:
            return True
        else:
            return False
    else:
        removed = text.replace(' ', '')
        if removed == reversed:
            return True
        else:
            return False # Added a new function in the isPalindrome() function - with spaces
