import numpy as np

class DualNumber:
    """
    Implementation of a Dual Number with support for custom operations for Automatic Differentiation.
    
    Attributes:
        real: int, float
            The real part of the dual number, carries the primal trace in AD.
            After the AD process, this carries the result of the function applied to the input value.
        
        dual: int, float
            The dual part of the dual number, will carry the tangent trace in AD.
            After the AD process, this carries the result of the derivative of the function applied to the input value.
    """

    def __init__(self, real, dual = 1):
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
            >>> x = DualNumber(1, 2)
            DualNumber(real = 1, dual = 2)
        """
        self.real = real
        self.dual = dual

    def __repr__(self):
        """
        Prints the the class (self) in the form: DualNumber(real = real, dual = dual)
        
        Parameters:
            self: the DualNumber object
        
        Returns:
            Dual object with real and dual components
        
        Examples:
            >>> dual_number = DualNumber(3, 1)
            >>> print(dual_number)
            
            DualNumber(real=3, dual=1)
        """
        return "{name}(real={real}, dual={dual})".format(name = type(self).__name__, real = self.real, dual = self.dual)
    
    def __pos__(self):
        """
        Returns the positive of self
        
        Parameters:
            self: the DualNumber object
        
        Returns:
            DualNumber object equivalent to the positive self
        
        Examples:
            >>> dual_number = + DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=3, dual=1)
        """
        return DualNumber(self.real, self.dual)

    def __neg__(self):
        """
        Returns the negative of self
        
        Parameters:
            self: the DualNumber object
        
        Returns:
            DualNumber object equivalent to the negative self
        
        Examples:
            >>> dual_number = - DualNumber(3, 1)
            >>> print(dual_number)
            
            DualNumber(real=-3, dual=-1)
        """
        return DualNumber(-self.real, -self.dual)

    def __add__(self, other):
        """
        Returns the addition of self and other
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the addition of self and other
        
        Examples:
            >>> dual_number = DualNumber(2, 1) + DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=5, dual=2)
            
            >>> dual_number =  DualNumber(3, 2) + 2
            >>> print(dual_number)

            DualNumber(real=5, dual=2)
        """

        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError('Other can only be of types ', (int, float, DualNumber))
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real, self.dual + other.dual)
        else:
            return DualNumber(self.real + other, self.dual)

    def __radd__(self, other):
        """
        Returns the addition of other and self
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber
    
        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the addition of other and self
        
        Examples:
            >>> dual_number = DualNumber(2, 1) + DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=5, dual=2)
            
            >>> dual_number =  2 + DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=5, dual=2)
        """

        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError('Other can only be of types ', (int, float, DualNumber))
        return self + DualNumber(other, 0)

    def __sub__(self, other):
        """
        Returns the subtraction of self and other
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the addition of self and other
        
        Examples:
            >>> dual_number = DualNumber(2, 1) - DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=-1, dual=0)
            
            >>> dual_number =  DualNumber(3, 2) - 2
            >>> print(dual_number)

            DualNumber(real=1, dual=2)
        """

        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError('Other can only be of types ', (int, float, DualNumber))
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real, self.dual - other.dual)
        else:
            return DualNumber(self.real - other, self.dual)

    def __rsub__(self, other):
        """
        Returns the subtraction of other and self
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the subtraction of other and self
        
        Examples:
            >>> dual_number = DualNumber(2, 1) - DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=-1, dual=0)
            
            >>> dual_number =  2 - DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=-1, dual=-2)
        """

        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError('Other can only be of types ', (int, float, DualNumber))
        return -1 * self + DualNumber(other, 0)

    def __mul__(self, other):
        """
        Returns the multiplication of self and other
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the multiplication of self and other
        
        Examples:
            >>> dual_number = DualNumber(2, 1) * DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=6, dual=5)
            
            >>> dual_number =  DualNumber(3, 2) * 2
            >>> print(dual_number)

            DualNumber(real=6, dual=4)
        """
        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError(f"Unsupported type `{type(other)}`")
        if isinstance(other, (int, float)):
            # scalar numbers
            return DualNumber(other * self.real, other * self.dual)
        else:
            # dual number
            return DualNumber(
                self.real * other.real,
                self.real * other.dual + self.dual * other.real)

    def __rmul__(self, other):
        """
        Returns the multiplication of other and self
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the multiplication of other and self
        
        Examples:
            >>> dual_number = DualNumber(2, 1) * DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=6, dual=5)
            
            >>> dual_number =  2 * DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=6, dual=4)
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Returns the division of self and other
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the division of self and other
        
        Examples:
            >>> dual_number = DualNumber(1, 1) / DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=0.3333333333333333, dual=0.2222222222222222)
            
            >>> dual_number =  DualNumber(1, 1) / 2
            >>> print(dual_number)

            DualNumber(real=0.5, dual=0.5)
        """

        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError(f"Unsupported type `{type(other)}`")

        if isinstance(other, DualNumber):
            return DualNumber(self.real / other.real, (self.dual * other.real - self.real * other.dual) / other.real ** 2)
        else:
            return DualNumber((self.real * other) / other ** 2, (self.dual * other) / other ** 2)
   
    def __rtruediv__(self, other):
        """
        Returns the division of other and self
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber
        
        Returns:
            DualNumber object equivalent to the division of other and self
        
        Examples:
            >>> dual_number = DualNumber(1, 1) / DualNumber(3, 1)
            >>> print(dual_number)

            DualNumber(real=0.3333333333333333, dual=0.2222222222222222)
            
            >>> dual_number =  2 / DualNumber(1, 1)
            >>> print(dual_number)

            DualNumber(real=2.0, dual=-2.0)
        """
        
        return DualNumber((self.real * other) / self.real ** 2, (-self.dual * other) / self.real ** 2)

    def __pow__(self, other):
        """
        Returns the power of self by other
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the power of self by other
        
        Examples:
            >>> dual_number = DualNumber(2, 3) ** DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=8, dual=47.090354888959126)
            
            >>> dual_number =  DualNumber(3, 2) ** 2
            >>> print(dual_number)

            DualNumber(real=9, dual=12)
        """
        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError(f"Unsupported type `{type(other)}`")

        if isinstance(other, DualNumber):
            factored = self.real ** (other.real -1)
            sum_a = other.real * self.dual
            sum_b = np.log(self.real) * self.real * other.dual
            pow_dual = factored * (sum_a + sum_b)
            return DualNumber(self.real ** other.real, pow_dual)
        else:
            pow_dual = other * self.real ** (other-1) * self.dual
            return DualNumber(self.real ** other, pow_dual)

    def __rpow__(self, other):
        """
        Returns the power of other by self
        
        Parameters:
            self: the DualNumber object
            other: int, float or DualNumber

        Raises:
            TypeError
                If the type of input x is not supported
        
        Returns:
            DualNumber object equivalent to the power of other by self
        
        Examples:
            >>> dual_number = DualNumber(2, 3) ** DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=8, dual=47.090354888959126)
            
            >>> dual_number =  2 ** DualNumber(3, 2)
            >>> print(dual_number)

            DualNumber(real=8, dual=11.090354888959125)
        """
        return DualNumber(other ** self.real, np.log(other) * other ** self.real * self.dual)
    
    def __eq__(self, other):    
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 2, dual = 1)
        >>> print(x == y)
        False
        """

        if isinstance(other, int) or isinstance(other, float):
            return self.dual == 0 and self.real == other
        elif isinstance(other, DualNumber):
            return self.dual == other.dual and self.real == other.real
        else:
            raise ValueError("Invalid type")    
        
    def __ne__(self, other):
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 1, dual = 2)
        >>> print(x != y)
        False
        """

        return not self.__eq__(other)

    def __lt__(self, other):  
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 1, dual = 2)
        >>> print(x < y)
        False
        """

    
        if isinstance(other, int) or isinstance(other, float):
            return self.real < other
        elif isinstance(other, DualNumber):
            return self.real < other.real
        else:
            raise ValueError("Invalid type")    
    
    def __le__(self, other):
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 1, dual = 2)
        >>> print(x <= y)
        True
        """


        if isinstance(other, int) or isinstance(other, float):
            return self.real <= other
        elif isinstance(other, DualNumber):
            return self.real <= other.real
        else:
            raise ValueError("Invalid type")

    def __gt__(self, other):
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 1, dual = 2)
        >>> print(x > y)
        False
        """

        if isinstance(other, int) or isinstance(other, float):
            return self.real > other
        elif isinstance(other, DualNumber):
            return self.real > other.real
        else:
            raise ValueError("Invalid type")

    def __ge__(self, other):
        """
        Inputs
            real: int, float
                The real part of the dual number.
                The input corresponds to the value for which f'(x) will be evaluated.

            dual: int, float
                The dual part of the dual number. The input corresponds to the seed vector.

        Examples:
        >>> x = DualNumber(1, 2)
        >>> y = DualNumber(real = 1, dual = 2)
        >>> print(x >= y) 
        True
        """

        if isinstance(other, int) or isinstance(other, float):
            return self.real >= other
        elif isinstance(other, DualNumber):
            return self.real >= other.real
        else:
            raise ValueError("Invalid type")
