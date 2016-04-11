"""Summary."""
from __future__ import absolute_import


class Fraction(object):
    """docstring for Fraction."""

    def __init__(self, numerator, denominator=1, whole_number=0):
        """
        Constructor.

        Args:
            numerator (int): The numerator or top part of the fraction
            denominator (int): The denominator or bottom part of the fraction
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        if not isinstance(numerator, int) or not isinstance(denominator, int)\
                or not isinstance(whole_number, int):
            raise TypeError(
                'Invalid argument type. All argument must be integrers')

        self.top = (whole_number * denominator) + numerator
        self.denominator = denominator
        self.whole = whole_number
        self.numerator = numerator

    def __str__(self):
        """
        Magic method for returning formatted fraction output.

        Returns:
            name (TYPE): Formatted instance
        """
        return "{0} {1}/{2}".format(self.whole, self.top, self.denominator)

    def __unicode__(self):
        """
        Magic method for returning formatted fraction output.

        Returns:
            name (TYPE): Formatted instance
        """
        return "{0} {1}/{2}".format(self.whole, self.top, self.denominator)

    def __add__(self, other):
        """
        Addition magic method.

        Args:
            other (Fraction): The other fraction to add

        Returns:
            name (Fraction): New fraction instance
        """
        denominator = self.denominator * other.denominator
        numerator = (self.top * other.denominator) + \
            (other.top * self.denominator)

        whole = numerator // denominator
        numerator = numerator % denominator
        if not denominator % numerator:
            denominator = denominator // numerator

        return Fraction(numerator, denominator, whole)
