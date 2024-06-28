#%%
class Calculations:
    """Calculation Application
        This is a simple calculator app. 
        It does basic arithmetic calculations 
        (Addition, Subtraction,
         Multiplication, Division,
         Modulus. Exponent, Floor Division)
    """
    def __init__(self, a, b):
        """Init Summary
        Initiates the entries to use for calculation.

        Args:
            a (integer or float): first input for calculation
            b (integer or float): second input for calculation
        """
        self.a = a
        self.b = b

    def get_sum(self):
        """get_sum method

        Returns: the sum of a and b
        """
        return self.a + self.b

    def get_difference(self):
        """get_difference method

        Returns: the difference between a and b
        """
        return self.a - self.b

    def get_product(self):
        """get_method method

        Returns: the product of a and b
        """        
        return self.a * self.b

    def get_division(self):
        """get_division method

        Returns: the division of a and b
        """        
        return self.a / self.b
    
    def get_modulus(self):
        """get_difference method

        Returns: the difference between a and b
        """          
        return self.a % self.b
    
    def get_exponent(self):
        """get_exponent method

        Returns: the exponent of a and b
        """
        return self.a  ** self.b
    
    def get_floordiv(self):
        """get_floordiv method

        Returns: the floor division between a and b
        """
        return self.a // self.b



        # %%

