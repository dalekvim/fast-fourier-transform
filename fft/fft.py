from .polynomial import Polynomial as Poly
from .roots_of_unity import NthRootsOfUnity


def smallest_power_of_two_not_less_than(n: int):
    """Does what it says on the tin."""

    i = 1
    while i < n:
        i *= 2
    return i


def adjust(sample_evens, sample_odds):
    if len(sample_evens) == 1:
        while len(sample_evens) < len(sample_odds):
            sample_evens.append(sample_evens[0])
    if len(sample_odds) == 1:
        while len(sample_odds) < len(sample_evens):
            sample_odds.append(sample_odds[0])
    return sample_evens, sample_odds


def fft(polynomial: Poly, roots_of_unity: NthRootsOfUnity = None) -> list[complex]:
    """This is a simple implementation of the Fast Fourier Transform (FFT).

    The FFT is an efficient algorithm for the Discrete Fourier Transform. This implementation converts polynomials
    from a coefficient representation to a sample representation.

    What makes the FFT 'fast' is the clever choice of inputs used to evaluate the polynomial, at two points,
    almost simultaneously. This combined with the fact that polynomials can be split into even and odd pairs in the
    following way::

        f(x) = e(x^2) + x*o(x^2)

    allows to create a divide and conquer algorithm that can evaluate a degree ``n`` polynomial at, at least, ``n`` points in
    ``O(n*log(n))``.
    """

    # START BASE CASE

    if polynomial.is_zero:  # Checks if it is the zero polynomial (has degree -1).
        return [0]

    if polynomial.is_constant:  # Checks if it is a constant polynomial (has degree zero).
        # You could have evaluated at an arbitrary integer in constant time, but I thought this was more elegant.
        return [polynomial[0]]  # Returns the constant term.

    # END BASE CASE

    if not roots_of_unity:
        # This section gives a default value to the roots_of_unity if it doesn't have one.
        # This couldn't have been done earlier since we needed to know the degree of the polynomial.
        n = smallest_power_of_two_not_less_than(polynomial.degree + 1)
        roots_of_unity = NthRootsOfUnity(n)

    # One very clever idea that the FFT uses is that, if there are an even number of roots of unity, when they are
    # squared term-wise, the resulting list repeats at the halfway point. The method first_half is used to remove
    # those repeated elements.

    # START DIVIDE STEP

    sample_evens = fft(polynomial.evens(), roots_of_unity.squared().first_half())
    sample_odds = fft(polynomial.odds(), roots_of_unity.squared().first_half())

    # END DIVIDE STEP

    # This part is just an implementation detail that insures that the polynomials are the same size; if lists aren't
    # the same size python's zip function may miss out some terms.
    sample_evens, sample_odds = adjust(sample_evens, sample_odds)

    # START CONQUER STEP

    # The use of two lists is just an implementation detail. The wo
    sample_first_half, sample_second_half = [], []

    for evens, odds, root in zip(sample_evens, sample_odds, roots_of_unity):
        sample_first_half.append(evens + root * odds)
        sample_second_half.append(evens - root * odds)

    # END CONQUER STEP

    return sample_first_half + sample_second_half
