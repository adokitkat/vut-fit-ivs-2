result = 0

class Math:

    def __init__(self, arg : str = None):
        global result

        if arg is None:
            self.val = result
        else:
            self.init_eval(str(arg))
            
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

    def __add__(self, other):
        tmp = self.val + other.val
        return Math(tmp)

    def __sub__(self, other):
        tmp = self.val - other.val
        return Math(tmp)

    def __mul__(self, other):
        tmp = self.val * other.val
        return Math(tmp)

    def __truediv__(self, other):
        tmp = self.val / other.val
        return Math(tmp)
    
    def __floordiv__(self, other):
        tmp = self.val // other.val
        return Math(tmp)

    def __mod__(self, other):
        tmp = self.val % other.val
        return Math(tmp)

    def __pow__(self, other):
        tmp = self.val ** other.val
        return Math(tmp) 

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

    def ln(self):
        n = 100000000.0
        if self.val <= 0:
            return "Math Error"
        return Math(round(n * ((self.val ** (1/n)) - 1), 8))

    def log(self, base):
        n = 100000000.0
        if self.val <= 0 or base <= 0:
            return "Math Error"
        tmp = (n * ((self.val ** (1/n)) - 1)) / (n * ((base ** (1/n)) - 1))
        return Math(round(tmp, 8))

    def C(self):
        global result
        result = 0
        return Math()

    def factorial(self):
        result = 1

        if type(self.val) is float or self.val < 0:
            #raise "Math Error"
            return "Math Error"

        for i in range(1,int((self.val)+1)):
            result *= i 
        return Math(result)

    def __str__(self):
        value = self.val
        try: # If float
            if value.is_integer():
                value = int(value)
                #if len(str(value)) > 19 :
                #    return "Out of range" 
            else:
                value = round(value, 15)
        except:
            pass

        return str(value)