"""Summary."""
from __future__ import absolute_import


class Fraction(object):
    """docstring for Fraction."""

    def __init__(self, numerator, denominator):
        """
        Constructor.

        Args:
            numerator (int): The numerator or top part of the fraction
            denominator (int): The denominator or bottom part of the fraction
        """
        self.top = numerator
        self.bottom = denominator

    def __str__(self):
        """
        Magic method for returning formatted fraction output.

        Returns:
            name (TYPE): Formatted instance
        """
        return "{} : {}/{}".format(self, self.top, self.bottom)

    def __unicode__(self):
        """
        Magic method for returning formatted fraction output.

        Returns:
            name (TYPE): Formatted instance
        """
        return "{} : {}/{}".format(self, self.top, self.bottom)
