import math #Import the math module

def is_prime(num):
    '''
    This function will determine whether a given integer is prime or not.
    Input: An integer.
    Output: True/False Statement
    :param num:
    :return:
    '''
    if num % 2 == 0 and num > 2: #All even numbers greater than 2 are not prime.
        return False
    for i in range(3, int(math.sqrt(num)+1), 2): #All odd numbers from 3 up to (but not including its sqrt)+1
        if num % i == 0:
            return False
    return True
