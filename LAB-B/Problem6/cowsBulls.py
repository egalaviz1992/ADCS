import random

def gen_num():
    """
    Description:
        Generates a 4 digit numbers with non repeated digits
    Input:
        (None)        
    Output:
        (String) A 4 digit number with non repeated digits
    """
    number = ''.join(random.sample("0123456789", 4))
    return number

def count_cows_bulls(base_num, user_num):
    """
    Description:
        Count the number of cows and bulls from the given number (user_num)
        against the base_number.
    Input:
        base_num(String): the base number
        user_num(String): number given by the user
    Output: 
        (tuple) A tuple of 2 elements,(cows,bulls) with the number 
        of cows and bulls got by the user with his/her guess    
        None if any of both input numbers is not a valid number.
    """
    cows = 0
    bulls = 0
    
    
    if verify_num(base_num) == False or   verify_num(user_num) == False:
        return None
    for i in range(0,len(user_num)):
        if base_num[i] == user_num[i]:
            cows += 1
        elif user_num[i] in list(base_num):
            bulls += 1
    return (cows, bulls)        

def any_repeated_digit(num):
    """
    Description:
        Check if a number has repeated digit:
    Input:
        num (String): a number in string type
    Output:
        True if has at least one repeated digit
        False if num has not repeated digit
    """
    chars = list(num)
    my_set = set()
    for i in chars:
        if i in my_set:
            return True
        my_set.add(i)
    return False     

def verify_num(num):
    """
    Description:
        Verify if num is a correc 4 digit number with non repeated digits
    Input:
        num(String): number to verify
    Output:
        True: Valid number
        False: Invalid number
    """
    if len(num) != 4:
        return False 
    if any_repeated_digit(num):
        return False
    return True    
        
def get_user_num():
    """
    Description:
        It get from stdin the user input number to be compared with base number
    Input:
        None
    Output:
        user_num(String): The number provided by user
    """
    user_num = str(input("Enter your guess: "))
    while verify_num(user_num) == False:
        user_num = str(input("Bad number. Intro a 4 digit(non repeated) number:"))
    return user_num
        

def play(list_in=None,base_num = None):
    """
    Description:
        Play cows and bulls game. If list_in is None means that code will run
        in interactive mode, base_num will be generated randomly,
        user will introduce by keyboard the guesses
        and it will return the number of attemps to win. 
        If list_in is not empty, code will run in non_interactive mode 
        (designed for testing) and will evaluate any number in the list against 
        base_num given as argument as well, it will return the number of 
        attemps required to reach the goal or -1 if the list didn't contain 
        the correct answer.
        Note that, no valid number (number of any other amout of digit or)
            number with repeated digit doesn't increase attemps counter.
    Input: 
        list_in(list): List of number in string format
        base_num(string): Base number in string format
    Ouput:
        -1  : Case of non interactive mode (for testing) and list passed
              has not the correct number or base_num is not valid number
       <int>: A positive integer that contains the number of attemps to win
             the gamein both cases (interactive and non interactive mode)  
    """
    attemps = 0
    print("*****Welcome to Cows and Bulls Game*****")
    # Interactive mode
    if list_in == None:
        base_num = gen_num()
        user_num = "inf"
        #print(base_num)  
        while user_num != base_num:
            user_num = get_user_num()
            cows, bulls = count_cows_bulls(base_num, user_num)
            print ("Cows:%s --- Bulls:%s"%(cows,bulls))
            attemps += 1
        print("**************************************")
        print("Congratulation!!!!!!")
        print("You have won")
        print("Attemps: %s" % (attemps))
        print("**************************************")
        return attemps
    else:
        if verify_num(base_num) == False:
            return -1;
        for i in list_in:
            if (verify_num(i)):
                attemps +=1
            if i == base_num:
                return attemps
        return -1;
#play()
