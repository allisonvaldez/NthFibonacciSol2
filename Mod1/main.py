"""
time: O(n) since we are using memoization to save the base cases and
previously calculated values to save on processing time
space: O(n) space since it depends on the size of the array
"""

"""
Declare the parameters, however we want to initialize the hash table with the 
starting values of 1 pointing to 0, and 2 pointing to 1 as a dictionary data 
value (base cases).

The variable memoize represents a hash table.
"""


def get_nth_fib(num, memoize={1: 0, 2: 1}):
    """
    Uses the concept of memoization to calculate the fibonacci sequence. The
    if statement allows for easy access of previously calculated values as it
    just returns the previous key. Else if the number is not found in the hash
    table then we need to calculate it ourselves and store the value in the
    table.

    :param num: the number parameter
    :param memoize: the hash table that saves previously calculated values
    :return: the key of previously calculated value of sequence
    """
    if num in memoize:
        return memoize[num]
    else:
        memoize[num] = get_nth_fib(num-1) + (num-2)
        return memoize[num]


print(get_nth_fib(4))