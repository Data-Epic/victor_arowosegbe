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

        Returns: the modulus between a and b
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

    
    
def get_valid_inputs(prompt):
        """
        Prompts the user to enter a valid floating-point number.
        
        Args:
            prompt (str): The input prompt for the user.
            
        Returns:
            float: The validated floating-point number.
        """
        while True:
            try:
                user_input = float(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a number.")

    

def main():
    """
    The main function to run the calculator app, providing a menu for the user to select operations.
    """
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponent")
        print("7. Floor Division")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            a = get_valid_operand("Enter the first operand: ")
            b = get_valid_operand("Enter the second operand: ")

            calc = Calculations(a, b)

            operations = {
                '1': calc.get_sum,
                '2': calc.get_difference,
                '3': calc.get_product,
                '4': calc.get_division,
                '5': calc.get_modulus,
                '6': calc.get_exponent,
                '7': calc.get_floordiv
            }

            try:
                result = operations[choice]()
                print(f"The result is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '8':
            print("Exiting the calculator app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



        # %%

