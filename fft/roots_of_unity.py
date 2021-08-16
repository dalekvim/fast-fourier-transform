from cmath import exp, pi


class NthRootsOfUnity(list[complex]):
    """This calculates a list of the nth roots of unity.

    This is initialised with the order of the roots of unity we want to generate. The order of a cyclic group is
    smallest power you can raise them all to, to make the identity.

    Attributes
    ----------
    n : int
        The order of the roots.

    Methods
    -------
    squared() : NthRootsOfUnity
        Returns a list of the square of each of the roots of unity. The type
        was kept as NthRootsOfUnity for convenience.

    """

    def __init__(self, n: int):
        if n <= 0:
            raise ValueError()
        super(NthRootsOfUnity, self).__init__([exp((2j * pi * k) / n) for k in range(n)])
        self.n = n

    def copy_roots(self):
        """Creates a copy of the NthRootsOfUnity.

        :return: The nth root of unity where n was the input value at some point in time.
        """

        # TODO: Make this more efficient, if possible.
        return NthRootsOfUnity(self.n)

    def first_half(self):
        """
        :return: The first half of the NthRootsOfUnity.
        """

        middle = len(self) // 2
        tmp = self.copy_roots()
        while len(tmp) > middle:
            tmp.pop()
        return tmp

    def squared(self):
        """
        :return: The square of each of the roots of unity.
        """

        squared = [self[(2 * i) % len(self)] for i in range(len(self))]
        tmp = self.copy_roots()  # Returns a copy of self.
        for key, value in enumerate(tmp):
            if not (value in squared):
                tmp.pop(key)
        return tmp
