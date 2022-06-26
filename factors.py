#!/usr/bin/python3
"""
   This module imports and factorize numbers
   from a files and prints output to stdout
"""
from sys import argv


class RSA_Factors:
    ''' class open and reads the file
        multiplying the entities in the file by the formula
        n = q * p
    '''
    def __init__(self, filename=None):
        '''
        set filename attribute
        '''
        if filename is not None:
            self.filename = filename

    def read_file(self):
        '''
        read from file
        '''
        try:
            with open(self.filename, encoding="utf-8") as file:
                buffer = file.readline()
                while buffer != "":
                    num = int(buffer.split('\n')[0])
                    self.factors(num)
                    buffer = file.readline()
        except ValueError as error:
            print(error)
        except FileNotFoundError as error:
            print(error)

    def factors(self, n):
        '''
        return the factors of a number
        '''
        i = 2

        if n < 2:
            print("Number less than 2")
            return
        while n % i:
            i += 1
        print("{:.0f}={:.0f}*{:d}".format(n, n / i, i))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: please provide file path")
    RSA_Factors(argv[1]).read_file()
