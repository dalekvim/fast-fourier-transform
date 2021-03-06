"""This file contains the Polynomial class, created to quick and easy access to polynomials."""

from operator import add


class Polynomial(list):
    """This class represents polynomials as a list of coefficients.

    :example:

    .. code-block::

        import fft.Polynomial as Poly

        # f(x) = 1 + 2x + xx
        f = Poly([1, 2, 1])

        # The f is callable and will evaluate the polynomial at the input value.
        f(3) -> 16.

    Attributes
    ----------
    degree : int
        The largest power the variable is raised to in the polynomial.

    Methods
    -------
    add(polynomial_1 : list, polynomial_2 : list) : list
        Adds two polynomials and returns the result.

    adjust(polynomial_1 : list, polynomial_2 : list) : list
        Adds a buffer so that the two lists representing the polynomials are the same size.

    are_equal(polynomial_1 : list, polynomial_2 : list) : bool
        Compares the two input polynomials to check if they are the same.
    """

    def __init__(self, _list: list):
        """Initializes the polynomial as a list of coefficients."""

        super(Polynomial, self).__init__(_list)
        # The degree is the largest power term with nonzero coefficient.
        # It is calculated by first striping away any trailing zeros and
        self.degree = len(self.strip_zeros()) - 1
        self.is_zero = (self.degree == -1)
        self.is_constant = (self.degree == 0)

    def evens(self):
        """This returns a polynomial whose coefficients correspond to the even powers of x of the polynomial it is
        run on."""
        return Polynomial([self[2 * i] for i in range((len(self) + 1) // 2)])

    def odds(self):
        """This returns a polynomial whose coefficients correspond to the run powers of x of the polynomial it is
        run on."""
        return Polynomial([self[2 * i + 1] for i in range(len(self) // 2)])

    def __call__(self, x: complex) -> complex:
        """Element wise multiplies the coefficients of this polynomial with powers of x.

        :param x: Input to the polynomial.
        :return: The polynomial evaluated at x.
        """

        if not self:
            # The empty list represents the zero polynomial.
            return 0

        return self.horners_rule(x)

    @staticmethod
    def add(polynomial_1: list, polynomial_2: list) -> list:
        """Adds together two input polynomials and returns the result.

        :example:

        .. code-block::

            # (1 + 2x) + (3 + 2x + 5xx) = 4 + 4x + 5xx
            Poly.add([1, 2], [3, 2, 5]) -> [4, 4, 5]

        :return: The sum of the two polynomials.
        """

        polynomial_1, polynomial_2 = Polynomial.adjust(polynomial_1, polynomial_2)

        return list(map(add, polynomial_1, polynomial_2))

    @staticmethod
    def adjust(polynomial_1: list, polynomial_2: list) -> tuple[list, list]:
        """Insures that polynomials are the same size by adding zeros as buffer.

        This function is useful for the add method.

        :return: The two polynomials adjusted to have the same size.
        """

        while len(polynomial_1) < len(polynomial_2):
            polynomial_1.append(0)
        while len(polynomial_1) > len(polynomial_2):
            polynomial_2.append(0)
        return polynomial_1, polynomial_2

    @staticmethod
    def are_equal(polynomial_1: list, polynomial_2: list) -> bool:
        """Checks if two polynomials are equal.

        :return: Returns true if the polynomials are equal and false otherwise.
        """

        polynomial_1, polynomial_2 = Polynomial.strip_zeros_l([polynomial_1, polynomial_2])

        if polynomial_1 == polynomial_2:
            return True
        return False

    def horners_rule(self, x: complex) -> complex:
        """Evaluates this polynomial using Horner's Rule.

        Horner's Rule allows polynomials to be evaluated in linear time, whereas evaluating term by term would have a
        polynomial time complexity.

        :param x: Input to the polynomial.
        :return: The polynomial evaluated at the input.
        """

        subtotal = 0
        for coefficient in reversed(self):
            subtotal = coefficient + x * subtotal
        return subtotal

    def strip_zeros(self) -> list:
        """Removes any terms with coefficient zero from the end of the polynomial.

        :return: The polynomial as a list without trailing zeros.
        """

        if self:
            # First checks if the list of coefficients is nonempty.
            while self[-1] == 0:
                # Removes the last element if it is zero.
                self.pop()
                if not self:
                    # Breaks the while loop if list is empty.
                    break
        return self

    @staticmethod
    def strip_zeros_l(polynomials: list[list]) -> list[list]:
        """Strips zeros from a list of polynomials.

        :param polynomials: A list of polynomials.
        :return: The same polynomials with trailing terms with trailing zeros removed.
        """

        stripped_polynomials = []
        for polynomial in polynomials:
            stripped_polynomials.append(Polynomial(polynomial).strip_zeros())
        return stripped_polynomials
