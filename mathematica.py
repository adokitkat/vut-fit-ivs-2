result = 0

class Math:

    def __init__(self, arg : str = None):
        
        global result

        if arg is None:
            self.val = result
        else:
            try:
                tmp = eval(str(arg).replace('^','**'))
            except:
                pass

            self.val = tmp
            result = self.val


    def __add__(self, other):

        tmp = self.val + other.val
        return Math(tmp)

    def __sub__(self, other):

        tmp = self.val - other.val
        return Math(tmp)

    def __mul__(self, other):

        tmp = self.val * other.val
        return Math(tmp)

    def __div__(self, other):

        tmp = self.val / other.val
        return Math(tmp)

    def __pow__(self, other):

        tmp = self.val ** other.val
        return Math(tmp) 

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

    def ln(self):
        n = 100000000.0
        return Math(n * ((self.val ** (1/n)) - 1))

    def log(self, base):
        tmp = Math.ln(self.val)/Math.ln(base)
        return Math(tmp)

    def C(self):
        global result
        result = 0
        return Math()


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