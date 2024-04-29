'''
    A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps
    that takes a float as a parameter, representing the number of feet walked, and returns an
    integer that represents the number of steps walked. Then, write a main program that reads
    the number of feet walked as an input, calls function feet_to_steps() with the input as
    an argument, and outputs the number of steps as an integer.
    Use floating-point arithmetic to perform the conversion.

    Ex: If the input is:
        150.5
    the output is:
        60

    The program must define and call the following function:
    def feet_to_steps(user_feet)
'''

# Define your function here
def feet_to_steps(user_steps):
    result = int(user_steps / 2.5)
    return result

if __name__ == '__main__':
    user_steps = float(input('Enter the amount of steps you took: '))
    print(feet_to_steps(user_steps))