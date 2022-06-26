#!/usr/bin/python3
from sys import argv
from math import sqrt

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
        with open(self.filename, encoding="utf-8") as file:
            buffer = file.readlines()
        buffer_int = []
        for line in buffer:
            buffer_int.append(int(line))
        return buffer_int
    def factors(self, n):
        '''
        return the factors of a number
        '''
        for i in range (2, n):
            if n == ((n // i) * i):
                print("{}={}*{}".format(n, (n // i), i))
                break
    def iterate(self):
        '''
        iterate through the file
        '''
        int_list = self.read_file()
        for n in int_list:
            self.factors(n)
if __name__ == "__main__":
    RSA_Factors(argv[1]).iterate()
