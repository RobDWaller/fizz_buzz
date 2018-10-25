'''
Facade module to execute the FizzBuzz test.
'''

from fizz_buzz.src.output import Output

def fizz_buzz():
    '''
    Executes fizz buzz output over the numbers 1 to 100 using a range.
    Prints out ouput of get_fizz_buzz method.
    '''

    for number in range(1, 101):

        print(Output.get_fizz_buzz(number))
