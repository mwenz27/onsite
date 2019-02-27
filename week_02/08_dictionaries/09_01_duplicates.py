'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.
'''


def has_duplicates(l): # l is parameter, while lis is the argument
    '''
    This function takes in a list
    :return: True if there is any element duplicated
    '''
    d = {}
    for i in l:
        d[i] = 0
    if len(d) != len(l):
        return True


lis = [1,2,3,4,5,2]
print(has_duplicates(lis))






