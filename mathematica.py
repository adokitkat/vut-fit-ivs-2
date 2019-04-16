## @file matematica.py
# @brief Matematická knižnica
# @author Jakub Mĺkvy 
# @author Adam Múdry
# @author Daniel Paul
# @author Peter Koprda
# @version 1.0
# @date Máj 2019

result = 0

## @brief Trieda Math
# @class Math
class Math:
    

    ## @brief Konštruktor 
    # @param result Výsledok operácie
    def __init__(self, arg : str = None):
        global result

        if arg is None:
            self.val = result
        else:
            try:
                tmp = eval(str(arg).replace('^','**'))
            except:
                pass ###

            self.val = tmp
            result = self.val

    ## @brief Funkcia na súčet
    # @return Súčet dvoch čísel
    def __add__(self, other):

        tmp = self.val + other.val
        return Math(tmp)

    ## @brief Funkcia na rozdiel
    # @return Rozdiel dvoch čísel
    def __sub__(self, other):

        tmp = self.val - other.val
        return Math(tmp)

    ## @brief Funkcia na súčin
    # @return Súčin dvoch čísel
    def __mul__(self, other):

        tmp = self.val * other.val
        return Math(tmp)

    ## @brief Funkcia na podiel
    # @return Podiel dvoch čísel
    def __div__(self, other):

        tmp = self.val / other.val
        return Math(tmp)

    ## @brief Funkcia na mocninu
    # @return Umocnené číslo
    def __pow__(self, other):

        tmp = self.val ** other.val
        return Math(tmp) 

    ## @brief Funkcia na obecnú odmocninu
    # @pre n je prirodzené číslo
    # @return Odmocnené číslo
    def root(self, n=None):

        if n is None:
            tmp = self.val ** (1/2)
        else:
            try:
                if n.is_integer():
                    n = int (n)                
            except:
                pass

            if n != 0:
                tmp = self.val ** (1/n)
            else:
                print("Math Error") ####
                raise ZeroDivisionError

        return Math(tmp)

    ## @brief Funkcia na dekadický logaritmus
    # @return Dekadický logaritmus z čísla n
    def ln(self):
        n = 100000000.0
        return Math(n * ((self.val ** (1/n)) - 1))

    ## @brief Funkcia na logaritmus
    # @return Logaritmus
    def log(self, base):
        tmp = Math.ln(self.val)/Math.ln(base)
        return Math(tmp)

    ## @brief Funkcia na čistenie stdin
    # @return Vyčistený stdin
    def C(self):
        global result
        result = 0
        return Math()

    ## @brief Funkcia na konvertovanie dátových typov
    # @exception parameter value nie je číslo
    # @return prekonvertované číslo na string
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