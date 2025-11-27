def print_fibonacci(n):
    """
    Generates the Fibonacci sequence up to the specified length 'n' and prints it.

    The Fibonacci sequence starts with 0 and 1, and each subsequent
    number is the sum of the two preceding ones.

    Args:
        n (int): The desired length of the Fibonacci sequence list.
    """
    if n <= 0:
        fib_list = []
    elif n == 1:
        fib_list = [0]
    else:
        # Initialize the sequence with the first two mandatory numbers
        fib_list = [0, 1]

        # Use a while loop to continue adding numbers until the list reaches length n
        while len(fib_list) < n:
            # The next number is the sum of the last two numbers in the list
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)

    # Change: Print the list instead of returning it
    print(fib_list)

    """
    Generates and returns a list containing the Fibonacci sequence
    up to the specified length 'n'.

    The Fibonacci sequence starts with 0 and 1, and each subsequent
    number is the sum of the two preceding ones.

    Args:
        n (int): The desired length of the Fibonacci sequence list.

    Returns:
        list: A list of integers representing the Fibonacci sequence.
    """
    if n <= 0:
        # If the length is 0 or less, return an empty list
        return []
    elif n == 1:
        # If the length is 1, return the sequence with just the starting element
        return [0]

    # Initialize the sequence with the first two mandatory numbers
    fib_list = [0, 1]

    # Use a while loop to continue adding numbers until the list reaches length n
    # We start with 2 elements already, so we continue until len(fib_list) == n
    while len(fib_list) < n:
        # The next number is the sum of the last two numbers in the list
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    return fib_list