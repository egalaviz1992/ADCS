
def is_even(str_in):
    """
	Input:
 	    str_in: Input string
	Output:
            True if str_in has a even lenght
            False if str_in has a odd lenght	
    """
    if len(str_in)%2 == 0:
        return True
    else:
        return False

def split_string(str_in):
    """
	Description:
	    This function splits the given string in 2 equal size strings
	    and return them in a tuple. If the input string has odd lengh, 
            the character in the middle is ignored.
	Input:
	    str_in(String): The input string to split
	Output
	    tup_out(tuple): A tuple with the 2 strings of the result
    """
    if is_even(str_in):
        return (str_in[0 : int(len(str_in)/2)], str_in[int(len(str_in)/2) : len(str_in)])
    else:
        return (str_in[0 : int(len(str_in)/2)], str_in[int(len(str_in)/2+1) : len(str_in)])

def is_palindrome(str_in):
    """
	Input: 
     	    str_in(String): Input string
	Output: 
	    True if the input string is a palindrome, False otherwise.  
    """ 

    str1, str2 = split_string(str_in)
    
    #Reverse string
    str2 = str2[::-1]

    if str1 == str2:
        return True
    else:
        return False
    

    

