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

    def __mul__(self, other):

        tmp = self.val * other.val
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


    def C(self):
        global result
        result = 0
        return Math()


    def __str__(self):

        tmp = self.val
        
        try: # If float
            if tmp.is_integer():
                tmp = int(tmp)
            else:
                tmp = round(tmp, 15)
        except:
            pass

        return str(tmp)