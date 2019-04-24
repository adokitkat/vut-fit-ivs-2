#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @file matematica.py
## @brief Math library
## @authors Jakub Mĺkvy, Adam Múdry, Daniel Paul, Peter Koprda
## @version 1.0
## @date May 2019

result = 0

## @brief Trieda Math
# @class Math
class Math:

    ## @brief Constructor 
    def __init__(self, arg : str = None):
        global result

        if arg is None:
            self.val = result
        else:
            self.init_eval(str(arg))
    
    ## @brief Tries to evaluate the expression
    # @param self.val In-class result of operation
    # @param result Global result of operation
    def init_eval(self, expr):
        global result

        try:
            tmp = eval(expr.replace('^','**'))
            self.val = tmp
            result = self.val
        except Exception as e:
            if str(e) == "division by zero":
                self.val = "Math Error"
            else:
                print(e)
                self.val = "Syntax Error"

    ## @brief Function for sum
    # @return sum of two numbers
    def __add__(self, other):
        tmp = self.val + other.val
        return Math(tmp)

    ## @brief Function for subtraction
    # @return subtracton of two numbers
    def __sub__(self, other):
        tmp = self.val - other.val
        return Math(tmp)

    ## @brief Function for multiplying
    # @return multiplication of two numbers
    def __mul__(self, other):
        tmp = self.val * other.val
        return Math(tmp)

    ## @brief Function for true division
    # @return division of two numbers, result may be float
    def __truediv__(self, other):
        tmp = self.val / other.val
        return Math(tmp)
    
    ## @brief Function for floor division
    # @return division of two numbers, result is integer
    def __floordiv__(self, other):
        tmp = self.val // other.val
        return Math(tmp)

    ## @brief Function for modulo
    # @return modulo of two numbers
    def __mod__(self, other):
        tmp = self.val % other.val
        return Math(tmp)

    ## @brief Function for power
    # @return squared number
    def __pow__(self, other):
        tmp = self.val ** other.val
        return Math(tmp) 

    ## @brief Function for square root
    # @pre n is unsigned integer
    # @return square root of number
    def root(self, n=None):

        if self.val < 0:
            return "Math Error"

        if n is None:
            tmp = self.val ** (1/2)
        else:
            try:
                if n.is_integer():
                    n = int(n)                
            except:
                pass

            if n != 0:
                tmp = self.val ** (1/n)
            else:
                return "Math Error"

        return Math(tmp)

    ## @brief Function for natural logarithm
    # @return natural logarithm of number
    def ln(self):
        n = 100000000.0
        if self.val <= 0:
            return "Math Error"
        return Math(round(n * ((self.val ** (1/n)) - 1), 8))

    ## @brief Function for logarithm
    # @return logarithm of number
    def log(self, base):
        n = 100000000.0
        if self.val <= 0 or base <= 0:
            return "Math Error"
        tmp = (n * ((self.val ** (1/n)) - 1)) / (n * ((base ** (1/n)) - 1))
        return Math(round(tmp, 8))

    ## @brief Function for clearing result screen
    # @return empty screen
    def C(self):
        global result
        result = 0
        return Math()

    ## @brief Function for factorial
    # @return factorial of a number
    def factorial(self):
        result = 1

        if type(self.val) is float or self.val < 0:
            return "Math Error"

        for i in range(1,int((self.val)+1)):
            result *= i 
        return Math(result)

    ## @brief Function for converting 
    # @exception parameter value is not a number
    # @return converted number
    def __str__(self):
        value = self.val
        try: # If float
            if value.is_integer():
                value = int(value)
            else:
                value = round(value, 15)
        except:
            pass

        return str(value)