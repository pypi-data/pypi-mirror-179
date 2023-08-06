class Water:
    """
    This class is used to testing import and package code.
    """
    
    # * testing functions
    def add( num1, num2, stringify=False):
        """Adds 2 given numbers

        Args:
            num1 (int): This variable will be the one added by num2
            num2 (int): This variable will add to num1
            stringify (bool, optional): Formats the output into a complete sentence. Defaults to False.
        """
        
        if stringify == False:
            return(num1 + num2)
        else:
            return(f"The output for adding {num1} and {num2} is {num1 + num2}")
    
    
    def sub(num1, num2, stringify=False):
        """Subtracts 2 given numbers

        Args:
            num1 (int): This variable will be the one subtracted by num2
            num2 (int): This variable will subtract num1
            stringify (bool, optional): Formats the output into a complete sentence. Defaults to False.
        """
        
        if stringify == False:
            return(num1 - num2)
        else:
            return(f"The output for subtracting {num1} and {num2} is {num1 - num2}")
    
    
    def multiply(num1, num2, stringify=False):
        """Multiply 2 given numbers

        Args:
            num1 (int): This variable will be the one multiplied by num2
            num2 (int): This variable will multiply num1
            stringify (bool, optional): Formats the output into a complete sentence. Defaults to False.
        """
        
        if stringify == False:
            return(num1 * num2)
        else:
            return(f"The output for multiplying {num1} and {num2} is {num1 * num2}")
    
    
    def div(num1, num2, stringify=False):
        """Divides 2 given numbers

        Args:
            num1 (int): This variable will be the one divided by num2
            num2 (int): This variable will divide num1
            stringify (bool, optional): Formats the output into a complete sentence. Defaults to False.
        """
        
        if stringify == False:
            return(num1 / num2)
        else:
            return(f"The output for dividing {num1} and {num2} is {num1 / num2}")
