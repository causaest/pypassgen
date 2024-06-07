import string
import random

SPECIAL_CHARS = [ "{", "}", "(", ")", "[", "]", "#", ";", ":", "^", ",", ".", 
                 "?", "!", "|", "&", "_", "`", "~", "@", "$", "%", "/", "+", 
                 "-", "=", "\\", "'", "\"" ]
EXCLUDED_CHARS = ["O", "0", "1", "l", "`", "'"]
# EXCLUDED_CHARS = EXCLUDED_CHARS + list(string.ascii_lowercase) + list(string.ascii_uppercase)

def main():
    """
    You should write your code here. 
    """
    pass_final = string_gen(length = 8, 
                            special = 1, 
                            exclude = EXCLUDED_CHARS, 
                            uppercase = True)
    # If a password has been generated, print it along with its strength
    if pass_final is None:
        print("No password has been generated.")
    else:
        print("Your randomly generated password is:", pass_final)
        strength_assess(pass_final)

def strength_assess(password):
    """
    Assesses the strength of a string when used as a password.
    The assessment is only based on length; more sophisticated methods 
    should be considered.
 
    Args:
        password (str): The string to assess its strength as password.

    Returns:
        None.
    """
    if len(password) <= 6:
        print("Password strength: weak")
    elif len(password) <= 10:
        print("Password strength: moderate")
    else:
        print("Password strength: strong")

def string_gen(length, special, exclude, uppercase = True):
    """
    Creates a string consisting of random characters drawn from a list.
 
    Args:
        length (int): The length of the desired string.
        exclude (list): A list of characters to be excluded from the list.
        uppercase (bool): Should uppercase letters be considered? 
        Default is True.
 
    Returns:
        str: A string of random characters.
    """
    char_set_alphanum = get_char_set(exclude, uppercase)
    # Too many excluded characters may result in an empty list
    if char_set_alphanum is None:
        return
    n_alphanum = length - special
    # Length should be grater than the number of special characters
    if n_alphanum <= 0:
        print("Length should be larger than number of special characters!")
        return
    # Randomly select alphanumeric characters
    char_lst_rand = random.choices(char_set_alphanum, k = n_alphanum)
    # Randomly select special characters
    char_lst_special = random.choices(SPECIAL_CHARS, k = special)
    # Unify the two lists
    char_lst_unified = char_lst_rand + char_lst_special
    # Shuffle so that special characters don't always go last
    random.shuffle(char_lst_unified)
    # Collapse the list into a single random string
    pass_rand = "".join(char_lst_unified)
    return(pass_rand)

def get_char_set(exclude, uppercase):
    """
    Creates a list of characters to be used as a pool to draw random 
    characters from.
 
    Args:
        exclude (list): A list of characters to be excluded from the list.
        uppercase (bool): Should uppercase letters be considered?
 
    Returns:
        list: A list of valid characters.
    """
    # Test if uppercase is boolean, as required
    if type(uppercase) != bool:
        raise TypeError("uppercase should be boolean")
    # Test if exclude is list, as required
    if type(exclude) != list:
        raise TypeError("exclude should be a list")
    # Create lists of lowercase and uppercase latin letters
    letters_lowercase = list(string.ascii_lowercase)
    letters_uppercase = list(string.ascii_uppercase)
    # Create list of digits as characters
    numbers = list(range(0, 10))
    numbers = list(map(str, numbers))
    # Create alphanumeric list
    char_set = numbers + letters_lowercase
    # Add uppercase letters, if required
    if uppercase == True:
        char_set = char_set + letters_uppercase
    # Exclude desired characters
    char_set_clean = []
    for character in char_set:
        if character not in exclude:
            char_set_clean.append(character)
    # Test if final list has sufficient number of characters
    # If not, return None
    if len(char_set_clean) <= 8:
        print("Too many excluded characters!")
        print("Please reduce excluded characters and try again.")
        return
    return(char_set_clean)

# Don't edit these next two lines
# They tell python to run main function
if __name__ == '__main__':
    main()
