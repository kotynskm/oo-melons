"""Classes for melon orders."""

import random
import datetime


class TooManyMelonsError(ValueError):
    """Error to raise when too many melons are ordered."""

    def __init__(self):
        """Initialize TooManyMelonsError using init method from ValueError."""

        super().__init__("No more than 100 melons!")


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species

        if qty > 100:
            raise TooManyMelonsError

        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        """Calculate base price using splurge pricing and rush hour fee."""

        # Splurge rate
        base_price = random.randrange(5, 10)

        now = datetime.datetime.now()

        # Is it rush hour?
        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order purchased by the US Government."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record whether the melon order has passed inspection or not."""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order from within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
