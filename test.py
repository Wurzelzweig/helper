#########################################################################################
################################## This is a file #######################################
#########################################################################################


def create_random_string(length: int) -> str:
    '''
    This function will create a random string 
    by using the parameter length for the number
    of characters will be used.

    :param length: An integer number for the length
    of the string which will be created.
    :param type: int
    :return: str
    '''
    import random
    import string
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
